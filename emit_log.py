import pika
from sys import argv
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

information_type = argv[1]

body = " ".join(argv[2:])

data = {
    'type': information_type,
    'info': body,
}

json_str = json.dumps(data)

channel.basic_publish(exchange='logs', routing_key='', body=json_str)

print('[X] sent')

connection.close()
