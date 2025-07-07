from parser import parse_legacy_data

if __name__ == "__main__":
    data_file = "../data/legacy_sample_data.txt"
    df = parse_legacy_data(data_file)
    print(df)
