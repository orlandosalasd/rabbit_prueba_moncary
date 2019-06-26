import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test')

# body = input('Please type down the message: ')
for i in range(1, 11):
    channel.basic_publish(exchange='', routing_key='test', body=str(i))

print('[X] Sent')
connection.close()