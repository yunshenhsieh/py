from flask import  Flask,request,render_template


app = Flask(__name__,static_url_path='/static1',static_folder='./static_0516')

@app.route('/hello_post',methods=['GET','POST'])
def hello_post():
    request_method = request.method
    username=''
    if request_method == 'POST':
        username = request.form.get('name')
    return render_template('hello_post.html',request_method=request_method,username=username)

if __name__ == '__main__' :
    app.run(debug=True,host='0.0.0.0',port=5000)