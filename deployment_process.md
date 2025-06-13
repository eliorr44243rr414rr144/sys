# Deployment Process

Infra Ops Event Pipeline deployments follow standard CI/CD workflows.

## Deployment Steps

1. Code merged to `main` branch.
2. CI validation passes (tests, configs, YAML schema).
3. GitHub Actions deploy workflow triggers.
4. Canary rollout to `us-west-2`.
5. Full rollout to `us-east-1`.

## Rollback Procedure

- Rollback via GitHub Actions workflow.
- Latest verified stable release tagged as `stable-prod`.
- Rollbacks audited in deployment logs.