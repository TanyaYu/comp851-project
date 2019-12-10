import pika
from parser import binary_to_json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='leads')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

    item = binary_to_json(body)
    #Write the leads into the txt file
    f = open("leads.txt", "a")
    f.write(str(item))
    f.write('\n')
    f.close()

channel.basic_consume(queue='leads', auto_ack=True, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
