-- SQL script to create the 'jobs' table for the Tech Jobs Data Pipeline project

CREATE DATABASE IF NOT EXISTS tech_jobs_db;
USE tech_jobs_db;

CREATE TABLE IF NOT EXISTS jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(255),
    position VARCHAR(255),
    location VARCHAR(255),
    tags VARCHAR(255),
    url TEXT
);
