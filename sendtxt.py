import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='leads')

def send_to_txt(item):
    channel.basic_publish(exchange='', routing_key='leads', body=str(item))

# connection.close()
