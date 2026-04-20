import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# load data
def load_clean_data(path="data/processed/data_clean.json"):
    return pd.read_json(path)


# feature engineering
def categorize_duration(x):
    if x < 60:
        return "Category 1"
    elif x < 300:
        return "Category 2"
    elif x < 600:
        return "Category 3"
    else:
        return "Category 4"


def add_duration_category(df):
    df["duration_category"] = df["duration_sec"].apply(categorize_duration)
    return df


# analysis
def avg_views_by_duration(df):
    return df.groupby("duration_category")["views"].mean()


def count_videos_by_duration(df):
    return df.groupby("duration_category").size()


def top_channels_by_category(df):
    channel_per_category = (
        df.groupby(["duration_category", "channel"])["views"]
        .sum()
        .reset_index()
    )

    top_channel = (
        channel_per_category
        .sort_values(["duration_category", "views"], ascending=[True, False])
        .groupby("duration_category")
        .head(5)
    )

    return top_channel


def videos_per_year(df):
    df["publishedAt"] = pd.to_datetime(df["publishedAt"])
    df["year"] = df["publishedAt"].dt.year
    return df.groupby("year").size()


def views_per_year(df):
    df["publishedAt"] = pd.to_datetime(df["publishedAt"])
    df["year"] = df["publishedAt"].dt.year
    return df.groupby("year")["views"].sum()


def views_by_year_and_duration(df):
    df["publishedAt"] = pd.to_datetime(df["publishedAt"])
    df["year"] = df["publishedAt"].dt.year

    return df.groupby(["year", "duration_category"])["views"].sum().unstack()


# visualitation
def plot_videos_per_year(series, save_path=None):
    import matplotlib.pyplot as plt

    plt.figure()
    series.plot(marker="o")
    plt.title("Number of Videos per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Videos")

    if save_path:
        import os
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()


def plot_views_per_year(series, save_path=None):
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    plt.figure()
    series.plot(marker="o")
    plt.title("Total Views per Year")
    plt.xlabel("Year")
    plt.ylabel("Total Views")

    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f'{int(x/1e6)}M')
    )

    if save_path:
        import os
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()   


def plot_views_by_category(df, save_path=None):
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    plt.figure()
    df.plot(marker="o")
    plt.title("Total Views by Duration Category per Year")
    plt.xlabel("Year")
    plt.ylabel("Total Views")

    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f'{int(x/1e6)}M')
    )

    if save_path:
        import os
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()

def save_describe(df, path="reports/describe.txt"):
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)

    desc = df.describe()

    with open(path, "w", encoding="utf-8") as f:
        f.write(desc.to_string())

    print(f"Describe saved to {path}")