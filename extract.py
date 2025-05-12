import requests
import json
import os


def fetch_job_data():
    url = "https://remoteok.com/api"  # Free job board API
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        jobs = response.json()[1:6]  # Skip the first metadata item, get first 5 jobs
        os.makedirs("data", exist_ok=True)
        with open("data/raw_jobs.json", "w") as f:
            json.dump(jobs, f, indent=2)
        print("Job data saved to data/raw_jobs.json")
    else:
        print("Failed to fetch job data")


if __name__ == "__main__":
    fetch_job_data()
