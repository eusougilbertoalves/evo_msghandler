from flask import Flask, request
from message_sender import MessageSender
from message_receiver import MessageReceiver

app = Flask(__name__)

@app.route("/messages-upsert", methods=['POST'])
def funcao():
    
    data = request.get_json()     

    receiver = MessageReceiver(data)
        
    sender = MessageSender()

    sender.textMessage(number=receiver.phone, message="Olá, tudo bem?")
    #sender.textMessage(number=msg.phone, msg=msg.text_message)

    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)