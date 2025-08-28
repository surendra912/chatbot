from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').lower()
    # Predefined Q&A
    if user_message in ['hi', 'hi, how are you?', 'hello chatbot!', 'hello', 'good morning!', "what's up?"]:
        if 'how are you' in user_message:
            bot_reply = "I'm a bot, but I'm doing great! How about you?"
        elif 'good morning' in user_message:
            bot_reply = "Good morning! Hope you have a wonderful day!"
        elif 'what\'s up' in user_message:
            bot_reply = "Not much, just here to chat with you!"
        else:
            bot_reply = "Hello! How can I help you today?"
    elif 'are you human' in user_message:
        bot_reply = "No, I'm an AI chatbot created to assist you."
    elif 'telugu' in user_message:
        bot_reply = "Avunu! Nenu Telugu matladagalanu. Mee kosam em cheyyali? (Yes! I can speak Telugu. How can I help you?)"
    elif 'who created you' in user_message:
        bot_reply = "I was created by a developer using Python and AI technology."
    elif 'your name' in user_message:
        bot_reply = "I'm Chatbot, your virtual assistant!"
    elif 'emotion' in user_message:
        bot_reply = "I don't have real emotions, but I can understand and respond to yours!"
    elif 'joke' in user_message:
        bot_reply = "Why did the computer show up at work late? It had a hard drive!"
    elif 'ai' in user_message and 'what' in user_message:
        bot_reply = "AI stands for Artificial Intelligence. It's the simulation of human intelligence in computers."
    elif 'prime minister of india' in user_message:
        bot_reply = "The Prime Minister of India is Narendra Modi."
    elif 'capital of france' in user_message:
        bot_reply = "The capital of France is Paris."
    elif 'machine learning' in user_message:
        bot_reply = "Machine learning is a way for computers to learn from data and make decisions without being explicitly programmed."
    elif '5g' in user_message:
        bot_reply = "5G is the fifth generation of mobile networks, offering faster speeds and more reliable connections."
    elif 'founder of microsoft' in user_message:
        bot_reply = "The founder of Microsoft is Bill Gates."
    elif 'distance between earth and moon' in user_message:
        bot_reply = "The average distance between Earth and the Moon is about 384,400 kilometers."
    elif 'cloud computing' in user_message:
        bot_reply = "Cloud computing means storing and accessing data and programs over the internet instead of your computer's hard drive."
    elif 'blockchain' in user_message:
        bot_reply = "Blockchain is a digital ledger technology that records transactions securely and transparently."
    elif 'latest iphone model' in user_message:
        bot_reply = "As of 2025, the latest iPhone model is the iPhone 15 series."
    elif 'bye' in user_message:
        bot_reply = 'Goodbye! Have a nice day!'
    else:
        bot_reply = "Sorry, I don't have an answer for that yet."
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
