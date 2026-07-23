Markdown# ☁️ AWS RDS MySQL Python Connector



An automated Python tool built with `pymysql` to manage \*\*AWS RDS MySQL\*\* instances. Automatically handles database creation, schema setup, bulk data insertion, and outputs formatted terminal tables.



\---



\## ⚡ Features At A Glance



\* 🔐 \*\*Secure Configuration\*\*: Keeps sensitive database credentials isolated using local config.

\* 🛠️ \*\*Auto-Provisioning\*\*: Creates target database and tables dynamically if they don't exist.

\* 📦 \*\*Bulk Data Handling\*\*: Executes fast multi-row `INSERT` queries using parameter binding.

\* 📊 \*\*CMD Table Rendering\*\*: Displays fetched records in clean, aligned terminal tables.



\---



\## 🔄 System Workflow



```mermaid

flowchart TD

&#x20;   A\[Start Execution] --> B\[Load Config Details]

&#x20;   B --> C\[Establish TCP Connection on Port 3306]

&#x20;   C --> D{AWS Security Group Check}

&#x20;   

&#x20;   D -- IP Allowed --> E\[Authenticate Credentials]

&#x20;   D -- IP Denied / Blocked --> F\[❌ Connection Timeout Error]

&#x20;   

&#x20;   E --> G{Database Exists?}

&#x20;   G -- No --> H\[Execute CREATE DATABASE]

&#x20;   G -- Yes --> I\[Select \& USE Target DB]

&#x20;   H --> I

&#x20;   

&#x20;   I --> J{Table Exists?}

&#x20;   J -- No --> K\[Execute CREATE TABLE]

&#x20;   J -- Yes --> L\[Perform Operations]

&#x20;   K --> L

&#x20;   

&#x20;   L --> M\[Bulk Insert Records]

&#x20;   M --> N\[SELECT Query Execution]

&#x20;   N --> O\[Format \& Display Output in CMD]

&#x20;   O --> P\[Close RDS Connection Safely]

☁️ AWS RDS Instance Setup Guide

1️⃣ Create the MySQL InstanceConfiguration FieldRecommended SettingEngine TypeMySQLTemplateFree Tier (or Dev/Test)DB Instance IdentifiermydbMaster UsernameadminMaster Password(Your secure password)Public AccessYes (Required for local connection)

2️⃣ Configure Security Group Rules (Crucial)Allow your local IP address to access MySQL over port 3306:Go to RDS Console ➔ Databases ➔ Click your instance.Under Connectivity \& security, click the VPC security group link.Select Inbound rules ➔ Edit inbound rules.Add the following rule:PlaintextType: MYSQL/Aurora  |  Protocol: TCP  |  Port: 3306  |  Source: My IP

🛠️ Prerequisites \& Installation

Python 3.xPyMySQL 

Library:DOS

pip install pymysql

