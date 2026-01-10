# Prompt Gallery

這裡收錄常用的 Copilot 提示範例，方便快速複製使用。

---

## 1. 建立 Merge Request 描述
**Prompt 範例：**
請根據以下 commit 訊息，生成一份 GitLab Merge Request 描述，包含：
- 📌 修改目的
- 🔄 主要變更
- ✅ 測試情況
- 📎 相關 Issue
- 📝 Reviewer 注意事項

---

## 2. 撰寫測試案例
**Prompt 範例：**
請為以下 Python 函式生成 pytest 測試案例，要求：
- 涵蓋正常情況與錯誤情況
- 使用清楚的函式命名
- 測試必須能通過 flake8/black 格式檢查

---

## 3. 生成 CI/CD pipeline
**Prompt 範例：**
請生成一份 GitLab CI/CD pipeline (`.gitlab-ci.yml`)，需求如下：
- 使用 Python 3.11
- 包含 lint (flake8/black)、測試 (pytest)、部署三個 stage
- 測試必須在 Ubuntu runner 上執行
- 部署階段僅在 main 分支觸發