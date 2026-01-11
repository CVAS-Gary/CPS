# GitHub Copilot Prompt Gallery

這裡收錄常用的 Copilot 提示範例，方便快速複製使用於 GitHub 專案。
---

## 1. 撰寫功能實作提示
**Prompt 範例：**
```
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
```
---

## 2. 建立 Pull Request 描述
**Prompt 範例：**
請根據以下 commit 訊息，生成一份 GitHub Pull Request 描述，包含：
- 📌 修改目的
- 🔄 主要變更
- ✅ 測試情況
- 📎 相關 Issue (使用 `Closes #123` 格式)
- 📝 Reviewer 注意事項

---

## 3. 撰寫測試案例
**Prompt 範例：**
請為以下 Python 函式生成 pytest 測試案例，要求：
- 涵蓋正常情況與錯誤情況
- 使用清楚的函式命名
- 測試必須能通過 flake8/black 格式檢查
- 測試結果可在 GitHub Actions 中執行並通過

---

## 4. 生成 GitHub Actions CI/CD Workflow
**Prompt 範例：**
請生成一份 GitHub Actions workflow (`.github/workflows/ci.yml`)，需求如下：
- 使用 Python 3.11
- 包含 lint (flake8/black)、測試 (pytest)、部署三個 job
- 測試必須在 Ubuntu runner 上執行
- 部署階段僅在 `main` 分支觸發

### 5. 撰寫新專案部署
# 1. 複製指定檔案與資料夾
Copy-Item -Path "CPS-tmp\.github\pull_request_template.md" -Destination ".github\pull_request_template.md" -Force
Copy-Item -Path "CPS-tmp\PromptGallery" -Destination "." -Recurse -Force
Copy-Item -Path "CPS-tmp\CONTRIBUTING.md" -Destination "." -Force

# 3. 刪除暫存資料夾
Remove-Item -Recurse -Force "CPS-tmp"
