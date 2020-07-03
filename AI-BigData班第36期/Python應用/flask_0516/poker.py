from flask import Flask,request,jsonify
from flask_0516 import poker_model as p


app = Flask(__name__)

@app.route('/poker', methods=['GET', 'POST'])
def poker():
    if request.method == 'GET':
        outStr = """
        <html>
            <head>
                <title>poker</title>
            </head>
            <body>
                <h1>How many players?</h1>
                <form action="/poker" method="post">
                    <input type="textbox" name="players">
                    <button type="submit">Submit</button>
                </form>
            </body>
        </html>
        """
        return outStr
    elif request.method == 'POST':
        players = request.form.get('players')
        cards = p.poker(int(players))
        return jsonify(cards)


if __name__ == '__main__' :
    app.run(debug=True,host='0.0.0.0',port=5000)

