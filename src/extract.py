import requests
import pandas as pd
import os


from dotenv import load_dotenv
load_dotenv()


def extract():
    url = "https://api.adzuna.com/v1/api/jobs/us/search/1"

    params = {
        "app_id": os.getenv("ADZUNA_APP_ID"),
        "app_key": os.getenv("ADZUNA_APP_KEY"),
        "results_per_page": 20,
        "what": "data engineer"
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = data["results"]

    df = pd.DataFrame(jobs)

    return df
