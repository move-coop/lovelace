from utils import logger, setup_environment
from parsons import GoogleBigQuery, Table
from __future__ import print_function
import os.path
import time
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/contacts.readonly','https://www.googleapis.com/auth/directory.readonly','https://www.googleapis.com/auth/admin.directory.orgunit.readonly','https://www.googleapis.com/auth/admin.directory.user.readonly','https://www.googleapis.com/auth/admin.directory.group']
SERVICE_ACCOUNT_FILE = 'example.json'

# Need to impersonate someone with admin privileges. 
admin = 'admin@org.org'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES, subject=admin)

group_key = 'sample@org.org'

def main(db: GoogleBigQuery):

    service = build('admin', 'directory_v1', credentials=credentials)
    sql = "select distinct email from dataset.table"
    tbl = db.query(sql)
    if tbl.num_rows==0:
        logger.info("No rows were returned as a result of the query.")
    else:
        temp = tbl.to_json()
        j = open(temp)
        json_string = json.load(j)

        #######################################################################################

        json_data = json.loads(json_string)
        for i in json_data:
            data = i
            idata = json.dumps(data)
            print(idata)
            member = json.loads(idata)
            try:
                service.members().insert(groupKey=group_key, body=member).execute()
            except HttpError as error:
                error_response = error.resp
                logger.info(f"Error response: {error_response}")
            time.sleep(1)
        #######################################################################################



if __name__ == "__main__":
	setup_environment()
	db = GoogleBigQuery()
	main(db=db)