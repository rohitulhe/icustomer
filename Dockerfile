# Use the official Airflow image
FROM apache/airflow:2.4.3

# Set environment variables for Airflow
ENV AIRFLOW_HOME=/opt/airflow
ENV PYTHONPATH="${AIRFLOW_HOME}/dags:${AIRFLOW_HOME}/etl:${PYTHONPATH}"

# Install additional dependencies
USER root
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && apt-get clean

USER airflow
RUN pip install pandas sqlalchemy psycopg2-binary

# Copy your DAGs and scripts into the Airflow container
COPY airflow/dags /opt/airflow/dags
COPY etl /opt/airflow/etl
COPY data /opt/airflow/data

