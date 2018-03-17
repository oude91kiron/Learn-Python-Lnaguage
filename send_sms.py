from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACfb9e97bcc27752b8460f055f0a1b387a"
# Your Auth Token from twilio.com/console
auth_token  = "9ea08f29d9fd667bbfa99a0f13cc50d8"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+905386978055",
    from_="+15408811010",
    body="have a nice day your bro Oude")

print(message.sid)
