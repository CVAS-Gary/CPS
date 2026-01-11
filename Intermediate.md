### CLI增加Microsoft Learn MCP Server
/mcp add https://learn.mcp.microsoft.com/
已配置的 MCP 服务器信息保存在 mcp-config.json，默认位置是 ~/.copilot（可通过设置 XDG_CONFIG_HOME 改变位置）。

### 三輪迭代
"""
第一輪迭代要求：
    撰寫一個純函式：
    寫一個函式，接收整數陣列並回傳排序後的去重結果
第二輪迭代要求：
- 名稱：deduplicate_and_sort
- 輸入：list of int
- 輸出：排序後去重的 list of int
- 若輸入含非整數，拋出 ValueError("Invalid input")
- 加入清楚的 docstring（說明參數與回傳）
- 通過 flake8/black 格式檢查
- 通過 pytest 測試（test_dedup.py）
第三輪迭代要求：
強化版本要求：
- 使用明確的輸入驗證（僅允許 int）
- 對 None/空值顯式處理
- 保持循環複雜度低（不做過度巢狀）
- cyclomatic complexity < 5
- 文件字串（docstring）完整描述例外情況

"""

### 建立測試環境
python -m venv .venv

.venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install pytest black flake8

black --check .
flake8 .
pytest -q

### 初始化專案環境
在 .github/workflows/*.yml 中加入以下內容：
# Prompt: Initialize Project from CPS Template

此 GitHub Actions workflow 會在 `main` 分支 push 或手動觸發時執行，目的是將 CPS 樣板專案內容初始化到目前的 repository。  
主要步驟如下：

1. **Checkout 專案原始碼**：取得目前 repository 的最新內容。
2. **拉取 CPS 樣板**：從 `https://github.com/CVAS-Gary/CPS.git` 複製 CPS 樣板專案。
3. **複製樣板檔案**：將 `PromptGallery`、`CONTRIBUTING.md` 及 PR 樣板複製到本專案。
4. **提交變更**：自動 commit 並 push 樣板檔案到 repository。

此流程可協助專案快速套用標準化的 CPS 樣板結構，確保專案初始內容一致，並方便後續協作與管理。

### 建立新專案參考
請幫我依照init-template.yml完整執行在demo資料夾下建立新專案CPS，並將template repo中的範例檔案複製到我的新專案。
請幫我參照CPS專案自動複製".github\所有資料夾和檔案"、"PromptGallery\所有資料夾和檔案"、"CONTRIBUTING.md"、"README.md"、"requirements.txt"到demo資料夾下建立的新專案CPS。

設定參考instructionsFilesLocations:
@id:chat.instructionsFilesLocations 

    """
    接收 JSON 格式的整數列表，回傳排序後去重的結果。
    輸入格式：
        { "input_list": [整數, ...] }
    回傳格式：
        { "result": [整數, ...] }
    例外：
        若輸入格式錯誤，回傳 400 並附錯誤訊息。
    """