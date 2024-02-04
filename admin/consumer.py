import pika,os,json,django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()


from products.models import Product 


params = pika.ConnectionParameters(host='rabbitmq_container', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

#Declaring a queque
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')
    
channel.basic_consume(queue='admin', on_message_callback=callback ,auto_ack=True)

print("started Consuming")

channel.start_consuming()

channel.close()