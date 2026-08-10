# Databricks notebook source
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "false") \
    .csv("/Volumes/workspace/default/healthcare_raw/patients_records.csv")

# COMMAND ----------

df.show(5)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.count()

# COMMAND ----------

df.write \
    .format("delta") \
    .option("delta.columnMapping.mode", "name") \
    .mode("overwrite") \
    .saveAsTable("workspace.default.bronze_patients")

# COMMAND ----------

spark.sql("""
SELECT COUNT(*) AS total_records
FROM workspace.default.bronze_patients
""").show()

# COMMAND ----------

spark.sql("""
SELECT *
FROM workspace.default.bronze_patients
LIMIT 5
""").show()
