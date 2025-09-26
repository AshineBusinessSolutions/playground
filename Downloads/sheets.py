import gspread
from google.oauth2.service_account import Credentials
import psycopg2
import requests

KEY_FILE_PATH = '/Users/priyaangel/Downloads/tonal-nucleus-472723-u8-4bb8a367a123.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']
DB_CONFIG = {
    "host": "localhost",
    "database": "my_app_db",
    "user": "priyaangel",
    "password": "priya123",
    "port": "5432"
}


def get_sheets_client():

    try:
        creds = Credentials.from_service_account_file(KEY_FILE_PATH, scopes=SCOPES)
        return gspread.authorize(creds)
    except Exception as e:
        print(f"Error authenticating with Google Sheets: {e}")
        return None

def fetch_sheets_data(sheet_name='Students'):
    """Fetches all records from a specific worksheet in a Google Sheet."""
    client = get_sheets_client()
    if not client:
        return []
    try:
        sheet = client.open(sheet_name)

        worksheet = sheet.get_worksheet(0)
        data = worksheet.get_all_records()
        return data
    except Exception as e:
        print(f"Error fetching data from Google Sheets: {e}")
        return []


def db_conn():

    try:
        return psycopg2.connect(**DB_CONFIG)
    except psycopg2.OperationalError as e:
        print(f"Database connection failed: {e}")
        return None


def create_user(timestamp,fullname, email, phonenumber, university, major, linkedinprofile, githubprofile, resume):

    conn = db_conn()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            query = """
            INSERT INTO students (timestamp,fullname, email, phonenumber, university, major, linkedinprofile, githubprofile, resume)
            VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, (timestamp, fullname, email, phonenumber, university, major, linkedinprofile, githubprofile, resume))
        conn.commit()
    except Exception as e:
        print(f"Error creating user: {e}")
        conn.rollback()
    finally:
        conn.close()

def update_user(timestamp,fullname, email, phonenumber, university, major, linkedinprofile, githubprofile, resume):

    conn = db_conn()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            query = """
            UPDATE students SET
                timestamp = %s,
                fullname = %s,
                phonenumber = %s,
                university = %s,
                major = %s,
                linkedinprofile = %s,
                githubprofile = %s,
                resume = %s
            WHERE email = %s
            """
            cursor.execute(query, (timestamp,fullname, phonenumber, university, major, linkedinprofile, githubprofile, resume, email))
        conn.commit()
    except Exception as e:
        print(f"Error updating user: {e}")
        conn.rollback()
    finally:
        conn.close()



def get_users():

    conn = db_conn()
    if not conn: return []
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM students"
            cursor.execute(query)
            return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []
    finally:
        conn.close()

def sync_sheets_to_db():

    sheets_data = fetch_sheets_data()
    if not sheets_data:
        print("No data fetched from Google Sheets.")
        return

    conn = db_conn()
    if not conn:
        print("Could not connect to the database for syncing.")
        return

    print(f"Syncing {len(sheets_data)} records from Google Sheets to the database...")
    try:
        with conn.cursor() as cursor:
            for row in sheets_data:

                query = """
                INSERT INTO students (timestamp,fullname, email, phonenumber, university, major, linkedinprofile, githubprofile, resume)
                VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (email) DO UPDATE SET
                    timestamp = EXCLUDED.timestamp,
                    fullname = EXCLUDED.fullname,
                    phonenumber = EXCLUDED.phonenumber,
                    university = EXCLUDED.university,
                    major = EXCLUDED.major,
                    linkedinprofile = EXCLUDED.linkedinprofile,
                    githubprofile = EXCLUDED.githubprofile,
                    resume = EXCLUDED.resume;
                """
                cursor.execute(query, (
                    row.get('timestamp'),row.get('fullname'), row.get('email'), row.get('phonenumber'),
                    row.get('university'), row.get('major'), row.get('linkedinprofile'),
                    row.get('githubprofile'), row.get('resume')
                ))
        conn.commit()

    except Exception as e:
        print(f"An error occurred during sync: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    sync_sheets_to_db()
