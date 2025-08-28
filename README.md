# 🚗 Vehicle Data ETL Pipeline

A clean, modular **ETL pipeline** that ingests a raw vehicles CSV, **transforms** it into analytics‑ready data, and **loads** it into a SQLite database for **SQL analysis** and easy extension to cloud.

---

## ✨ Highlights
- **End‑to‑end ETL**: Extract → Transform → Load
- **Production style**: modular code, logging, error handling
- **Feature engineering**: adds `car_age`
- **Database ready**: loads to SQLite (`vehicles.db`) with a single command
- **Analysis included**: SQL queries for common business questions
- **Cloud‑friendly**: structure easily ports to PostgreSQL / AWS RDS & Airflow

---

## 🧱 Architecture
```mermaid
flowchart LR
    A[Raw CSV: vehicles_dataset.csv] --> B[Extract (extract.py)]
    B --> C[Transform (transform.py)
        • clean missing values
        • normalize text
        • type casting
        • feature: car_age
        • de-dup]
    C --> D[Load (load.py) → SQLite: data/vehicles.db (table: vehicles)]
    D --> E[Analytics: sql_queries.sql / BI / Dashboard]
```

---

## 📂 Project Structure
```
vehicle_data_pipeline/
├── data/
│   ├── vehicles_dataset.csv          # raw input
│   └── vehicles.db                   # SQLite database (created by pipeline)
├── extract.py                        # read & validate CSV
├── transform.py                      # clean, normalize, feature engineer
├── load.py                           # write to SQLite
├── main.py                           # orchestration (runs ETL)
├── utils.py                          # logging & DB helpers
├── sql_queries.sql                   # analysis queries
├── requirements.txt                  # python deps
└── README.md                         # this file
```

---

## 🧪 Dataset Schema (Input)
**Rows:** ~1,000 | **Columns:** 18

| Column | Type | Notes |
|---|---|---|
| name | string | Listing title (e.g., "2024 Jeep Wagoneer Series II") |
| description | string? | Optional free text |
| make | string | Brand (e.g., Jeep, GMC, RAM) |
| model | string | Model name |
| type | string | New/Used/Certified |
| year | int | Model year |
| price | float? | Price; may be missing |
| engine | string? | Engine spec text |
| cylinders | float? | e.g., 4, 6, 8 (may be missing) |
| fuel | string? | e.g., gasoline, diesel (may be missing) |
| mileage | float? | Odometer reading; may be missing |
| transmission | string? | e.g., 8-Speed Automatic |
| trim | string? | Variant/trim |
| body | string? | e.g., SUV, Pickup Truck |
| doors | float? | e.g., 4 |
| exterior_color | string? |  |
| interior_color | string? |  |
| drivetrain | string? | e.g., Four-wheel Drive |

> `?` indicates fields that may contain missing values in the raw file.

---

## 🔧 Transformation Rules
- **De-duplication**: remove exact duplicate rows
- **Missing values**
  - `price` → median of available `price`
  - `mileage` → median of available `mileage`
  - `fuel` → "unknown"
- **Normalization**
  - `fuel`, `transmission` → lowercased and trimmed
- **Type casting**
  - Ensure `year` = int; `price`, `mileage` numeric
- **Feature engineering**
  - `car_age` = `current_year` − `year`

> All steps are logged with record counts before/after.

---

## ▶️ Quickstart

### 1) Environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Place data
Put your raw file at `data/vehicles_dataset.csv` (already included in this repo).

### 3) Run ETL
```bash
python main.py
```
This will create `data/vehicles.db` with a table named `vehicles`.

### 4) Run Analysis Queries
Use your favorite SQLite client, or:
```bash
sqlite3 data/vehicles.db < sql_queries.sql
```

---

## 🧩 Code Overview

### `utils.py`
- `get_logger(name)` → standard structured logging
- `get_db_connection(db_path)` → ensures `data/` exists and opens SQLite connection

### `extract.py`
- `extract_data(file_path)` → reads CSV; logs shape; raises on failure

### `transform.py`
- `transform_data(df)` → applies rules above, adds `car_age`, logs final shape

### `load.py`
- `load_data(df, table_name)` → writes DataFrame to SQLite (`if_exists="replace"`)

### `main.py`
- `run_pipeline()` → orchestrates Extract → Transform → Load

---

## 🧠 Analysis – `sql_queries.sql`
```sql
-- 1) Average price by brand
SELECT make, ROUND(AVG(price), 2) AS avg_price
FROM vehicles
GROUP BY make
ORDER BY avg_price DESC;

-- 2) Top 5 most expensive cars
SELECT name, make, model, year, price
FROM vehicles
ORDER BY price DESC
LIMIT 5;

-- 3) Average mileage by fuel type
SELECT fuel, ROUND(AVG(mileage), 2) AS avg_mileage
FROM vehicles
GROUP BY fuel
ORDER BY avg_mileage DESC;

-- 4) Price vs. age (avg)
SELECT car_age, ROUND(AVG(price), 2) AS avg_price
FROM vehicles
GROUP BY car_age
ORDER BY car_age ASC;

-- 5) Most common drivetrain per brand
SELECT make, drivetrain, COUNT(*) AS cnt
FROM vehicles
GROUP BY make, drivetrain
ORDER BY cnt DESC;
```

---

## 🧱 Extending to Cloud / Orchestration
- **Database**: swap SQLite for PostgreSQL (local Docker or AWS RDS)
- **Orchestration**: add an **Airflow** or **Prefect** DAG to schedule daily/weekly
- **Storage**: land raw CSVs in S3/Blob/GCS; version with timestamps
- **CI/CD**: GitHub Actions to run tests + lint + pipeline on PRs
- **Serving**: build a Streamlit or Power BI dashboard on top of the DB

---

## ✅ What This Project Demonstrates
- Realistic **data cleaning & standardization**
- **Feature engineering** for downstream analytics
- **Database modeling** and **SQL querying**
- **Reproducible** pipeline with clear separation of concerns

---

## 🧭 Roadmap
- [ ] Unit tests (pytest) for transform logic
- [ ] Data validation (Great Expectations)
- [ ] Dockerfile + Compose (SQLite → Postgres)
- [ ] Airflow DAG
- [ ] Streamlit dashboard

---

## 📄 License
MIT – free to use and adapt.

---

## 🤝 Contributing
PRs & issues welcome! Please open an issue to discuss major changes.

---

## 🙌 Acknowledgements
Sample dataset provided by the project owner for educational purposes.

