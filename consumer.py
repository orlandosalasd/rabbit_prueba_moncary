import pika, random
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test')


def callback(ch, method, properties, body):
    time = random.randint(1, 10)
    print(body, time)
    sleep(float(time))
    print(f'[X] recived {body.decode()}')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test', on_message_callback=callback, auto_ack=True)

print('Waiting for a message...')
channel.start_consuming()
