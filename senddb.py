import pika
import filter from filter

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='leadsdb')

def send_item(item):
    channel.basic_publish(exchange='', routing_key='leadsdb', body='item')
    print(" [x] Sent Leads File")

connection.close()
