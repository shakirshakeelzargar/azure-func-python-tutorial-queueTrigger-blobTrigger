import smtplib, ssl

def send_email(message_dict):
    print(message_dict['to'])
    print(message_dict['body'])

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "shakirshakeelzargar11@gmail.com"
    password = "orwcwwkdhindlqsb"
    receiver_email = message_dict['to']
    message = message_dict['body']

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print("Email Successfully Sent")