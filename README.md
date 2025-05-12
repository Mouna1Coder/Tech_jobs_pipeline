
# Tech Jobs Data Pipeline Project

This project demonstrates a simple yet effective data engineering pipeline using Python, MySQL, and Google Looker Studio. It extracts, transforms, and loads tech job listings into a MySQL database and visualises the insights via a custom dashboard.

## 📁 Project Structure

tech_jobs_pipeline/
│
├── etl/
│ ├── extract.py # Extracts data from the original source
│ ├── transform.py # Cleans and formats the extracted data
│ ├── load.py # Loads cleaned data into MySQL
│
├── db/
│ └── db_connection.py # Manages MySQL connection
│
├── data/
│ └── clean_jobs.csv # Cleaned CSV file ready for loading
│
└── README.md # This file


## 💡 What This Project Does

1. **Extracts** job data from a CSV or API (based on your setup).
2. **Transforms** it: cleaning null values, standardising column formats, etc.
3. **Loads** the data into a MySQL database.
4. **Visualises** insights via Google Looker Studio using a Google Sheets connector.

## 🛠️ Tech Stack

- **Python** (for ETL scripts)
- **MySQL** (for storing structured data)
- **Google Sheets** (used to link MySQL data with Looker Studio)
- **Looker Studio** (for dashboard visualisation)
- **Pandas** (for data transformation)
- **mysql-connector-python** (for DB integration)

## ⚙️ How to Run

1. Clone this repository.
2. Make sure you have the required packages installed:
   ```bash
   pip install pandas mysql-connector-python
3.Update your MySQL credentials in db/db_connection.py.

4.Run the ETL pipeline in order:

bash
Copy
Edit
python extract.py
python transform.py
python load.py
The clean data will appear in the data/clean_jobs.csv file and be loaded into your MySQL database.

5.Upload the CSV to Google Sheets.

6.Connect the sheet to Looker Studio and build interactive charts.

📊 Dashboard
The dashboard includes:

Number of jobs per company

Job locations distribution

Tags breakdown

Detailed table of job postings

📝 Notes
All data used in this project is fictional or publicly available and used for demonstration purposes only.


📫 Contact
If you have any questions, feel free to open an issue or contact the creator via G
