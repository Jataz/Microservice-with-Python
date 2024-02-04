import pika, json

params = pika.ConnectionParameters(host='rabbitmq_container', port=5672, credentials=pika.PlainCredentials('guest', 'guest'),heartbeat=65535)
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)