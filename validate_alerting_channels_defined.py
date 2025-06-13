import yaml

def main():
    print("Validating...")

    def test_alerting_channels_defined():
    with open("InfraPipelineFeatureFlags.yml") as f:
        config = yaml.safe_load(f)
    assert "alerting" in config
    for channel in config["alerting"].get("channels", []):
        assert "slack" in channel or "pagerduty" in channel

    print("Validation completed.")

if __name__ == "__main__":
    main()