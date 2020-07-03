from flask import Flask,request

app = Flask(__name__,static_url_path='/static1',static_folder='./static_0516')

@app.route('/hello_gt')
def hello_get():
    outStr="""<img src="/static1/color.png">"""
    return outStr

if __name__ == '__main__' :
    app.run(debug=True,host='0.0.0.0',port=5000)