terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.116.0"
    }
    azapi = {
      source  = "azure/azapi"
      version = "~> 2.1.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# ==== 參數 ====
variable "location" {
  description = "部署區域"
  type        = string
  default     = "eastus2"
}

variable "resource_group_name" {
  description = "資源群組名稱"
  type        = string
  default     = "rg-landing-zone"
}

variable "hub_name" {
  description = "Foundry Hub (AML Workspace) 名稱"
  type        = string
  default     = "ml-foundry-hub"
}

variable "vnet_cidr" {
  description = "虛擬網路 CIDR"
  type        = string
  default     = "10.10.0.0/16"
}

variable "subnet_cidr" {
  description = "子網路 CIDR"
  type        = string
  default     = "10.10.1.0/24"
}

# ==== 基礎資源 ====
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

# 建立虛擬網路與子網路（登陸區網路骨幹）
resource "azurerm_virtual_network" "vnet" {
  name                = "${var.resource_group_name}-vnet"
  address_space       = [var.vnet_cidr]
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_subnet" "subnet_ml" {
  name                 = "snet-ml"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = [var.subnet_cidr]
  # 開啟服務端點供儲存體/Key Vault 使用
  service_endpoints = ["Microsoft.Storage", "Microsoft.KeyVault"]
}

# 儲存體供工作區使用
resource "azurerm_storage_account" "sa" {
  name                     = replace(lower("${var.hub_name}sa"), "-", "")
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"
}

# Log Analytics + Application Insights
resource "azurerm_log_analytics_workspace" "law" {
  name                = "${var.hub_name}-law"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
}

resource "azurerm_application_insights" "ai" {
  name                = "${var.hub_name}-ai"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
  workspace_id        = azurerm_log_analytics_workspace.law.id
  application_type    = "web"
}

# Key Vault
resource "azurerm_key_vault" "kv" {
  name                        = "${var.hub_name}-kv"
  location                    = var.location
  resource_group_name         = azurerm_resource_group.rg.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name                    = "standard"
  purge_protection_enabled    = true
  soft_delete_retention_days  = 7
  enabled_for_disk_encryption = true
  # 簡化存取策略：允許當前身分
  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    secret_permissions = ["Get", "List", "Set", "Delete", "Purge", "Recover", "Backup", "Restore"]
    key_permissions    = ["Get", "List", "Create", "Delete", "Recover", "Backup", "Restore"]
    certificate_permissions = ["Get", "List", "Create", "Delete", "Recover", "Backup", "Restore"]
  }
}

# Container Registry
resource "azurerm_container_registry" "acr" {
  name                = replace(lower("${var.hub_name}acr"), "-", "")
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  sku                 = "Standard"
  admin_enabled       = false
}

data "azurerm_client_config" "current" {}

# ==== Foundry Hub (以 AML Workspace 部署) ====
resource "azurerm_machine_learning_workspace" "hub" {
  name                    = var.hub_name
  location                = var.location
  resource_group_name     = azurerm_resource_group.rg.name
  application_insights_id = azurerm_application_insights.ai.id
  key_vault_id            = azurerm_key_vault.kv.id
  storage_account_id      = azurerm_storage_account.sa.id
  container_registry_id   = azurerm_container_registry.acr.id
  identity {
    type = "SystemAssigned"
  }

  # 啟用受控網路，符合 Landing Zone 安全需求
  managed_network {
    isolation_mode = "Disabled" # 若需完全隔離可改成 "AllowOnlyApprovedOutbound"
  }

  tags = {
    environment = "landing-zone"
    workload    = "foundry-hub"
  }
}

# 若需為 Hub 啟用私有端點，可追加下列示例 (以 Key Vault 為例)：
# resource "azurerm_private_endpoint" "pe_kv" {
#   name                = "${var.hub_name}-pe-kv"
#   location            = var.location
#   resource_group_name = azurerm_resource_group.rg.name
#   subnet_id           = azurerm_subnet.subnet_ml.id
#
#   private_service_connection {
#     name                           = "kv-connection"
#     is_manual_connection           = false
#     private_connection_resource_id = azurerm_key_vault.kv.id
#     subresource_names              = ["vault"]
#   }
# }

output "hub_endpoint" {
  description = "Foundry Hub (AML Workspace) URL"
  value       = "https://${azurerm_machine_learning_workspace.hub.name}.studio.azureml.ms"
}

output "resource_group" {
  value = azurerm_resource_group.rg.name
}