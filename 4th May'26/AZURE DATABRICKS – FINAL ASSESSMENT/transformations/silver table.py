import dlt
from pyspark.sql.functions import col, lit, current_timestamp, sum, count

@dlt.table(
    name="hospital_silver",
    comment="Cleaned patient data with calculated total bills."
)
@dlt.expect_or_drop("valid_visit_id", "visit_id IS NOT NULL") # Data Quality Check
def hospital_silver():
    return dlt.read("hospital_bronze") \
        .withColumn("total_bill", col("consultation_fee") + (col("tests_count") * 500)) \
        .withColumn("ingestion_timestamp", lit(current_timestamp()))