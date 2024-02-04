import pika

# Establish a connection to RabbitMQ
#params = pika.URLParameters( "amqp://guest:guest@localhost:5672/")
params = pika.ConnectionParameters(host='172.22.0.3', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Declare a queue
queue_name = 'flask'
channel.queue_declare(queue=queue_name)

# Define the message to publish
message = 'Hello, RabbitMQ!'

# Publish the message to the queue
channel.basic_publish(exchange='', routing_key=queue_name, body=message)

# Close the connection
connection.close()