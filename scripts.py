from project_module1.preprocess import load_json_files, clean_data, save_clean_data

def main():
    # cleaning
    files = ["3awal.json",
    "brainrot464.json",
    "brainrot467.json",
    "brainrot531.json",
    "doomscrolling522.json"]
    df = load_json_files(files)
    df_clean = clean_data(df)
    save_clean_data(df_clean)

    print(f"Total cleaned data: {len(df_clean)}")

    # eda


if __name__ == "__main__":
    main()