import pandas as pd
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
import time
from utils import *

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

df = pd.read_csv("./Syllabus_Response.csv")
df = df.astype(str)
df_email_sent = pd.read_csv("./Sent_Email_History.csv")
df_email_sent = df_email_sent.astype(str)

course_title = ""
university_name = ""
instructor_email_id = ""
prof_name = ""

email_sent_list = list(df_email_sent["instructor_email_id"])
newly_sent_list = []
for i, row in df.iterrows():

	instructor_email_id, modified_email_subject, modified_email_body = get_email_subject_body(row)

	if(instructor_email_id == None or  modified_email_subject == None or modified_email_body == None):
		continue

	if(instructor_email_id in email_sent_list or instructor_email_id in newly_sent_list):
		continue
	
	service = build('gmail', 'v1', credentials=creds)
	message = MIMEText(modified_email_body, 'html')
	# message['to'] = instructor_email_id
	message['to'] = temp_email_id #Temporarily overwriting instructor email address
	message['subject'] = modified_email_subject
	# message['cc'] = prof_vaccaro_email
	create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
	try:
		message = (service.users().messages().send(userId="me", body=create_message).execute())
		print(F'sent message to {message} Message Id: {message["id"]}')
		newly_sent_list.append(instructor_email_id)
	except Exception as exception:
		print(F'An exception occurred: {exception}')
		continue
	time.sleep(1)
	# if(len(newly_sent_list) >=2):
	# 	break

print("Newly sent email ids = ", newly_sent_list)

email_sent_list = email_sent_list + newly_sent_list
email_sent_df = pd.DataFrame({"instructor_email_id": email_sent_list})
email_sent_df.to_csv("./Sent_Email_History.csv", index = None)

