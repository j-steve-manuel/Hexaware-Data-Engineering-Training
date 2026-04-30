import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="silver_patient_visits"
)
def silver_patient_visited():
    df = dlt.read("bronze_patient_visits")

    return df.select(
        col("visit_id"),
        upper(col("patient_name")).alias("patient_name"),
        upper(col("city")).alias("city"),
        upper(col("department")).alias("department"),
        col("consultation_fee").cast("int"),
        col("number_of_tests").cast("int"),
        (2000 * col("number_of_tests")).alias("test_cost"),
        (col("consultation_fee") + (2000 * col("number_of_tests"))).alias("total_bill"),
        
    ).filter(
        (col("consultation_fee") > 0) 
    )

