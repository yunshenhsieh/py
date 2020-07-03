from flask import Flask

app = Flask(__name__)

@app.route('/hello/<username>')
def helloFlask(username):
    return 'Hello {}'.format(username)

if __name__ == '__main__' :
    app.run(debug=True,host='0.0.0.0',port=5000)