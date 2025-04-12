import pandas as pd
import os
from app.utils.rules_loader import load_rules

def generate_report(input_path="data/input/input.csv", ref_path="data/reference/reference.csv", output_path="data/output/output.csv"):
    # Load files
    input_df = pd.read_csv(input_path)
    ref_df = pd.read_csv(ref_path)

    # Merge on refkey1 and refkey2
    merged_df = pd.merge(input_df, ref_df, on=["refkey1", "refkey2"], how="left")

    # Load transformation rules
    rules = load_rules()
    result_df = pd.DataFrame()

    # Apply each rule
    for outfield, expression in rules.items():
        try:
            # Replace textual rule with real pandas expression
            expr = expression
            expr = expr.replace("max(", "max_")  # temp handle for max()
            expr = expr.replace("+", " + ")
            expr = expr.replace("*", " * ")
            expr = expr.replace("max_", "max(")

            result_df[outfield] = merged_df.eval(expr)
        except Exception as e:
            print(f"Failed to apply rule for {outfield}: {expression}. Error: {e}")
            result_df[outfield] = None

    # Save result
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    result_df.to_csv(output_path, index=False)

    return output_path
