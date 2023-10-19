from twilio.rest import Client
TWILIO_SID = "AC1d880e4709af6139d7198b7a0c60d556"
TWILIO_AUTH = "b4e5e88af397c6ce3413a350a7acf79f"
TWILIO_VIRTUAL_NUMBER = "+12245854646"
TWILIo_VERIFIED_NUMBER = "+91918369789524"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.client = Client(TWILIO_SID, TWILIO_AUTH)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message, from_=TWILIO_VIRTUAL_NUMBER, to=TWILIo_VERIFIED_NUMBER)

        print(message.sid)
