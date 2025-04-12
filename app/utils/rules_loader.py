import yaml

def load_rules(filepath: str = "config/transformation_rules.yaml") -> dict:
    with open(filepath, "r") as f:
        data = yaml.safe_load(f)
    return data.get("rules", {})
