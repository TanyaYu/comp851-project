import db
from filter import filter 


data = db.get_leads()
filter(data)
