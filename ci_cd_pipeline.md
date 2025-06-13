# CI/CD Pipeline

## Overview

- All changes must pass CI checks:
    - YAML validation
    - Required files check
    - Unit tests
    - Pre-commit hooks

- Deployments handled via:
    - `.github/workflows/deploy.yml` workflow.

## Stages

1. PR created → CI pipeline runs.
2. PR merged → Deploy workflow triggers.
3. Staged rollout:
    - us-west-2 → us-east-1.

4. Post-deploy validation.

## Notes

- CI/CD workflows reviewed monthly.