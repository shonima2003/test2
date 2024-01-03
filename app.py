from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello! My name is [Your Name], and my USN is [Your USN].'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
