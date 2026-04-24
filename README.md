# Job Market Data Pipeline

## Overview

Built an end-to-end data pipeline that extracts real-time job market data from an external API, processes and cleans the data, and loads structured datasets into PostgreSQL for analysis.

The pipeline transforms unstructured job listings into actionable insights on salary trends, top-paying companies, and job market demand.

---

## Tech Stack

- Python
- Pandas
- Requests (API integration)
- PostgreSQL
- SQLAlchemy

---

## Pipeline Architecture

Adzuna API → Extract → Transform → Load → PostgreSQL

---

## Pipeline Steps

### Extract
- Fetches job listings from Adzuna API
- Converts JSON response into a structured DataFrame
- Handles nested API fields

### Transform
- Selects relevant features (title, company, location, category, salary)
- Cleans nested JSON structures
- Creates derived feature: `salary_avg`
- Filters invalid/missing salary data
- Prepares data for analysis

### Load
- Stores cleaned dataset into PostgreSQL (`jobs_cleaned`)
- Generates and stores aggregated insight tables

---

## Data Outputs

### jobs_cleaned
- title, company, location, category, salary_avg, created

### salary_by_location
- Average salary by location

### top_companies
- Highest-paying companies

### jobs_by_category
- Job demand distribution

---

## Key Insights

- Identifies top-paying locations for data roles
- Highlights companies offering highest salaries
- Reveals demand distribution across job categories

---

## How to Run

1. Clone the repository
```bash
git clone https://github.com/Anas127/job-market-data-pipeline.git
cd job-market-data-pipeline
