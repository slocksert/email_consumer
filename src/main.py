from infra.providers.consumer import RabbitmqConsumer
from send_email import SendEmail

send = SendEmail()

rabbitmq = RabbitmqConsumer(send.send_email)
rabbitmq.start()