# Healthcare Patient Analytics Data Pipeline

An end-to-end healthcare data engineering project built using **Databricks, PySpark, Spark SQL, Delta Lake, and Unity Catalog**. The pipeline follows the **Medallion Architecture** to transform raw healthcare data into clean, validated, business-ready datasets and interactive analytics.

---

## Project Overview

The project processes healthcare patient records through three data layers:

**Raw Data → Bronze → Silver → Gold → Dashboard**

The pipeline demonstrates practical data engineering concepts including:

- Data ingestion using PySpark
- Delta Lake tables
- Data cleaning and validation
- Duplicate removal
- Data type standardization
- Data quality checks
- Business-level aggregations
- Databricks AI/BI Dashboard

---

## Architecture


                    Healthcare CSV
                          |
                          v
               Databricks Unity Catalog
                    Managed Volume
                          |
                          v
                +-------------------+
                |   Bronze Layer    |
                | Raw Delta Table   |
                +-------------------+
                          |
                          v
                +-------------------+
                |   Silver Layer    |
                | Cleaning &        |
                | Validation        |
                +-------------------+
                          |
                          v
                +-------------------+
                |    Gold Layer     |
                | Business          |
                | Aggregations      |
                +-------------------+
                          |
                          v
                +-------------------+
                | Databricks AI/BI  |
                |    Dashboard      |
                +-------------------+
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Technology Stack:

Technology	Purpose
Python	Data processing
PySpark	Distributed data processing
Spark SQL	Data querying and validation
Databricks	Data engineering platform
Delta Lake	Reliable table storage
Unity Catalog	Data organization and governance
AI/BI Dashboard	Data visualization
GitHub	Version control
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Dataset:
The healthcare dataset contains patient-related information including:
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

The raw CSV is stored in a Databricks Unity Catalog managed volume and is not included in this repository.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Bronze Layer
The Bronze layer stores the source data in Delta format while preserving the original structure.

Source
patients_records.csv
Databricks Volume
/Volumes/workspace/default/healthcare_raw/
Bronze Table
workspace.default.bronze_patients
Processing
Read raw CSV using PySpark
Preserved source data
Stored data as a Delta table
Used Delta column mapping to support source column names containing spaces
Records ingested: 55,500
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Silver Layer
The Silver layer performs data cleaning, transformation, and validation on the Bronze dataset.

Silver Table
workspace.default.silver_patients
Transformations
Duplicate Removal
Total Bronze records: 55,500
Distinct records: 54,966
Duplicate records removed: 534
Name Standardization
Inconsistent capitalization was standardized using PySpark initcap().
Example:
DaNnY sMiTh → Danny Smith
Data Type Standardization
Column	Data Type
Age	Integer
Billing Amount	Double
Room Number	Integer
Date of Admission	Date
Discharge Date	Date

Data Quality Validation

Null values checked
Invalid ages checked
Invalid admission/discharge dates checked
Negative billing amounts identified and removed
Validation Results
Negative billing records removed: 106
Invalid age records: 0
Invalid date records: 0
NULL values: 0
Final Silver Dataset
54,860 records
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Gold Layer
The Gold layer contains business-ready datasets created from the cleaned Silver data.
1. Condition Summary
workspace.default.gold_condition_summary

Provides:

Total patients by medical condition
Average patient age
Average billing
Total billing
2. Hospital Summary
workspace.default.gold_hospital_summary

Provides:

Patient count by hospital
Average patient age
Average billing
Total billing
3. Insurance Summary
workspace.default.gold_insurance_summary

Provides:

Patient count by insurance provider
Average patient age
Average billing
Total billing
Dashboard

The Gold datasets are used to create a Databricks AI/BI Dashboard for healthcare analytics.

Dashboard Name

Healthcare Patient Analytics Dashboard

Key Performance Indicators
Total Patients
Total Billing
Average Patient Age
Average Billing
Visualizations
Patients by Medical Condition
Patients by Insurance Provider
Total Billing by Medical Condition
Average Billing by Medical Condition
Top 10 Hospitals by Patient Count
Average Patient Age by Medical Condition
Dashboard Preview

Data Quality Summary
Metric	Result
Raw Records	55,500
Duplicate Records Removed	534
Negative Billing Records Removed	106
Invalid Age Records	0
Invalid Date Records	0
NULL Values	0
Final Silver Records	54,860
Repository Structure
Healthcare-Patient-Analytics-Databricks/
│
├── notebooks/
│   ├── 01_Bronze_Ingestion.py
│   ├── 02_Silver_Transformation.py
│   └── 03_Gold_Aggregation.py
│
├── dashboard/
│   └── healthcare-dashboard.png
│
└── README.md
Future Enhancements

The current implementation uses batch processing. The following enhancements can be added in future versions:

Slowly Changing Dimension (SCD) Type 2 using MERGE
Real-time ingestion using Apache Kafka
Automated pipelines using Delta Live Tables
Incremental data processing
Predictive healthcare analytics
Machine Learning / MLOps integration
Power BI or Tableau integration
Key Learning Outcomes

This project demonstrates practical experience with:
Medallion Architecture
PySpark data processing
Spark SQL
Delta Lake
Databricks
Unity Catalog
Data quality and validation
Data transformation
Business-level data aggregation
Dashboard development
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Author
Aksh Jain
B.Tech Computer Science & Engineering
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
