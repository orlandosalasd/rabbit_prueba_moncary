import pika
from sys import argv
import json
from send_email import send_email

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result_queue = channel.queue_declare(queue='', exclusive=True)

queue_name=result_queue.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)


def callback(ch, method, properties, body):
    body = body.decode()
    body = eval(body)
    information_type = argv[1]
    if information_type == 'debug':
        print(f'[X] received {body}')
        archive = open('message.txt', 'a+')
        archive.write(body['info'])
        archive.close()
        send_email(body['info'])

    elif information_type == 'info':
        if body['type'] == 'info' or body['type'] == 'warning' or body['type'] == 'error':
            print(f'[X] received {body}')
            archive = open('message.txt', 'a+')
            archive.write(body['info'])
            archive.close()
            send_email(body['info'])

    elif information_type == 'warning':
        if body['type'] == 'warning' or body['type'] == 'error':
            print(f'[X] received {body}')
            archive = open('message.txt', 'a+')
            archive.write(body['info'])
            archive.close()
            send_email(body['info'])

    elif information_type == 'error':
        if body['type'] == 'error':
            print(f'[X] received {body}')
            archive = open('message.txt', 'a+')
            archive.write(body['info'])
            archive.close()
            send_email(body['info'])


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print('Starting consuming')
channel.start_consuming()