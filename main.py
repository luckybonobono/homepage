from flask import Flask, render_template, request, redirect, url_for
import sys, database
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
    if cleaness == None:
        cleaness = False
    else:
        cleaness = True

    database.save(location, cleaness, built_in)
    return render_template('apply_photo.html')

@app.route('/upload_done', methods=["POST"])
def upload_done():
    upload_files = request.files["file"]
    upload_files.save("static/img/{}".format(database.now_index()))

    return redirect(url_for("hello"))



@app.route('/list')
def list():
    house_list = database.load_list()
    return render_template('list.html', house_list = house_list)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
