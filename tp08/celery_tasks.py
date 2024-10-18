
from celery import Celery

app = Celery("celery_tasks",broker="pyamqp://guest@localhost//",backend='rpc://d')

@app.task
def add(a,b):
    return a+b