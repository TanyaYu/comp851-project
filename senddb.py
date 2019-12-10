import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='leadsdb')

def send_to_db(item):
    channel.basic_publish(exchange='', routing_key='leadsdb', body=str(item))

def send_to_db_high_priority(item):
    channel.basic_publish(exchange='', routing_key='leadsdb_high_priority', body=str(item))

# connection.close()
