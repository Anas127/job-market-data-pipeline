import logging
from extract import *
from transform import *
from load import *

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        logging.info("Starting pipeline...")

        df = extract()
        df, jobs_per_category, avg_salary_per_company, avg_salary_per_location = transform(
            df)
        load(df, jobs_per_category, avg_salary_per_company, avg_salary_per_location)

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
