import yaml

def main():
    print("Validating...")

    def fallback_test():
    with open("InfraEventPipelineConfig.yml") as f:
        config = yaml.safe_load(f)
    assert "pipeline" in config

    print("Validation completed.")

if __name__ == "__main__":
    main()