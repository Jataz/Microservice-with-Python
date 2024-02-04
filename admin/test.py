import pika

# Establish a connection to RabbitMQ
params = pika.URLParameters( "amqp://guest:guest@localhost:5672/")

connection = pika.BlockingConnection(params)
channel = connection.channel()

# Declare a queue
queue_name = 'my_queue1'
channel.queue_declare(queue=queue_name)

# Define the message to publish
message = 'Hello, RabbitMQ!'

# Publish the message to the queue
channel.basic_publish(exchange='', routing_key=queue_name, body=message)

# Close the connection
connection.close()