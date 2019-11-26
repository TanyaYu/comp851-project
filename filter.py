# If a lead is in the United States
# then they should be put into a PostgreSQL
# database table named leads.  If they are not and
# they have a known CC number, then they should go
# into a database table named high_priority, and
# otherwise all leads should be deposited into a text file.

from lead import Lead
import db


def filter(leads):
    for lead in leads:
        if lead.country == 'United States':
            # put into a PostgreSQL table leads
            pass
        elif lead.cc:
            # database table named high_priority
            pass
        else:
            # deposited into a text file
            write_into_file(lead)


def write_into_file(item):
    f = open("leads.txt", "a")
    f.write(str(item))
    f.write('\n')
    f.close()

leads = db.get_leads()
print(*leads)
filter(leads)
