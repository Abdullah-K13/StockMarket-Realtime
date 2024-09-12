# Real-Time Data Engineering Project

This repository contains my first real-time data engineering project, designed for self-learning. In this project, I process real-time data using **Apache Kafka** and upload the processed data to an **S3 bucket**. The data is then cataloged using an **AWS Glue Crawler**, and I query the data using **AWS Athena**.

## Project Overview

The project involves ingesting stock market data (sourced from a Kaggle dataset) into Apache Kafka, streaming the data in real time, and then pushing it to an S3 bucket. An AWS Glue crawler is used to generate a data catalog, which is later queried using Athena for analysis.

## Tech Stack

- **Apache Kafka**: For real-time data ingestion and streaming
- **AWS S3**: To store the processed streaming data
- **AWS Glue**: To create a data catalog for the ingested data
- **AWS Athena**: To query the data directly from S3
- **Docker**: For containerized deployment of all services
- **Python**: To orchestrate Kafka consumers and producers

## Dataset

I used the **Stock Market Data** from Kaggle to simulate real-time data ingestion in Kafka. The dataset includes stock prices, trading volumes, and other relevant metrics for analysis.

## Project Workflow

1. **Ingestion**: Stock market data is ingested into Kafka in real time.
2. **Processing**: Kafka streams the data to consumers running in Docker containers.
3. **Storage**: The processed data is uploaded to an AWS S3 bucket.
4. **Cataloging**: AWS Glue crawler is used to create a data catalog from the S3 data.
5. **Querying**: AWS Athena is used to query the data stored in S3 for further analysis.

## Architecture Diagram
![Architecture](https://github.com/user-attachments/assets/a06e0602-0596-4fed-8d45-da7ee4ae16ee)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repo-name.git
   cd repo-name
