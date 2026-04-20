from project_module1.fetch_data import build_dataset
from project_module1.save_data import save_to_json

def main():
    # fetching data
    keywords = ["mengatasi brainrot"]
    regions = ["ID"]

    all_data = []

    for kw in keywords:
        for reg in regions:
            data = build_dataset(
                query=kw,
                region_code=reg,
                max_results=500
            )
            all_data.extend(data)

    save_to_json(all_data, "data/raw/brainrot464.json")

    print(f"Fetching process is Done!\nTotal data: {len(all_data)}")


if __name__ == "__main__":
    main()