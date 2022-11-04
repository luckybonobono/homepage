from flask import Flask,render_template, request
import sys
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/applyphoto')
def photo_apply():
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    built_in = request.args.get("built")
    print(location, cleaness, built_in)
    #return render_template('apply.html')


@app.route('/list')
def list():
    return render_template('list.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0')
