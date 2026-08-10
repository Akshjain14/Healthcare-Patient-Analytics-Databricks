# Healthcare Patient Analytics Data Pipeline

 Overview

This project implements a scalable healthcare data engineering pipeline using the Medallion Architecture in Databricks.

The pipeline transforms raw healthcare patient data into cleaned, validated, and business-ready datasets for analytical use cases.

The project follows three processing layers:

Raw Healthcare Data → Bronze → Silver → Gold → Dashboard

The pipeline was implemented using PySpark, Spark SQL, Databricks, and Delta Lake.

 Project Architecture


                    Raw Healthcare CSV
                           |
                           v
                Databricks Volume
                healthcare_raw
                           |
                           v
                  +----------------+
                  | Bronze Layer   |
                  | Raw Data       |
                  +----------------+
                           |
                           v
                  +----------------+
                  | Silver Layer   |
                  | Cleaning &     |
                  | Transformation |
                  +----------------+
                           |
                           v
                  +----------------+
                  | Gold Layer     |
                  | Aggregation &  |
                  | Analytics      |
                  +----------------+
                           |
                           v
                  +----------------+
                  | Databricks     |
                  | AI/BI Dashboard|
                  +----------------+


Technologies Used
Python
PySpark
Spark SQL
Databricks
Delta Lake
Unity Catalog
Databricks AI/BI Dashboards
GitHub
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Dataset
The project uses a healthcare patient dataset containing information such as:

Patient Name
Age
Gender
Blood Type
Medical Condition
Date of Admission
Doctor
Hospital
Insurance Provider
Billing Amount
Room Number
Admission Type
Discharge Date
Medication
Test Results

The raw CSV file is stored in a Databricks Unity Catalog managed volume.

The raw dataset is not included in this repository.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Medallion Architecture
1. Bronze Layer

The Bronze layer stores the raw healthcare data in Delta format while preserving the original source structure.

Input
patients_records.csv
Databricks Volume
/Volumes/workspace/default/healthcare_raw/patients_records.csv
Bronze Table
workspace.default.bronze_patients
Bronze Processing
Read CSV using PySpark
Preserved the original data
Stored the data as a Delta table
Used Delta column mapping to support source column names containing spaces

The Bronze layer contains:
55,500 records
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Silver Layer

The Silver layer performs data cleaning, validation, and transformation on the Bronze data.

Silver Table
workspace.default.silver_patients
Transformations Performed
Duplicate Removal

The Bronze dataset contained:

55,500 total records
54,966 distinct records

Therefore:

534 duplicate records

were identified and removed.

Name Standardization

Patient names with inconsistent capitalization were standardized using PySpark initcap().

Example:

DaNnY sMiTh

became:

Danny Smith
Data Type Conversion

The following columns were converted to appropriate data types:

Column	Data Type
Age	Integer
Billing Amount	Double
Room Number	Integer
Date of Admission	Date
Discharge Date	Date
Null Validation

The dataset was checked for null values.

Result:

Null values = 0
Billing Validation

Negative billing amounts were identified as invalid records.

Negative billing records = 106

These records were removed from the Silver dataset.

Age Validation

Age values were checked for invalid ranges.

Validation rule:

Age <= 0 OR Age > 120

Result:

Invalid age records = 0
Date Validation

Admission and discharge dates were checked to ensure that the discharge date was not earlier than the admission date.

Result:

Invalid date records = 0
Final Silver Dataset

After cleaning and validation:
54,860 records
were stored in:
workspace.default.silver_patients
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3. Gold Layer
The Gold layer contains business-ready aggregated datasets for analytics and reporting.

Gold Table 1 — Condition Summary
workspace.default.gold_condition_summary

Contains:

Medical Condition
Total Patients
Average Age
Average Billing
Total Billing

This table supports analysis of patient distribution and billing by medical condition.

Gold Table 2 — Hospital Summary
workspace.default.gold_hospital_summary

Contains:

Hospital
Total Patients
Average Age
Average Billing
Total Billing

This table supports hospital-level patient and billing analysis.

Gold Table 3 — Insurance Summary
workspace.default.gold_insurance_summary

Contains:

Insurance Provider
Total Patients
Average Age
Average Billing
Total Billing

This table supports analysis of patient distribution and billing across insurance providers.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Dashboard
A Databricks AI/BI Dashboard was created using the Gold datasets.

Dashboard Name
Healthcare Patient Analytics Dashboard

The dashboard contains KPI cards and analytical visualizations including:
KPIs
Total Patients
Total Billing
Average Billing
Average Patient Age
Visualizations
Patients by Medical Condition
Patients by Insurance Provider
Total Billing by Medical Condition
Average Billing by Medical Condition
Top 10 Hospitals by Patient Count
Average Patient Age by Medical Condition

The dashboard provides a business-friendly view of the processed healthcare data.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Project Workflow:
Healthcare CSV
      |
      v
Databricks Unity Catalog Volume
      |
      v
+----------------------+
| Bronze Layer         |
| Raw Delta Table      |
| 55,500 records       |
+----------------------+
      |
      v
+----------------------+
| Silver Layer         |
| Cleaning & Validation|
| 54,860 records       |
+----------------------+
      |
      v
+----------------------+
| Gold Layer           |
| Business Aggregation |
+----------------------+
      |
      v
+----------------------+
| AI/BI Dashboard      |
| Analytics & Insights |
+----------------------+
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Repository Structure
Healthcare-Patient-Analytics-Databricks/
│
├── notebooks/
│   ├── 01_Bronze_Ingestion.py
│   ├── 02_Silver_Transformation.py
│   └── 03_Gold_Aggregation.py
│
├── dashboard/
│   └── dashboard-screenshot.png
│
├── docs/
│   └── architecture.png
│
└── README.md
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Key Data Quality Results
Metric	Result
Raw Records	55,500
Duplicate Records Removed	534
Negative Billing Records Removed	106
Invalid Age Records	0
Invalid Date Records	0
Null Values	0
Final Silver Records	54,860
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Future Enhancements
The current pipeline uses batch processing.

Possible future enhancements include:
Real-time data ingestion using Apache Kafka
Automated pipeline orchestration
Delta Live Tables / Lakeflow-based pipeline automation
Advanced healthcare analytics
Predictive analytics and machine learning
Power BI or Tableau integration
Additional data-quality rules
Incremental processing
Slowly Changing Dimension (SCD) Type 2 implementation for historical dimension tracking
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Conclusion
This project demonstrates an end-to-end healthcare data engineering workflow using Databricks and the Medallion Architecture.
Raw healthcare data is ingested into the Bronze layer, cleaned and validated in the Silver layer, transformed into business-ready aggregations in the Gold layer, and finally presented through an interactive Databricks AI/BI Dashboard.
The project demonstrates practical use of PySpark, Spark SQL, Delta Lake, Unity Catalog, and analytical data modeling.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author
Aksh Jain
B.Tech Computer Science and Engineering
