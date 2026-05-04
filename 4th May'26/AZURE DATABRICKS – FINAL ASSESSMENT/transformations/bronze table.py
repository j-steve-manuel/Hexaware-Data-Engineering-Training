import dlt
from pyspark.sql.functions import col, lit

@dlt.table(
    name="hospital_bronze",
    comment="Raw patient visit data ingested from source."
)
def hospital_bronze():
    data = [
    (101,"Arjun Reddy","Hyderabad","Cardiology",5000,1),
    (102,"Sneha Kapoor","Delhi","Orthopedics",3000,2),
    (103,"Rahul Sharma","Mumbai","Dermatology",1500,1),
    (104,"Priya Nair","Bangalore","Cardiology",5000,2),
    (105,"Vikram Singh","Chennai","Neurology",7000,1),
    (106,"Ananya Das","Kolkata","Orthopedics",3000,3),
    (107,"Karan Patel","Ahmedabad","Cardiology",5000,1),
    (108,"Meera Iyer","Bangalore","Dermatology",1500,2)
    ]
    columns = [
    "visit_id",
    "patient_name",
    "city",
    "department",
    "consultation_fee",
    "tests_count"
    ]
    return spark.createDataFrame(data, columns)