CREATE DATABASE airflow;

\c analytics;
CREATE TABLE sample_data (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    value INT NOT NULL
);
