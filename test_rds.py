import pymysql
import config

# Use the variables from config.py
connection = pymysql.connect(
    host=config.RDS_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.TARGET_DB,
    port=config.PORT,
    autocommit=True,
    cursorclass=pymysql.cursors.DictCursor
)

# --- CONNECTION PARAMETERS ---
RDS_HOST = "mydb.c3q0yw24ewce.ap-south-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "redhat##"
TARGET_DB = "mydb"
PORT = 3306

# Dummy dataset containing 10 users
NEW_USERS = [
    ("priya_sharma", "priya.sharma@example.com"),
    ("rahul_verma", "rahul.v@example.com"),
    ("ananya_roy", "ananya.roy@example.com"),
    ("vikram_singh", "vikram.s@example.com"),
    ("neha_gupta", "neha.gupta@example.com"),
    ("amit_patel", "amit.p@example.com"),
    ("sneha_kulkarni", "sneha.k@example.com"),
    ("rohit_kumar", "rohit.k@example.com"),
    ("pooja_mehta", "pooja.m@example.com"),
    ("dev_joshi", "dev.j@example.com")
]

def populate_and_fetch_all():
    connection = None
    try:
        print("Connecting to AWS RDS MySQL database...")
        connection = pymysql.connect(
            host=RDS_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=TARGET_DB,
            port=PORT,
            autocommit=True,  # Ensures all INSERT operations are saved immediately
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected successfully!\n")

        with connection.cursor() as cursor:
            # 1. BULK INSERT DATA
            insert_query = "INSERT INTO users (username, email) VALUES (%s, %s);"
            cursor.executemany(insert_query, NEW_USERS)
            print(f"✅ Successfully inserted {cursor.rowcount} new records into AWS RDS!\n")

            # 2. RETRIEVE ALL DATA
            fetch_query = "SELECT * FROM users ORDER BY id ASC;"
            cursor.execute(fetch_query)
            all_records = cursor.fetchall()

            # 3. PRINT FORMATTED TABLE IN COMMAND PROMPT
            print("==================== RDS DATABASE: users ====================")
            print(f"{'ID':<6} | {'USERNAME':<20} | {'EMAIL':<30}")
            print("-" * 62)

            for record in all_records:
                user_id = record['id']
                username = record['username']
                email = record['email']
                print(f"{user_id:<6} | {username:<20} | {email:<30}")

            print("-" * 62)
            print(f"Total Rows Retrieved: {len(all_records)}")

    except pymysql.MySQLError as err:
        print(f"❌ MySQL Error: {err}")

    finally:
        if connection and connection.open:
            connection.close()
            print("\nRDS connection closed safely.")

if __name__ == "__main__":
    populate_and_fetch_all()