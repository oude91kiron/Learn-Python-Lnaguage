from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+90546455845",
    from_="+11111111010",
    body="have a nice day")

print(message.sid)
