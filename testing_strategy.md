# Testing Strategy

## Levels of Testing

| Level                | Tools / Methods |
|----------------------|-----------------|
| Unit Tests           | pytest          |
| Config Validation    | YAML schema, CI scripts |
| Integration Tests    | Staging pipeline runs |
| End-to-End Monitoring| Live dashboards + alerts |

## Test Coverage Goals

- Unit test coverage → 85%+ for critical pipeline code.
- CI validation must pass for all PRs.

## Notes

- Tests must run in CI pipeline.
- Tests reviewed quarterly.