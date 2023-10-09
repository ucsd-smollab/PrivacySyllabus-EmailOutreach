prof_vaccaro_email = "kvaccaro@ucsd.edu"
temp_email_id = "aimanjunath97@gmail.com" #Temporarily overwriting instructor email address

prof_email_subject = "Request for Syllabus: {}"
prof_email_body = """
<html>
  <body>
  <div>Dear Professor {}, </div>
  <br>
  <div>I hope this email finds you well. I am writing to request your assistance with a research project that our group, based at the University of California San Diego (UCSD), is currently undertaking. The objective of our research is to develop a comprehensive understanding of how privacy is integrated into university curricula and educational practices.</div>
  <br>
  <div>In our data collection, we found your course, <b>"{}"</b> offered at {}.</div>  
  <br>
  <div>Would you be willing to share the syllabus (and, if possible, any assignments) with us? We are collecting a dataset of syllabuses to analyze as part of this effort. Any information you provide will be used solely for research purposes. By default none of the dataset will be shared, but if you are open to your syllabus being released as part of a larger dataset, please let us know! </div>
  <br>
  <div>We understand that your time is valuable, and appreciate any contribution you can make to this project.</div>
  <br>
  <div>Thank you for your time and consideration, and please reach out if you have any questions or concerns!</div>
  <br>
  <div>Yours,</div>
  <div>Aishwarya Manjunath (Graduate student lead)</div>
  <div>Kristen Vaccaro (Assistant professor)</div>
  </body>
</html>
  
"""

dept_head_subject = "Request for Contact Information of Professor Teaching: {}"
dept_head_email_body = """
<html>
  <body>
  <div>Dear Professor {}, </div>
  <br>
  <div>I hope this email finds you well. I am writing to request your assistance in identifying the professor for the course <b>"{}"</b> at {}.</div>
  <br>
  <div>Our research group, based at the University of California San Diego (UCSD), is currently conducting a study to develop a comprehensive understanding of how privacy is integrated into university curricula and educational practices.</div>  
  <br>
  <div>In our data collection, we found a course offered at {}, titled - {}.</div>
  <br>
  <div>We would like to request a copy of the syllabus, but were not able to identify the instructor for this course. Would you be able to provide contact information or the syllabus itself ? — for {}.</div>
  <br>
  <div>Thank you for your time and consideration, and please reach out if you have any questions or concerns!</div>
  <br>
  <div>Yours,</div>
  <div>Aishwarya Manjunath (Graduate student lead)</div>
  <div>Kristen Vaccaro (Assistant professor)</div>
  </body>
</html>
"""