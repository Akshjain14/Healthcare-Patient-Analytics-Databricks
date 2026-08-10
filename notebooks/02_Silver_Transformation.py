# Databricks notebook source
silver_df = spark.table("workspace.default.bronze_patients")

# COMMAND ----------

silver_df.show(5)

# COMMAND ----------

silver_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col, sum

null_counts = silver_df.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in silver_df.columns
])

null_counts.show()

# COMMAND ----------

total_count = silver_df.count()
distinct_count = silver_df.distinct().count()

print("Total records:", total_count)
print("Distinct records:", distinct_count)
print("Duplicate records:", total_count - distinct_count)

# COMMAND ----------

silver_df = silver_df.dropDuplicates()

# COMMAND ----------

print("Silver records after removing duplicates:", silver_df.count())

# COMMAND ----------

from pyspark.sql.functions import initcap

silver_df = silver_df.withColumn(
    "Name",
    initcap("Name")
)

# COMMAND ----------

silver_df.select("Name").show(10, truncate=False)

# COMMAND ----------

from pyspark.sql.functions import col, to_date

# COMMAND ----------

silver_df = silver_df \
    .withColumn("Age", col("Age").cast("int")) \
    .withColumn("Billing Amount", col("Billing Amount").cast("double")) \
    .withColumn("Room Number", col("Room Number").cast("int")) \
    .withColumn("Date of Admission", to_date(col("Date of Admission"), "yyyy-MM-dd")) \
    .withColumn("Discharge Date", to_date(col("Discharge Date"), "yyyy-MM-dd"))

# COMMAND ----------

silver_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col, sum

silver_df.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in silver_df.columns
]).show()

# COMMAND ----------

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("delta.columnMapping.mode", "name") \
    .saveAsTable("workspace.default.silver_patients")

# COMMAND ----------

silver_check = spark.sql("""
SELECT *
FROM workspace.default.silver_patients
LIMIT 5
""")

silver_check.show()

# COMMAND ----------

spark.sql("""
SELECT COUNT(*) AS total_records
FROM workspace.default.silver_patients
""").show()

# COMMAND ----------

from pyspark.sql.functions import initcap

silver_df = silver_df.withColumn(
    "Name",
    initcap(col("Name"))
)

silver_df.select("Name").show(10, truncate=False)

# COMMAND ----------

categorical_cols = [
    "Gender",
    "Blood Type",
    "Medical Condition",
    "Insurance Provider",
    "Admission Type",
    "Medication",
    "Test Results"
]

for c in categorical_cols:
    print(f"\n--- {c} ---")
    silver_df.select(c).distinct().show(truncate=False)

# COMMAND ----------

from pyspark.sql.functions import min, max, avg

silver_df.select(
    min("Age").alias("min_age"),
    max("Age").alias("max_age"),
    min("Billing Amount").alias("min_billing"),
    max("Billing Amount").alias("max_billing")
).show()

# COMMAND ----------

negative_billing = silver_df.filter(
    col("Billing Amount") < 0
)

print("Negative billing records:", negative_billing.count())

# COMMAND ----------

negative_billing.select(
    "Name",
    "Age",
    "Medical Condition",
    "Hospital",
    "Billing Amount"
).show(10, truncate=False)

# COMMAND ----------

silver_df = silver_df.filter(
    col("Billing Amount") >= 0
)

print("Records after removing negative billing:",
      silver_df.count())

# COMMAND ----------

invalid_age = silver_df.filter(
    (col("Age") <= 0) | (col("Age") > 120)
)

print("Invalid age records:", invalid_age.count())

# COMMAND ----------

invalid_dates = silver_df.filter(
    col("Discharge Date") < col("Date of Admission")
)

print("Invalid date records:", invalid_dates.count())

# COMMAND ----------

from pyspark.sql.functions import col, sum

silver_df.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in silver_df.columns
]).show()

# COMMAND ----------

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("delta.columnMapping.mode", "name") \
    .saveAsTable("workspace.default.silver_patients")

# COMMAND ----------

spark.sql("""
SELECT COUNT(*) AS total_records
FROM workspace.default.silver_patients
""").show()
