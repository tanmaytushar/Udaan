from twilio.rest import Client
import random

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

otp = str(round(random.random()*100000))
print(otp)

message = client.messages.create(
  from_='',
  body='Share this OTP: '+otp,
  to=''
)

print(message.sid)

