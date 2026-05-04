import dlt
from pyspark.sql.functions import col, lit, current_timestamp, sum, count

@dlt.table(
    name="hospital_gold_dept_summary",
    comment="Summary of revenue and patient counts by department."
)
def hospital_gold_dept_summary():
    return dlt.read("hospital_silver") \
        .groupBy("department") \
        .agg(
            count("visit_id").alias("total_patients"),
            sum("total_bill").alias("total_revenue")
        )