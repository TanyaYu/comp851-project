import pika
import psycopg2
from config import config
from parser import binary_to_json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='leadsdb')
channel.queue_declare(queue='leadsdb_high_priority')


def callback_leads(ch, method, properties, body):
    # print(" [x] Received leads %r" % body)
    item = binary_to_json(body)
    connect(item, high_priority=False)



def callback_high_priority(ch, method, properties, body):
    # print(" [x] Received high priority %r" % body)
    item = binary_to_json(body)
    connect(item, high_priority=True)



def connect(item, high_priority):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        id = item["id"]
        first_name = item["first_name"]
        last_name =  item["last_name"]
        email = item["email"]
        gender = item["gender"]
        ip_address = item["ip_address"]
        cc = item["cc"]
        country = item["country"]
        birthdate = item["birthdate"]
        salary = item["salary"]
        title = item["title"]

        if birthdate == '':
            birthdate = '01-01-2018'
        if salary == '':
            salary = 0
        else:
            salary = salary.replace("$",'')
            salary = float(salary)
        if cc == '':
            cc = 0

        #insertVariblesIntoTable(id, first_name, last_name, email, gender, ip_address, cc, country, birthdate, salary, title)
        my_sql_leads = 'INSERT INTO leads(id, first_name, last_name, email, gender, ip_address, cc, country, birthdate, salary, title) VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)'
        my_sql_high_priority = 'INSERT INTO high_priority(id, first_name, last_name, email, gender, ip_address, cc, country, birthdate, salary, title) VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)'
        record_tuple = (id, first_name, last_name, email, gender, ip_address, cc, country, birthdate, salary, title)
        if high_priority:
            cur.execute(my_sql_high_priority, record_tuple)
        else:
            cur.execute(my_sql_leads, record_tuple)
        conn.commit()
        print("Record inserted successfully into Leads table")
        db_version = cur.fetchone()
        print(db_version)

       # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


#def insertVariblesIntoTable(Id, First_name, Last_name, Email, Gender, Ip_address, CC, Country, Birthdate, Salary, Title):








channel.basic_consume(queue='leadsdb', auto_ack=True, on_message_callback=callback_leads)
channel.basic_consume(queue='leadsdb_high_priority', auto_ack=True, on_message_callback=callback_high_priority)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

#Need to send the the database, but how is the question???
