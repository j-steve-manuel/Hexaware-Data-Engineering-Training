import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="gold_hospital_summary"
)
def gold_hospital_summary():
    df = dlt.read("silver_patient_visits")

    return df.groupBy("city", "department").agg(
        count("*").alias("total_patients"),
        sum("number_of_tests").alias("total_tests"),
        sum("total_bill").alias("total_revenue")
    )