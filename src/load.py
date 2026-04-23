from sqlalchemy import create_engine


def load(df, jobs_per_category, avg_salary_per_company, avg_salary_per_location):
    engine = create_engine(
        'postgresql://postgres:123@localhost:5432/data_pipeline_db')

    df.to_sql("jobs_cleaned", engine, if_exists="replace", index=False)
    jobs_per_category.to_sql("jobs_per_category", engine,
                             if_exists="replace", index=False)
    avg_salary_per_location.to_sql(
        "avg_salary_per_location", engine, if_exists="replace", index=False)
    avg_salary_per_company.to_sql(
        "avg_salary_per_company", engine, if_exists="replace", index=False)
