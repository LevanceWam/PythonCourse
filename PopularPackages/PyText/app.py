from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)

client.messages.create(
    to=config.phone,
    from_=config.twilio_number,
    body=config.text_message
)
