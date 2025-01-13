# code for initiate jenkins job remotely 

import requests

jenkins_job = "demo-job"
jenkins_url = "<jenkins-url>"
jenkins_user = "bob"
jenkins_token = "<token_id>"

result = requests.post(jenkins_url , auth=(jenkins_user,jenkins_token))

if result.status_code == 201:
  print(f"job {jenkins_job} launched successfully!")
else:
  print("Please check the job name or Credentials. Something went Wrong!")
