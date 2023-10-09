import re
from constants import *

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check_invalid_fields(field, type):
	if(type == "email"):
		if(not(re.fullmatch(email_regex, field))):
				return True
	else:
		if(field == None or len(str(field)) < 5):
			print("Invalid values of ", type, " and value is = ", field)
			return True
	return False


def get_email_subject_body(row):
	prof_name = str(row["Instructor Name"]).strip()
	university_name = str(row["University"]).strip()
	instructor_email_id = str(row["Instructor Email"]).strip()
	course_title = str(row["Title"]).strip()

	if(check_invalid_fields(instructor_email_id, "email")):
		alternate_email = row["Alternate Email (Department Head/Dept Chair)"]
		alternate_prof_name = row["Alternate Person Name (Department Head/Dept Chair)"]
		if(check_invalid_fields(alternate_email, "email") or check_invalid_fields(alternate_prof_name, "alternate_prof_name")):
			print("Skipping row due to missing alternate details - ", university_name, " and course title is : " , course_title)
			return None, None, None
		instructor_email_id = alternate_email
		prof_name = alternate_prof_name
		modified_email_body = dept_head_email_body.format(prof_name, course_title, university_name, university_name, course_title, course_title)
		modified_email_subject = dept_head_subject.format(course_title)
	else:
		modified_email_body = prof_email_body.format(prof_name, course_title, university_name)
		modified_email_subject = prof_email_subject.format(course_title)

	if(check_invalid_fields(prof_name, "prof_name") or check_invalid_fields(university_name, "university_name") or check_invalid_fields(course_title, "course_title")):
		return None, None, None


	return instructor_email_id, modified_email_subject, modified_email_body


