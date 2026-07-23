Markdown# ☁️ AWS RDS MySQL Python Connector

An automated Python tool built with `pymysql` to manage **AWS RDS MySQL** instances. It supports dynamic database initialization, table creation, bulk data insertion, full **CRUD (Create, Read, Update, Delete)** operations, and formatted terminal output.

---

## ⚡ Features At A Glance

* 🔐 **Secure Configuration**: Isolates sensitive database credentials using a local `config.py`.
* 🛠️ **Auto-Provisioning**: Creates target database and tables dynamically if absent.
* 🔄 **Full CRUD Operations**: Functions to insert, query, update, delete, and trim database rows.
* 📦 **Bulk Data Handling**: Executes fast multi-row `INSERT` queries via parameter binding (`%s`).
* 📊 **CMD Table Rendering**: Displays fetched records in clean, aligned terminal tables.

---

## 🔄 System Workflow

```mermaid
flowchart TD
    A[Start Execution] --> B[Load Config Details]
    B --> C[Establish TCP Connection on Port 3306]
    C --> D{AWS Security Group Check}
    
    D -- IP Allowed --> E[Authenticate Credentials]
    D -- IP Denied / Blocked --> F[❌ Connection Timeout Error]
    
    E --> G{Database Exists?}
    G -- No --> H[Execute CREATE DATABASE]
    G -- Yes --> I[Select & USE Target DB]
    H --> I
    
    I --> J{Table Exists?}
    J -- No --> K[Execute CREATE TABLE]
    J -- Yes --> L[Perform Operations]
    K --> L
    
    L --> M[Perform CRUD Operations]
    M --> N[SELECT Query Execution]
    N --> O[Format & Display Output in CMD]
    O --> P[Close RDS Connection Safely]
💻 CRUD Operations GuideThe connector script exposes modular functions for standard database operations:OperationFunction NameSQL Query ExecutedCREATEcreate_user(username, email)INSERT INTO users (username, email) VALUES (%s, %s);READread_all_users()SELECT * FROM users ORDER BY id ASC;UPDATEupdate_user_email(user_id, new_email)UPDATE users SET email = %s WHERE id = %s;DELETEdelete_user(user_id)DELETE FROM users WHERE id = %s;Code Usage ExamplePython# 1. READ records
read_all_users()

# 2. CREATE a new user
create_user("qa_tester", "qa.tester@example.com")

# 3. UPDATE user email by ID
update_user_email(1, "admin_updated@example.com")

# 4. DELETE a user by ID
delete_user(2)
☁️ AWS RDS Instance Setup Guide1️⃣ Create the MySQL InstanceConfiguration FieldRecommended SettingEngine TypeMySQLTemplateFree Tier (or Dev/Test)DB Instance IdentifiermydbMaster UsernameadminMaster Password(Your secure password)Public AccessYes (Required for local connection)2️⃣ Configure Security Group Rules (Crucial)Allow your local IP address to access MySQL over port 3306:Open RDS Console ➔ Databases ➔ Click your instance.Under Connectivity & security, click the VPC security group link.Select Inbound rules ➔ Edit inbound rules.Add the following rule:PlaintextType: MYSQL/Aurora  |  Protocol: TCP  |  Port: 3306  |  Source: My IP
🛠️ Prerequisites & InstallationPython 3.xPyMySQL Library:DOSpip install pymysql
🚀 QuickstartStep 1: Clone RepositoryDOSgit clone [https://github.com/Parmitadhara/aws-rds-python-mysql.git](https://github.com/Parmitadhara/aws-rds-python-mysql.git)
cd aws-rds-python
Step 2: Create Environment ConfigurationCreate a config.py file in the project root:PythonRDS_HOST = "your-rds-endpoint.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "your-password"
TARGET_DB = "mydb"
PORT = 3306
⚠️ Note: config.py is included in .gitignore to keep credentials off GitHub.Step 3: Run the ScriptDOSpython test_rds.py
