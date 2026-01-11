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