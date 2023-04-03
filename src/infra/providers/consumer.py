import pika

class RabbitmqConsumer:
    def __init__(self, callback):
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "my_queue"
        self.callback = callback
        self.__channel = self.__create_channel()
    
    def __create_channel(self):
        conection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(self.__username, self.__password)
        )
        channel = pika.BlockingConnection(conection_parameters).channel()
        
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )

        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.callback
        )

        return channel
    
    def start(self):
        print(f'Listen RabbitMQ on Port {self.__port}')
        self.__channel.start_consuming()



