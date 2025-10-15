import google.auth
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import psycopg2
from datetime import datetime
import logging
import time
import sys


logging.basicConfig(
    filename="/Users/priyaangel/update_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

KEY_FILE_PATH = '/Users/priyaangel/Downloads/ABS/tonal-nucleus-472723-u8-4bb8a367a123.json'

try:
    creds = Credentials.from_service_account_file(KEY_FILE_PATH)
    service = build('forms', 'v1', credentials=creds)
except Exception as e:
    logging.error(f"Error initializing Google service: {e}")
    print(f"Error initializing Google service: {e}")
    sys.exit(1)

form_id = '1ztWur5GRhTqQIO72PHtUpmP3fgaEEeR67MP9Dks6rt8'

TITLE_TO_COLUMN_MAP = {
    "Full Name": "fullname",
    "Email": "email",
    "Phone Number": "phonenumber",
    "University": "university",
    "Major": "major",
    "LinkedIn Profile": "linkedinprofile",
    "GitHub Profile": "githubprofile",
    "Resume": "resume"
}


def get_form_schema_and_map_questions(service, form_id, title_map):
    
    qid_to_column = {}
    try:
        logging.info("Fetching form schema for dynamic mapping...")
        form_metadata = service.forms().get(formId=form_id).execute()
        
        for item in form_metadata.get('items', []):
            question_item = item.get('questionItem', {})
            question_id = question_item.get('question', {}).get('questionId')
            
            question_title = item.get('title') 

            column_name = title_map.get(question_title)
            
            if question_id and column_name:
                qid_to_column[question_id] = column_name
                logging.debug(f"Mapped QID {question_id} to column {column_name}")
                
    except Exception as e:
        logging.error(f"Failed to fetch or parse form schema: {e}")
        print(f"FATAL: Failed to fetch form schema. Check form ID and API permissions. Error: {e}")
        sys.exit(1)
        
    if not qid_to_column:
        logging.error("Dynamic QID mapping resulted in an empty map. Check form titles and TITLE_TO_COLUMN_MAP.")
        print("FATAL: Could not map any form fields. Exiting.")
        sys.exit(1)

    return qid_to_column

qid_to_column = get_form_schema_and_map_questions(service, form_id, TITLE_TO_COLUMN_MAP)



MAX_RETRIES = 3
for attempt in range(MAX_RETRIES):
    try:
        logging.info(f"Fetching responses (Attempt {attempt + 1})...")
        response_data = service.forms().responses().list(formId=form_id).execute()
        responses = response_data.get('responses', [])
        logging.info(f"Successfully fetched {len(responses)} responses.")
        break  
    except Exception as e:
        logging.warning(f"Error fetching Google Forms data: {e}")
        if attempt < MAX_RETRIES - 1:
            time.sleep(2 ** attempt) 
        else:
            logging.error("Failed to fetch Google Forms data after multiple retries.")
            print("Failed to fetch Google Forms data after multiple retries. Check network or API quotas.")
            sys.exit(1)



try:
    conn = psycopg2.connect(
        host= "localhost",
        database= "my_app_db",
        user= "priyaangel",
        password="priya123",
        port= "5432"
    )
    cur = conn.cursor()
except Exception as e:
    logging.error(f"Error connecting to PostgreSQL: {e}")
    print(f"Error connecting to PostgreSQL: {e}")
    sys.exit(1)



new_rows = 0

for r in responses:
    try:
        
        submitted_at = r.get('lastSubmittedTime')
        submitted_at = datetime.fromisoformat(submitted_at.replace('Z', '+00:00'))

        answers_dict = r.get('answers', {})
        student_data = {"timestamp": submitted_at}

        for qid, ans in answers_dict.items():
            
       
            column_name = qid_to_column.get(qid)
            
            value = ans.get('textAnswers', {}).get('answers', [{}])[0].get('value')

            if column_name and value:
                student_data[column_name] = value

        if student_data:
            if 'email' not in student_data:
                logging.warning(f"Skipping response ID {r.get('responseId')}: 'email' field is missing or empty.")
                continue

            columns = ', '.join(student_data.keys())
            placeholders = ', '.join([f"%({k})s" for k in student_data.keys()])

            cur.execute(
                f"""
                INSERT INTO students ({columns})
                VALUES ({placeholders})
                ON CONFLICT (email) DO NOTHING;
                """,
                student_data
            )

            new_rows += cur.rowcount

    except Exception as e:
        logging.error(f"Error processing response ID {r.get('responseId')}: {e}")




try:
    conn.commit()
    logging.info(f"Successfully processed and committed {len(responses)} responses. Inserted {new_rows} new rows.")
    cur.close()
    conn.close()
except Exception as e:
    logging.error(f"Error during database commit/close: {e}")
