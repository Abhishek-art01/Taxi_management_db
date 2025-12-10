# 🚖 Taxi Travel Management System

_A streamlined web application to automate corporate taxi bookings, employee travel tracking, and voucher generation using Streamlit and PostgreSQL._

---

## 📌 Table of Contents
- [Overview](#overview)
- [Business Problem](#business-problem)
- [Database & Schema](#database--schema)
- [Tools & Technologies](#tools--technologies)
- [Project Structure](#project-structure)
- [Key Features & Logic](#key-features--logic)
- [User Interface](#user-interface)
- [How to Run This Project](#how-to-run-this-project)
- [Future Enhancements](#future-enhancements)
- [Author & Contact](#author--contact)

---

## <a name="overview"></a>Overview
This project facilitates the digital management of corporate taxi travel. It replaces manual logbooks with a centralized database application that allows for instant trip identification, employee verification, bulk voucher generation, and historical record viewing. The system ensures data integrity through strict validation rules and duplicate checks.

---

## <a name="business-problem"></a>Business Problem
Managing employee transport manually leads to several operational inefficiencies:
- **Data Redundancy:** Duplicate voucher numbers and trip records.
- **Manual Errors:** Incorrect employee IDs or names entered during rush hours.
- **Lack of Visibility:** Difficulty in tracking past trips or auditing travel costs.
- **Time Consumption:** Manually filling details for multiple employees on the same trip is slow.

**Solution:** A unified interface to fetch trip details automatically, assign employees in bulk, and generate secure records in a PostgreSQL database.

---

## <a name="database--schema"></a>Database & Schema
The system connects to a **PostgreSQL** database containing the following key tables:

* **`application_data_dump`**: Raw data source for application-based trip requests.
* **`manual_data_dump`**: Raw data source for manual/ad-hoc trip requests.
* **`taxi_travels`**: The master transactional table where confirmed bookings are stored.
    * *Columns:* `trip_id`, `travel_date`, `employee_id`, `voucher_no`, `amount`, `direction`, etc.

---

## <a name="tools--technologies"></a>Tools & Technologies
- **Frontend:** Streamlit (Python)
- **Database:** PostgreSQL
- **Backend Logic:** Python (Pandas, Psycopg2)
- **Configuration:** TOML (Secrets Management)
- **Deployment:** Streamlit Community Cloud / Local Host

---

## <a name="project-structure"></a>Project Structure
The project follows a modular structure to separate data, logic, and configuration:

```text
project_root/
│
├── .streamlit/                    # Streamlit configuration
│   └── secrets.toml               # Database credentials (DO NOT UPLOAD TO GITHUB)
│
├── data/                          # Raw data directories
│   ├── application_files/         # Source for App-based trip data
│   └── manual_files/              # Source for Manual/Ad-hoc trip data
│
├── images/ 
│       ├──dashboard_preview.png|  # UI screenshots and assets
│       ├──login_preview.png|      # UI screenshots and assets
│       ├──trip_preview.png|       # UI screenshots and assets
│
├── scripts/                       # Application source code
│   ├── data_loader_src.py         # ETL scripts to load dump data into DB
│   └── taxi_data_entry_web.py     # Main Streamlit application file
│
├── .gitignore                     # Git ignore rules (secrets, venv, etc.)
├── readme.md                      # Project documentation
└── requirements.txt               # Python dependencies