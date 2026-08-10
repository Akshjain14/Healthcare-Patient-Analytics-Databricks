# Healthcare Patient Analytics Data Pipeline

An end-to-end healthcare data engineering project built using **Databricks, PySpark, Spark SQL, and Delta Lake**.

The project follows the **Medallion Architecture**:

**Raw Data → Bronze → Silver → Gold → Dashboard**

## Tech Stack

- Python
- PySpark
- Spark SQL
- Databricks
- Delta Lake
- Unity Catalog

## Key Work

- Raw healthcare data ingestion into Bronze
- Data cleaning and validation in Silver
- Duplicate and invalid record removal
- Business-level aggregations in Gold
- Interactive Databricks AI/BI Dashboard

## Gold Tables

- `gold_condition_summary`
- `gold_hospital_summary`
- `gold_insurance_summary`

**[View Live Dashboard →](https://dbc-0cca5194-f832.cloud.databricks.com/dashboardsv3/01f194de50e21c99a54c0cbd7dcb12ec/published?o=7474652573665199)**

## Repository

```text
notebooks/
├── 01_Bronze_Ingestion.py
├── 02_Silver_Transformation.py
└── 03_Gold_Aggregation.py

dashboard/
└── healthcare-dashboard.png

Author
Aksh Jain
B.Tech Computer Science & Engineering
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
