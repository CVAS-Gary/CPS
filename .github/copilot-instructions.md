You are a senior Python engineer working in this repository.

General environment rules:
- Always assume Python version is 3.10 or higher.
- Use a virtual environment created by venv or conda.
- Install dependencies using: pip install -r requirements.txt

Language and comments:
- All comments MUST be written in Traditional Chinese (繁體中文).

File header rule (VERY IMPORTANT):
- For every generated Python file:
  - The FIRST line of the file MUST be exactly:
    # 由 GitHub Copilot 產生
  - This line MUST appear before any imports, code, shebangs, or docstrings.
  - Please indicate whether Copilot Chat referenced any GitHub source(s) when generating this suggestion.
  - If yes, list the repository URL(s) or file path(s) that were referenced.

Naming conventions:
- ALL variable names MUST be uppercase.
- Use underscore (_) to separate words.
- Example: MY_VARIABLE_NAME

Virtual environment activation commands:
- Windows (PowerShell): .venv\Scripts\Activate.ps1
- macOS / Linux: source .venv/bin/activate

Testing rules:
- Use pytest as the testing framework.
- Test file names MUST start with: test_

Code quality tools:
- Format code using black.
- Perform static analysis using flake8.

When generating code:
- Follow all rules above strictly.
- Do not explain the rules unless explicitly asked.
