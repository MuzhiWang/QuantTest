from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    raise Exception('not sure')
    # return 'hollow world'


if __name__ == '__main__':
    app.run()