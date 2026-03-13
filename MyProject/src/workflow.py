# 由 GitHub Copilot 產生
# 本檔案未參考任何 GitHub 原始碼

# Workflow 主流程類別（基礎可運作版本）
class Workflow:
    def __init__(self):
        # 儲存所有步驟
        self.STEPS = []

    def add_step(self, step_func):
        # 新增一個步驟（step_func 必須為可呼叫物件）
        self.STEPS.append(step_func)

    def run(self):
        # 順序執行所有步驟
        for STEP in self.STEPS:
            STEP()
