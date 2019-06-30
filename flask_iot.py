from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World, Lets explore it. Try to learn new things.  "


@app.route('/<user>')
def name(user):
    return f"my name is {user}"


@app.route('/temp')
def name1():
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug = True)