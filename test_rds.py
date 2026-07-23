import pymysql
import config

def get_connection():
    """Establish and return a connection to AWS RDS."""
    return pymysql.connect(
        host=config.RDS_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.TARGET_DB,
        port=config.PORT,
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )

# ----------------------------------------------------
# 1. CREATE (Insert Data)
# ----------------------------------------------------
def create_user(username, email):
    """Insert a single new record into the users table."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (username, email) VALUES (%s, %s);"
            cursor.execute(sql, (username, email))
            print(f"✅ [CREATE] User '{username}' added (ID: {cursor.lastrowid}).")
    except pymysql.MySQLError as err:
        print(f"❌ [CREATE Error]: {err}")
    finally:
        connection.close()

# ----------------------------------------------------
# 2. READ (Fetch & Display Data)
# ----------------------------------------------------
def read_all_users():
    """Fetch and display all records in a formatted table."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users ORDER BY id ASC;"
            cursor.execute(sql)
            records = cursor.fetchall()

            print("\n==================== RDS DATABASE: users ====================")
            print(f"{'ID':<6} | {'USERNAME':<20} | {'EMAIL':<30}")
            print("-" * 62)
            for row in records:
                print(f"{row['id']:<6} | {row['username']:<20} | {row['email']:<30}")
            print("-" * 62)
            print(f"Total Rows Retrieved: {len(records)}\n")
    except pymysql.MySQLError as err:
        print(f"❌ [READ Error]: {err}")
    finally:
        connection.close()

# ----------------------------------------------------
# 3. UPDATE (Modify Existing Record)
# ----------------------------------------------------
def update_user_email(user_id, new_email):
    """Update the email address for a specific user ID."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE users SET email = %s WHERE id = %s;"
            cursor.execute(sql, (new_email, user_id))
            if cursor.rowcount > 0:
                print(f"🔄 [UPDATE] ID {user_id}'s email updated to '{new_email}'.")
            else:
                print(f"⚠️ [UPDATE] No user found with ID {user_id}.")
    except pymysql.MySQLError as err:
        print(f"❌ [UPDATE Error]: {err}")
    finally:
        connection.close()

# ----------------------------------------------------
# 4. DELETE (Remove Record by ID)
# ----------------------------------------------------
def delete_user(user_id):
    """Delete a user record by ID."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM users WHERE id = %s;"
            cursor.execute(sql, (user_id,))
            if cursor.rowcount > 0:
                print(f"🗑️ [DELETE] User ID {user_id} removed.")
            else:
                print(f"⚠️ [DELETE] No user found with ID {user_id}.")
    except pymysql.MySQLError as err:
        print(f"❌ [DELETE Error]: {err}")
    finally:
        connection.close()

# ----------------------------------------------------
# 5. CLEANUP (Delete All Rows Above a Specific ID)
# ----------------------------------------------------
def trim_duplicate_rows(keep_below_id=12):
    """Clean up duplicate testing data while keeping early records."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM users WHERE id >= %s;"
            cursor.execute(sql, (keep_below_id,))
            print(f"🧹 [CLEANUP] Removed {cursor.rowcount} duplicate testing rows (IDs >= {keep_below_id}).")
    except pymysql.MySQLError as err:
        print(f"❌ [CLEANUP Error]: {err}")
    finally:
        connection.close()

# ----------------------------------------------------
# WORKFLOW EXECUTION
# ----------------------------------------------------
if __name__ == "__main__":
    print("🚀 Running AWS RDS CRUD Operations...\n")

    # Step 1: Clean up duplicate rows generated from repeated runs
    trim_duplicate_rows(keep_below_id=12)

    # Step 2: READ remaining records
    read_all_users()

    # Step 3: CREATE a new user
    create_user("qa_tester", "qa.tester@example.com")

    # Step 4: UPDATE user ID 1 email
    update_user_email(1, "admin_updated@example.com")

    # Step 5: DELETE user ID 2
    delete_user(2)

    # Step 6: READ final table state
    read_all_users()