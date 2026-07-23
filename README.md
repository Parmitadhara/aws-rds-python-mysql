\# AWS RDS MySQL Python Connector



A Python script using `pymysql` to connect to an AWS RDS MySQL instance. Supports dynamic database creation, table setup, bulk data insertion, and retrieving formatted records directly in terminal.



\## Requirements

\- Python 3.x

\- `pymysql` (`pip install pymysql`)



\## Setup

1\. Create a `config.py` file in the root directory:

&#x20;  ```python

&#x20;  RDS\_HOST = "your-rds-endpoint"

&#x20;  DB\_USER = "admin"

&#x20;  DB\_PASSWORD = "your-password"

&#x20;  TARGET\_DB = "mydb"

&#x20;  PORT = 3306

