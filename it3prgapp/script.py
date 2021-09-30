from flask import Flask, render_template           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def ahoj():                      # call method hello
    return "Hello World!"         # which returns "hello world"if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    pole=["jedna","dve","tri"]
    return render_template('script.html', name=name, pole=pole)