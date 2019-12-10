import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='leadsdb')
channel.queue_declare(queue='leadsdb_high_priority')


def callback_leads(ch, method, properties, body):
    print(" [x] Received leads %r" % body)
    string = body.decode()
    item = json.dumps(str(string))


def callback_high_priority(ch, method, properties, body):
    print(" [x] Received high priority %r" % body)
    string = body.decode()
    item = json.dumps(str(string))



channel.basic_consume(queue='leadsdb', auto_ack=True, on_message_callback=callback_leads)
channel.basic_consume(queue='leadsdb_high_priority', auto_ack=True, on_message_callback=callback_high_priority)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

#Need to send the the database, but how is the question???
