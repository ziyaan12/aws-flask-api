rom flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {"message": "You should hire Ziyaan Osman, you won't regret it!"}
