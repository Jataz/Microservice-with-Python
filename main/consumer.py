import pika
import json

from main import Product, db
# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq_container', port=5672, credentials=pika.PlainCredentials('guest', 'guest'),heartbeat=65535))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    print('Received body:', body)  # Print the body content for debugging purposes

    try:
        # Parse the JSON data
        data = json.loads(body)
        print('Parsed JSON data:', data)

        # Process the data based on content type
        if properties.content_type == 'product_created':
            product = Product(id=data['id'], title=data['title'], image=data['image'])
            db.session.add(product)
            db.session.commit()
            print('Product Created')

        elif properties.content_type == 'product_updated':
            product = Product.query.get(data['id'])
            product.title = data['title']
            product.image = data['image']
            db.session.commit()
            print('Product Updated')

        elif properties.content_type == 'product_deleted':
            product = Product.query.get(data)
            db.session.delete(product)
            db.session.commit()
            print('Product Deleted')

    except json.JSONDecodeError as e:
        print('Invalid JSON format:', str(e))

    # Acknowledge the message
    channel.basic_ack(delivery_tag=method.delivery_tag)

# Start consuming messages
channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')

# Keep consuming messages until interrupted
channel.start_consuming()