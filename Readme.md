# ✨Schedule DBT job with Airflow✨
### We are using three technologies in this project
 - Airflow
 - DBT (Data Build Tool)
 - Snowflake (any other warehouse)
 
#### Step 1:  setup Airflow using below link
 - [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)

#### Step 2: Then create account on DBT and snowflake
- [Snowflake (30 days free trial) ](https://signup.snowflake.com/?utm_cta=trial-en-www-homepage-top-right-nav-ss-evg&_ga=2.74406678.547897382.1657561304-1006975775.1656432605&_gac=1.254279162.1656541671.Cj0KCQjw8O-VBhCpARIsACMvVLPE7vSFoPt6gqlowxPDlHT6waZ2_Kd3-4926XLVs0QvlzvTvIKg7pgaAqd2EALw_wcB)
- [DBT (14-day free trial)](https://www.getdbt.com/signup/)

#### Step 3: Connect database with DBT
- Ex: Database = Snowflake 
  - Open snowflake account
  - select admin >> partners connect
  - search dbt
  - connect with dbt and launch

#### Step 4: Create dag in airflow dag folder
