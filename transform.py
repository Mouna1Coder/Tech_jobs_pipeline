import json
import pandas as pd

def clean_job_data():
    with open("data/raw_jobs.json", "r") as f:
        jobs = json.load(f)

    df = pd.json_normalize(jobs)
    df = df[["company", "position", "location", "tags", "url"]]
    df["tags"] = df["tags"].apply(lambda tags: ", ".join(tags))

    df.to_csv("data/clean_jobs.csv", index=False)

    print("Cleaned data saved to data/clean_jobs.csv")

if __name__ == "__main__":
    clean_job_data()
