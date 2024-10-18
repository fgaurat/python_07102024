
from celery import Celery



def main():
    app = Celery("celery_tasks",broker="pyamqp://guest@localhost//",backend='rpc://d')
    r = app.send_task('celery_tasks.add',args=(1,3)) 
    print(r.get())
if __name__=='__main__':
    main()
