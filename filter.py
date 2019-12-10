# If a lead is in the United States
# then they should be put into a PostgreSQL
# database table named leads.  If they are not and
# they have a known CC number, then they should go
# into a database table named high_priority, and
# otherwise all leads should be deposited into a text file.

from lead import Lead
import json
from sendtxt import send_to_txt
from senddb import send_to_db
from senddb import send_to_db_high_priority


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

#Calling RabbitMQ to send each lead as an item
def write_into_file(item):
    send_to_txt(item)

def put_in_leads(item):
    send_to_db(item)

def put_in_high_priority(item):
    send_to_db_high_priority(item)
