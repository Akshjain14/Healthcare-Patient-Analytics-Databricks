# Databricks notebook source
silver_df = spark.table("workspace.default.silver_patients")

silver_df.show(5)

# COMMAND ----------

from pyspark.sql.functions import col, count, avg, sum

condition_summary = silver_df.groupBy("Medical Condition").agg(
    count("*").alias("total_patients"),
    avg("Age").alias("avg_age"),
    avg("Billing Amount").alias("avg_billing"),
    sum("Billing Amount").alias("total_billing")
)

condition_summary.show(truncate=False)

# COMMAND ----------

condition_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .option("delta.columnMapping.mode", "name") \
    .saveAsTable("workspace.default.gold_condition_summary")

# COMMAND ----------

spark.sql("""
SELECT *
FROM workspace.default.gold_condition_summary
ORDER BY total_patients DESC
""").show(truncate=False)

# COMMAND ----------

from pyspark.sql.functions import count, avg, sum

hospital_summary = (
    silver_df
    .groupBy("Hospital")
    .agg(
        count("*").alias("total_patients"),
        avg("Age").alias("avg_age"),
        avg("Billing Amount").alias("avg_billing"),
        sum("Billing Amount").alias("total_billing")
    )
)

hospital_summary.show(10, truncate=False)

# COMMAND ----------

hospital_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.default.gold_hospital_summary")

# COMMAND ----------

spark.sql("""
SELECT *
FROM workspace.default.gold_hospital_summary
""").show(10, truncate=False)

# COMMAND ----------

from pyspark.sql.functions import count, avg, sum

insurance_summary = silver_df.groupBy("Insurance Provider").agg(
    count("*").alias("total_patients"),
    avg("Age").alias("avg_age"),
    avg("Billing Amount").alias("avg_billing"),
    sum("Billing Amount").alias("total_billing")
)

insurance_summary.show(truncate=False)

# COMMAND ----------

insurance_summary = insurance_summary.withColumnRenamed(
    "Insurance Provider",
    "Insurance_Provider"
)

insurance_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.default.gold_insurance_summary")

# COMMAND ----------

spark.sql("""
SELECT *
FROM workspace.default.gold_insurance_summary
""").show(10, truncate=False)

# COMMAND ----------

print("Condition Summary:", spark.table("workspace.default.gold_condition_summary").count())
print("Hospital Summary:", spark.table("workspace.default.gold_hospital_summary").count())
print("Insurance Summary:", spark.table("workspace.default.gold_insurance_summary").count())

# COMMAND ----------

top_hospitals = spark.sql("""
SELECT
    Hospital,
    total_patients,
    avg_age,
    avg_billing,
    total_billing
FROM workspace.default.gold_hospital_summary
ORDER BY total_patients DESC
LIMIT 10
""")

top_hospitals.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.default.gold_top_hospitals")

# COMMAND ----------

spark.table("workspace.default.gold_top_hospitals").show(truncate=False)
