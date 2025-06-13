# Contributing to Infra Event Pipeline

## Overview

This is an internal Roblox project maintained by the **Infra Platform** team.

External contributions are not accepted.

## Process

1. Create a feature branch off `main`.
2. Validate config changes using `make validate-config`.
3. Run tests using `make run-tests`.
4. Ensure pre-commit passes:
    ```bash
    pre-commit run --all-files
    ```
5. Submit PR with appropriate reviewers from `CODEOWNERS`.

## PR Review Guidelines

- At least 1 approval from Infra Platform team.
- For changes to `InfraAuditPolicy.xml`, legal-ops must review.
- For major changes, notify `#infra-platform` Slack.

## Internal Links

- [Jira board](https://jira.roblox.com/projects/INFRA)
- [Infra Pipeline Dashboard](https://metrics.rbx.com/d/infra_pipeline/infra-pipeline-prod)

For questions → infra-platform@roblox.com