def transform(df):

    df = df[["title", "salary_min", "salary_max",
             "location", "company", "category", "created"]]

    df["company"] = df["company"].apply(
        lambda x: x["display_name"] if isinstance(x, dict) else None)

    df["location"] = df["location"].apply(
        lambda x: x["display_name"] if isinstance(x, dict) else None)

    df["category"] = df["category"].apply(
        lambda x: x["label"] if isinstance(x, dict) else None)

    df["salary_avg"] = (df["salary_min"] + df["salary_max"]) / 2

    df = df.dropna(subset=["salary_avg"])

    df = df.sort_values(by="salary_avg", ascending=False)

    avg_salary_per_location = df.groupby(
        "location")["salary_avg"].mean().reset_index()
    avg_salary_per_location = avg_salary_per_location.sort_values(
        by="salary_avg", ascending=False)

    avg_salary_per_company = df.groupby(
        "company")["salary_avg"].mean().reset_index()
    avg_salary_per_company = avg_salary_per_company.sort_values(
        by="salary_avg", ascending=False)
    avg_salary_per_company = avg_salary_per_company.head(5)

    jobs_per_category = df.groupby("category")["title"].count().reset_index()


    jobs_per_category = jobs_per_category.rename(columns={"title": "job_count"})
    jobs_per_category = jobs_per_category.sort_values(
        by="job_count", ascending=False)
    jobs_per_category = jobs_per_category.head(5)

    return df, jobs_per_category, avg_salary_per_company, avg_salary_per_location
