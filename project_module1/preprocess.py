import pandas as pd
import json
import re
from pathlib import Path


def load_json_files(file_list, base_path="data/raw"):
    all_data = []

    for f in file_list:
        filepath = Path(base_path) / f
        with open(filepath, "r", encoding="utf-8") as file:
            all_data.extend(json.load(file))

    return pd.DataFrame(all_data)


def clean_data(df):
    # drop duplicate
    df = df.drop_duplicates(subset="videoId")

    # type conversion
    df["views"] = df["views"].astype(int)
    df["likes"] = df["likes"].astype(int)
    df["comments"] = df["comments"].astype(int)

    # duration convert
    def iso8601_to_seconds(duration):
        match = re.match(r"PT((\d+)H)?((\d+)M)?((\d+)S)?", duration)

        hours = int(match.group(2)) if match.group(2) else 0
        minutes = int(match.group(4)) if match.group(4) else 0
        seconds = int(match.group(6)) if match.group(6) else 0

        return hours * 3600 + minutes * 60 + seconds

    df["duration_sec"] = df["duration"].apply(iso8601_to_seconds)

    # date format
    df["publishedAt"] = pd.to_datetime(df["publishedAt"]).dt.date.astype(str)

    # filtering
    keywords = ["roblox", "#roblox", "anomali", "minecraft", "gaming"]
    pattern = "|".join(keywords)

    mask = df["title"].str.contains(pattern, case=False, na=False)

    df = df[~mask]

    # select columns
    df = df[["title", "channel", "views", "duration_sec", "publishedAt", "likes", "comments"]]

    return df


def save_clean_data(df, filename="data/processed/data_clean.json"):
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, indent=4)

    print(f"Saved to {filepath}")
