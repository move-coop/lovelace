# THIS IS A SAMPLE SCRIPT USED IN REDSHIFT

from __future__ import print_function

import os.path
import pandas as pd
import civis
import time
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly','https://www.googleapis.com/auth/directory.readonly','https://www.googleapis.com/auth/admin.directory.orgunit.readonly','https://www.googleapis.com/auth/admin.directory.user.readonly','https://www.googleapis.com/auth/admin.directory.group']
SERVICE_ACCOUNT_FILE = 'example.json'

# Need to impersonate someone with admin privileges. 
admin = 'admin@org.org'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES, subject=admin)

group_key = 'sample@org.org'

def main():
    
    
    creds = credentials


    service = build('admin', 'directory_v1', credentials=creds)


    sql = "select distinct email from schema.table"

  
    try:
        run = civis.io.read_civis_sql(sql, database="TMC", use_pandas=True)
    except civis.base.EmptyResultError:
        print("No rows were returned as a result of the query.")
    else:
        json_string = run.to_json(orient = "records")


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
                print(f"Error response: {error_response}")
            time.sleep(1)
        #######################################################################################


if __name__ == '__main__':
    main()