---
name: python-coding-style
description: Apply Python coding style, naming conventions, and best practices when writing, modifying, or reviewing Python code.
---

# Python Coding Style Skill
This skill defines the mandatory coding style and conventions for Python code.

## When to use this skill
Use this skill automatically when the user:
- writes new Python code
- modifies existing Python code
- asks for refactoring suggestions for Python code
- requests code review or pull request review for Python code
- asks whether Python code follows company standards
## General rules
Always prioritize company coding rules over personal preference or common open-source styles.
If there is a conflict between common best practices and company rules, follow company rules.
## Coding conventions
When generating or reviewing Python code, enforce the following:
1. **Naming**
   - Use snake_case for variable and function names
   - Use PascalCase for class names
   - Avoid abbreviations unless they are company-approved
   - Keep naming consistent across the file and project
2. **Code structure**
   - Functions should be small and single-purpose
   - Avoid deep nesting when possible
   - Prefer explicit logic over clever tricks
3. **Comments**
   - Add comments only when the intent is not obvious
   - Comments must explain *why*, not *what*
   - Avoid redundant or obvious comments
4. **Error handling**
   - Do not silently ignore errors
   - Errors should include meaningful messages
   - Prefer explicit error handling over generic catch-all logic
5. **Formatting**
   - Follow PEP 8 style guide for Python code
   - Use 4 spaces for indentation
   - Limit lines to 79 characters
   - Use blank lines to separate functions and classes

## Security review rules
When generating or reviewing Python code, also check for security issues:

1. **SQL Injection**
   - Never construct SQL statements using string concatenation,
     f-strings, or `%` formatting with user input.
   - Always use parameterized queries.

2. **Command Injection**
   - Do not pass unsanitized user input to subprocess or os.system.

3. **Hardcoded secrets**
   - Do not hardcode passwords, API keys, or tokens.

4. **Input validation**
   - Validate and sanitize all user-controlled input.

5. **Sensitive data exposure**
   - Avoid logging passwords or confidential information.

6. **Authentication**
   - Never store passwords in plaintext.
   - Use secure password hashing such as bcrypt.

7. **Dependency security**
   - Prefer maintained libraries and avoid deprecated packages.

## Code review behavior
When reviewing Python code:
- Point out violations of company coding standards
- Suggest concrete improvements with examples
- Be concise and professional
- Do not rewrite large sections unless necessary
## Output expectations
When responding:
- Clearly state whether the Python code complies with company coding style
- List issues in bullet points if any exist
- Provide corrected examples when appropriate