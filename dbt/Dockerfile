# Use official dbt image
FROM python:3.9
RUN pip install dbt-core dbt-postgres


# Set working directory
WORKDIR /dbt

# Copy the dbt project files
COPY . .

# Run dbt on container start
CMD ["dbt", "run"]
