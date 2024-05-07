from flask import Flask, render_template, request


app = Flask(__name__)
mock_data = {
    'question': "2 + 2 =",
    'fields' : ['5', '4']
}

@app.get("/")
def index():
    return render_template('poll.html', data = mock_data)

filename = "data.txt"

@app.get('/poll')
def poll():
    vote = request.args.get('field')
    with open(filename , "a") as out:
        out.write(vote + '\n')

    return f' your answer = {vote}'

if __name__ == '__main__':
    app.run(debug=True)