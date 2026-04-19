# -*- coding: utf-8 -*-


# merge dataset
import pandas as pd
import json

files = [
    "3awal.json",
    "brainrot464.json",
    "brainrot467.json",
    "brainrot531.json",
    "doomscrolling522.json"
]

all_data = []

import json
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        all_data.extend(json.load(file))

df = pd.DataFrame(all_data)

print(len(df))

# drop duplicate
df = df.drop_duplicates(subset = "videoId")
df

# checking missing value

df.isnull().sum()

# make sure the data type were correct

df["views"] = df["views"].astype(int)
df["likes"] = df["likes"].astype(int)
df["comments"] = df["comments"].astype(int)

# change duration format

import re

def iso8601_to_seconds(duration):
    match = re.match(r'PT((\d+)H)?((\d+)M)?((\d+)S)?', duration)

    hours = int(match.group(2)) if match.group(2) else 0
    minutes = int(match.group(4)) if match.group(4) else 0
    seconds = int(match.group(6)) if match.group(6) else 0

    return hours * 3600 + minutes * 60 + seconds

df["duration_sec"] = df["duration"].apply(iso8601_to_seconds)

df["publishedAt"] = pd.to_datetime(df["publishedAt"])
df['publishedAt'] = df['publishedAt'].dt.date.apply(lambda x: x.isoformat())

"""Deleting video where the title not match with the aim of the project"""

# setting the unmatch keywords
keywords = [
    "roblox",
    "#roblox",
    "anomali",
    "minecraft",
    "gaming"
]

# making pattern from the keyword
pattern = "|".join(keywords)

# making mask (matching the title which containing keywords that we already set before)
mask = df["title"].str.contains(pattern, case=False, na=False)

print("Total data:", len(df))
print("Data yang mengandung keyword:", mask.sum())

df_check = df[mask][["title", "views", "region"]]

print("\n=== SAMPLE DATA YANG AKAN DIHAPUS ===")
print(df_check.head(20))

"""We decide to keeping some rows because we did include gaming in the keyword. we know this keyword is 'grey' category. so, after we check the value, there are some rows that we don't want to delete (we want it still exist in our data) so that's why in the next code, we adding keep_index for video that we don't want it to be deleted"""

keep_index = [583, 827,1801,1889]
final_mask = mask & (~df.index.isin(keep_index))
df_clean = df[~final_mask]
print("Total data setelah dihapus:", len(df_clean))

df_clean

# taking variables that will be used in analysis

df_clean = df_clean[['title','channel','views','duration_sec','publishedAt','likes','comments']]
df_clean

import json

file_path = "data_clean.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(df_clean.to_dict(orient="records"), f, indent=4)

print("Saved", file_path)

