# 由 GitHub Copilot 產生
# 本檔案未參考任何 GitHub 原始碼

import pytest
from src.workflow import Workflow
from src.steps import step_hello, step_goodbye

def test_workflow_run(capsys):
    WF = Workflow()
    WF.add_step(step_hello)
    WF.add_step(step_goodbye)
    WF.run()
    OUT, _ = capsys.readouterr()
    assert "Hello World" in OUT
    assert "Goodbye" in OUT
