---
name: python-webdev
description: "Use when: working on Python 3.10+ apps/APIs/websites with venv + black/flake8/pytest + Docker/CI/CD (GitHub Actions). Keywords: Flask, FastAPI, Django, requirements.txt, pytest, flake8, black, Docker, GHCR, coverage."
---

# Skill: Python Web Dev + CI/CD

## When to Invoke
- 使用者提及 Python/venv/requirements/pyproject、Flask/FastAPI/Django、pytest/flake8/black。
- 需要示範或套用 CI/CD（GitHub Actions）、Docker/容器、雲端部署（Azure/GCP/AWS）、GHCR 推送。
- 要求遵守：首行「# 由 GitHub Copilot 產生」、變數全大寫底線、註解繁體中文。

## Paired Agents
- Demo: `.github/agents/Demo-agent.agent.md`（示範/一般開發流程）。
- Workshop: `.github/agents/Workshop-Demo.agent.md`（教學/工作坊版，含更完整框架/部署指引）。

## CI/CD Reference
- Workflow 範例：`.github/workflows/Workshop-Demo.yml`
  - 階段：安裝 → black --check → flake8 → pytest → coverage（可選） → 上傳報告。
  - Docker build/push：Buildx + GHCR（可依需求改 registry）。

## Default Steps (Agent should follow)
1) 盤點專案：`requirements*.txt`、`pyproject.toml`、入口 (`app.py`/`main.py`)、測試佈局。  
2) venv 啟用與安裝：Windows `.venv\\Scripts\\Activate.ps1`; macOS/Linux `source .venv/bin/activate`; `pip install -r requirements.txt`。  
3) 設計變更：介面/路由/資料模型/錯誤處理一致性。  
4) 實作：首行標示、全大寫底線命名、繁中註解，必要時摘要註解說明流程。  
5) 品質檢查：black、flake8、pytest（可加 coverage）；記錄失敗與修正。  
6) 回報：變更摘要、測試結果、風險/待辦（依賴、設定、部署）。

## Framework Hints
- Flask：`app.py`/`create_app`、Blueprint、CORS/Session/Logging。  
- FastAPI：`app = FastAPI()`、routers、Pydantic models、`Depends`、`response_model`、`HTTPException`。  
- Django：settings/urls/apps、migrations、views/DRF serializers/viewsets/routers、靜態/媒體、認證/權限/CSRF。  
- 新增路由/端點：保持錯誤格式一致，補測試與驗證/schema。

## Docker/Deploy Hints
- Dockerfile：`python:3.10-slim`、非 root、`pip install --no-cache-dir -r requirements.txt`、`PYTHONUNBUFFERED=1`、`PYTHONDONTWRITEBYTECODE=1`。  
- Compose：分離 app/DB/快取；環境變數用 `.env` 注入，勿硬編碼密鑰。  
- 雲端（Azure/GCP/AWS）：PORT/健康探針設定，機密用平臺設定或密鑰服務，日誌走 stdout/stderr，DB/快取優先受管服務。

## Response Style
- 簡潔、步驟導向，先詢問環境/框架/部署目標再給方案。  
- 強調前置條件與風險（依賴、機密、部署設定），必要時提供替代方案。  
- 如新增指令或流程，提示補 README/開發筆記（繁體中文）。

## Safety/Compliance
- 不硬編碼密鑰/連線字串；優先環境變數與 `.env.example`。  
- 對外輸出前序列化與驗證；避免 N+1；留意 CORS/認證/授權與敏感資訊 log。  
- 若觸及部署：提醒檢查 registry/雲端憑證是否已配置，避免洩漏 secrets。