from project_module1.preprocess import load_json_files, clean_data, save_clean_data
from project_module1.eda import (
    load_clean_data,
    add_duration_category,
    avg_views_by_duration,
    count_videos_by_duration,
    top_channels_by_category,
    videos_per_year,
    views_per_year,
    views_by_year_and_duration,
    plot_videos_per_year,
    plot_views_per_year,
    plot_views_by_category,
    save_describe,
)


def main():
    # cleaning
    files = [
        "3awal.json",
        "brainrot464.json",
        "brainrot467.json",
        "brainrot531.json",
        "doomscrolling522.json",
    ]
    df = load_json_files(files)
    df_clean = clean_data(df)
    save_clean_data(df_clean)

    print(f"Total cleaned data: {len(df_clean)}")

    # eda
    print("\n[4] Loading cleaned data for EDA...")
    df = load_clean_data("data/processed/data_clean.json")

    print("\n[5] Feature engineering...")
    df = add_duration_category(df)

    # analysis
    print("\n[6] Analysis results:\n")

    print("Average views by duration:")
    print(avg_views_by_duration(df), "\n")

    print("Video count by duration:")
    print(count_videos_by_duration(df), "\n")

    print("Top channels by category:")
    print(top_channels_by_category(df), "\n")

    # save describe
    print("\n[7] Saving describe...")
    save_describe(df, "reports/describe.txt")

    # visualization
    print("\n[8] Generating plots...")

    vpy = videos_per_year(df)
    plot_videos_per_year(vpy, save_path="reports/figures/videos_per_year.png")

    vviews = views_per_year(df)
    plot_views_per_year(vviews, save_path="reports/figures/views_per_year.png")

    vcat = views_by_year_and_duration(df)
    plot_views_by_category(vcat, save_path="reports/figures/views_by_category.png")

    print("\n=== THE PROCESSES IS DONE!!! ===")


if __name__ == "__main__":
    main()
