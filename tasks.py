from __future__ import absolute_import, unicode_literals

from celery import Celery,task
from time import sleep

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task() 
def hello_world():
    return 'Hello world.........'

@app.task()
def UploadTask():
 
    # Update the state. The meta data is available in task.info dicttionary
    # The meta data is useful to store relevant information to the task
    # Here we are storing the upload progress in the meta. 
 
    UploadTask.update_state(state='PROGRESS', meta={'progress': 0})
    sleep(30)
    UploadTask.update_state(state='PROGRESS', meta={'progress': 30})
    sleep(30)
    UploadTask.update_state(state='SUCCESS', meta={'progress': 100})
    
