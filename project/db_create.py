from views import db
from models import Task
from datetime import date

db.create_all()
#db.session.add(Task("Finish this tutorial", date(2016, 5, 28), 10, 1))
#db.session.add(Task("Finish Real Python", date(2016, 5, 28), 10, 1))

db.session.commit()
