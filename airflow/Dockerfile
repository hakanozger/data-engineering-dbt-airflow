# Use official Apache Airflow image
FROM quay.io/pypa/manylinux2014_aarch64
RUN yum install -y python3
RUN pip3 install apache-airflow


# Set working directory
WORKDIR /airflow

# Copy DAGs
COPY dags/ /opt/airflow/dags/

# Expose the Airflow webserver port
EXPOSE 8080

# Run Airflow scheduler and webserver
CMD ["airflow", "standalone"]
