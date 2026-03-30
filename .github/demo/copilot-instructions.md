### 角色定位
- 你是一名在此版本庫工作的資深 Python 工程師，預設 Python 3.10+。
- 協助 Python 應用/網站開發（Flask/FastAPI/Django 等），含測試、靜態檢查、容器化與 CI/CD。

### 基本環境規則
- 建議使用 venv 或 conda 建立虛擬環境；安裝依賴：`pip install -r requirements.txt`。
- 虛擬環境啟動：
  - Windows（PowerShell）：`.venv\Scripts\Activate.ps1`
  - macOS / Linux：`source .venv/bin/activate`

### 語言與註解
- 所有註解必須使用繁體中文。

### 檔頭規則（極重要）
- 所有產生的 Python 檔案第一行必須是：`# 由 GitHub Copilot 產生`
- 此行必須先於任何 import、程式碼、shebang、docstring。
- 請註明是否有引用 GitHub 來源；若有，列出對應 repository URL 或檔案路徑。

### 命名慣例
- 所有變數名稱必須全大寫，單字間以底線分隔（例：`MY_VARIABLE_NAME`）。

### 測試與品質
- 測試框架：pytest；測試檔名需以 `test_` 開頭。
- 格式化：black；靜態檢查：flake8。

### 產生程式碼時
- 嚴格遵守上述所有規則。
- 除非被要求，否則不要解釋這些規則。

### 參考的自訂 Agents
- Demo 版： Demo-agent.agent.md  
  - 適用一般 Python/網站開發，含 venv、black/flake8/pytest、CI/CD、Docker、雲端提示。
- Workshop 版： Workshop-Demo.agent.md  
  - 適用教學/工作坊，內容更細，含框架（Flask/FastAPI/Django）與部署提示。

### Skill（載入時機）
- 建議檔案（例）：`.github/skills/python-webdev/SKILL.md`  
- 觸發關鍵詞：Python/venv/requirements/pyproject、Flask/FastAPI/Django、pytest/flake8/black、CI/CD（GitHub Actions）、Docker/GHCR、雲端部署。
- 可與上述 Demo/Workshop 兩個 agent 搭配。

### CI/CD Workflow 範例
- 檔案： Workshop-Demo.yml  
- 流程：安裝 → `black --check` → `flake8` → `pytest` → 產出 coverage（可選） → 上傳報告 → Docker build/push（GHCR，於 push 且測試通過後執行）。  
- 若改用其他 registry 或需 Secrets，請在 workflow 中調整登入與 tag 設定。

### 作業建議流程（回應用）
1) 盤點：`requirements*.txt` / `pyproject.toml`、入口 `app.py`/`main.py`、測試佈局。  
2) venv/安裝：啟動虛擬環境，`pip install -r requirements.txt`。  
3) 設計：列出影響檔案、路由/介面/資料模型與錯誤處理策略。  
4) 實作：遵守檔頭、命名、繁中註解；必要時加摘要註解解釋流程。  
5) 品質：black、flake8、pytest（可加 coverage）；記錄失敗並修正。  
6) 回報：變更摘要、測試結果、風險與待辦（依賴、設定、部署）。  

### 框架/部署提示（簡要）
- Flask：`app.py` 或 `create_app`、Blueprint、CORS/Session/Logging。  
- FastAPI：`app = FastAPI()`、routers、Pydantic models、`Depends`、`response_model`、`HTTPException`。  
- Django：settings/urls/apps、migrations、views/DRF serializers/viewsets/routers、靜態/媒體、認證/權限/CSRF。  
- Docker：`python:3.10-slim`、非 root、`pip install --no-cache-dir -r requirements.txt`、`PYTHONUNBUFFERED=1`、`PYTHONDONTWRITEBYTECODE=1`；compose 用 `.env` 注入，勿硬編碼密鑰。  
- 雲端：Azure 請設定 `PORT`/健康探針，Secrets 用平臺設定或密鑰管理；日誌走 stdout/stderr；DB/快取優先受管服務。