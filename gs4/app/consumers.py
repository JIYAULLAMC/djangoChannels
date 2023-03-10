from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Web socket Connect ++++++++++++++++!", event)
        self.send({
            "type":"websocket.accept",
        })

    def websocket_receive(self, event):
        print("message received from client ++++++++++",event)
        print(event["text"])
        self.send({
            "type": "websocket.send",
            "text": "message is send to sever!"
        })

    def websocket_disconnected(self, event):
        print("disconnected! ++++++++++++++", event)
        raise StopConsumer() 

