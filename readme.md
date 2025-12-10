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
# 🚖 Taxi Travel Management System

_A centralized web application to automate corporate taxi bookings, streamline employee travel tracking, and eliminate manual redundancy using Streamlit and PostgreSQL._

---

## 📌 Table of Contents
- [Overview](#overview)
- [Business Problem & Motivation](#business-problem--motivation)
- [Project Structure](#project-structure)
- [Database & Schema](#database--schema)
- [Tools & Technologies](#tools--technologies)
- [Key Features](#key-features)
- [How to Run This Project](#how-to-run-this-project)
- [Future Roadmap](#future-roadmap)
- [Author & Contact](#author--contact)

---

## <a name="overview"></a>Overview
This project facilitates the digital transformation of corporate transport operations. It replaces fragmented excel sheets and manual logbooks with a robust database application. The system allows admin users to instantly search trip details, assign employees to vehicles in bulk, generate unique voucher codes, and maintain a secure historical record for auditing and vendor reconciliation.

---

## <a name="business-problem--motivation"></a>Business Problem & Motivation
Managing employee transport via manual methods (Excel/Email/Paper) creates significant operational bottlenecks:

* **Operational Inefficiency:** Manually copying employee details (Name, ID, Address) from dump files to booking logs is slow and error-prone, especially during high-volume shift changes.
* **Data Integrity & Duplication:** Without system validation, duplicate voucher numbers are often issued, leading to vendor billing disputes.
* **Lack of Visibility:** Transport teams struggle to track "Who traveled in which cab?" effectively. Retrieving historical data for audits is time-consuming.
* **Cost Leakage:** Inability to optimize cab occupancy (grouping employees effectively) often results in higher travel costs.
* **Vendor Reconciliation:** manual logs make it difficult to verify vendor invoices against actual trips taken.

**The Solution:** This system acts as a bridge between raw transport data and finalized bookings, enforcing unique vouchers, validating employee data, and saving distinct records for every passenger.

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