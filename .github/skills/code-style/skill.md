---
name: company-coding-style
description: Apply the company internal coding style, naming conventions, and best practices when writing, modifying, or reviewing code.
---

# Company Internal Coding Style Skill

This skill defines the mandatory coding style and conventions used inside the company.

## When to use this skill

Use this skill automatically when the user:
- writes new code
- modifies existing code
- asks for refactoring suggestions
- requests code review or pull request review
- asks whether code follows company standards

## General rules

Always prioritize company coding rules over personal preference or common open-source styles.

If there is a conflict between common best practices and company rules, follow company rules.

## Coding conventions

When generating or reviewing code, enforce the following:

1. **Naming**
   - Use clear, descriptive variable and function names
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
   - Keep formatting consistent within the file
   - Follow existing project formatting before introducing new styles

## Code review behavior

When reviewing code:
- Point out violations of company coding standards
- Suggest concrete improvements with examples
- Be concise and professional
- Do not rewrite large sections unless necessary

## Output expectations

When responding:
- Clearly state whether the code complies with company coding style
- List issues in bullet points if any exist
- Provide corrected examples when appropriate
