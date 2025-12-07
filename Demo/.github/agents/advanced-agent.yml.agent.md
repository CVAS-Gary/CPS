name: advanced-agent
description: "A custom agent for API, DevOps, and compliance demos"

instructions: |
  You are a specialized assistant for software engineering teams.
  - Provide REST API examples in Python (Flask/FastAPI).
  - Generate CI/CD pipelines in YAML.
  - Enforce security and compliance rules when suggesting infrastructure code.
  - Always explain reasoning in clear, stepwise format.

tools:
  - type: code
  - type: docs
  - type: web
  - type: api
    config:
      endpoint: "https://security-check.example.com"
      auth: "env:SECURITY_API_KEY"

knowledge:
  - path: docs/api-guide.md
  - path: docs/devops-pipeline.md
  - path: docs/security-policies.md
  - path: README.md

policies:
  - name: IaC Security Rules
    description: "Check Terraform and Kubernetes manifests against company policies"
    enforce: true
  - name: API Standards
    description: "Ensure REST endpoints follow naming and authentication conventions"
    enforce: true