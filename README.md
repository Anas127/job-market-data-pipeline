# Job Market Data Pipeline

## Overview

This project is a data engineering pipeline that extracts real-time job market data from an external API, processes and cleans the data using Python and Pandas, and stores both raw and aggregated insights in a PostgreSQL database.

The goal is to transform unstructured job listing data into structured, queryable datasets that provide insights into salary trends, company compensation, and job market demand.

---

## Tech Stack

- Python
- Pandas
- Requests (API integration)
- PostgreSQL
- SQLAlchemy

---

## Pipeline Architecture

API (Adzuna) → Extract → Transform → Load → PostgreSQL

---

## Pipeline Steps

### 1. Extract

- Fetches job listings using the Adzuna API
- Converts JSON response into a Pandas DataFrame
- Handles nested API structures

### 2. Transform

- Selects relevant fields (title, company, location, salary, category)
- Cleans nested JSON fields (company, location, category)
- Creates new feature: `salary_avg`
- Removes invalid or missing salary data
- Sorts data for analysis

### 3. Load

- Stores cleaned dataset into PostgreSQL (`jobs_cleaned`)
- Stores aggregated insights into separate tables

---

## Data Outputs

### jobs_cleaned

Cleaned job-level dataset:

- title
- company
- location
- category
- salary_avg
- created

### salary_by_location

Average salary by location:

- location
- salary_avg

### top_companies

Top companies by average salary:

- company
- salary_avg

### jobs_by_category

Job demand by category:

- category
- job_count

---

## Key Insights

- Identifies highest-paying locations for data engineering roles
- Highlights companies offering top compensation
- Shows demand distribution across job categories

---

## How to Run

### 1. Clone the repository

```bash
git clone <https://github.com/Anas127/job-market-data-pipeline.git>
cd job-market-data-pipeline
```
