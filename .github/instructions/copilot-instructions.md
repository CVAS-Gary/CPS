# Copilot Instructions for Python Development

## 1. 環境準備
- **Python 版本**：請使用 Python 3.10 或以上版本
- **虛擬環境**：請使用 `venv` 或 `conda` 建立隔離環境
- **安裝套件**：請使用 `pip install -r requirements.txt` 安裝相依套件

## 2. 註解與字串
- **繁體中文註解**：所有註解與字串內容請一律使用繁體中文
- **固定註解**：每份產生的程式碼最上方，請加上註解：由 GitHub Copilot 產生

## 3. 變數命名
- **變數命名規則**：所有變數請使用全大寫，並以底線分隔單字，例如：`MY_VARIABLE_NAME`

## 4. 虛擬環境啟用指令
- **Windows (PowerShell)**：`.venv\Scripts\Activate.ps1`
- **macOS/Linux**：`source .venv/bin/activate`

## 5. 測試框架
- **使用 pytest**：請使用 `pytest` 作為主要測試框架
- **測試檔案命名**：測試檔案請以 `test_` 開頭，例如：`test_my_module.py`

## 6. 程式碼風格
- **格式化工具**：請使用 `black` 進行程式碼格式化
- **靜態檢查工具**：請使用 `flake8` 進行靜態程式碼檢查