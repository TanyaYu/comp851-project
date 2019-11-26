# If a lead is in the United States
# then they should be put into a PostgreSQL
# database table named leads.  If they are not and
# they have a known CC number, then they should go
# into a database table named high_priority, and
# otherwise all leads should be deposited into a text file.

from lead import Lead
import db
import json


def filter(data):
    leads = json.loads(data)
    for lead in leads:
        if lead["country"] == 'United States':
            # put into a PostgreSQL table leads
            put_in_leads(lead)
        elif lead["cc"]:
            # database table named high_priority
            put_in_high_priority(lead)
        else:
            # deposited into a text file
            write_into_file(lead)


def write_into_file(item):
    f = open("leads.txt", "a")
    f.write(str(item))
    f.write('\n')
    f.close()

def put_in_leads(item):
    pass

def put_in_high_priority(item):
    pass

data = db.get_leads()
filter(data)
