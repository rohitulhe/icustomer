ETL Pipeline Project

Overview
This project sets up an ETL pipeline using Apache Airflow to manage workflows, PostgreSQL for data storage, and custom ETL scripts for data processing. The setup is containerized using Docker and Docker Compose.

Prerequisites
Docker and Docker Compose, Git, Python installed on your machine.

SETUP 
1. Clone the repository using git clone <repo name>
2. Navigate to project directory and run the requiremts.txt file on the terminal, using pip install -r requirements.txt command
2. Configure Docker by running docker-compose up --build
3. After Docker is up, you will be able to see the Postgres, Airflow running on the specified URL
4. Run the ETL dag from Airflow webserver.
5. You can connect to postgres using pgadmin client.

Required Credentials
Airflow webserver : username: admin, password: admin
Postgres, username: airflow password: airflow
PGadmin client, username:admin@admin.com, password: admin
