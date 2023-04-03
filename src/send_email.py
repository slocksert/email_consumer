from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
import json


class SendEmail:
    def __init__(self):        
        self.smtp_server = "smtp.gmail.com"
        self.email = "emailsenderapitest@gmail.com"
        self.password = "grfuiynzgvwrxkne"
        self.port = 465

    def send_email (self, ch, method, properties, body):
        context = ssl.create_default_context()
        body = body.decode('utf-8')
        body = json.loads(body)
        email_str = body['email']
        user_str = body['username']
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Confirmação de cadastro API"
        message["From"] = self.email
        message["To"] = email_str

        text = f"CADASTRO NO SISTEMA\nOlá, {user_str}\nBem vindo à minha API .\nSeu cadastro no sistema foi realizado com sucesso!\nObs: Está mensagem poderá ser entregue no Lixo Eletrônico antes mesmo da finalização do procedimento de cadastro. Portanto verifique sua caixa de SPAM." 

        html = f"""\
        <html>
            <body>
                <p>CADASTRO NO SISTEMA<br>
                <br>Olá, {user_str}<br>
                <br>Seu cadastro no sistema foi realizado com sucesso!<br>
                <br>Obs: Está mensagem poderá ser entregue no Lixo Eletrônico antes mesmo da finalização do procedimento de cadastro. Portanto verifique sua caixa de SPAM.
                </p>
            </body>
        </html>"""

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)


        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, email_str, message.as_string())
        
        print(f'Email sended to {email_str}') 