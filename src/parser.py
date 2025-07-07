import pandas as pd

def parse_legacy_data(file_path):
    # Define fixed-width fields
    colspecs = [(0, 5), (5, 20), (20, 26)]
    column_names = ["ID", "Name", "Balance"]

    df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)
    df["Balance"] = df["Balance"].astype(float) / 100  # Convert cents to dollars
    return df
