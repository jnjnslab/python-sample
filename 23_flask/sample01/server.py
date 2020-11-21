from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        print("post")
        rqname = request.form['name']
        print(rqname)
        rqgender = request.form['gender']
        print(rqgender)
        rqcolor = request.form.getlist("color")
        print(rqcolor)
        rqbloodtype = request.form['bloodtype']
        print(rqbloodtype)

        return redirect('/')

app.run()
