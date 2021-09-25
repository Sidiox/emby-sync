from app import app, db, INTERVAL
from app.functions import check_password, initRun, sync_cycle
from app.models import User, Session

initRun()
app.apscheduler.add_job(func=sync_cycle, trigger='interval', seconds=INTERVAL, id='sync_cycle')

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Session': Session, 'check_password': check_password}
