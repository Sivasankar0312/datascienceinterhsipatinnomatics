from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/', methods=["POST","GET"])
def index():
    if request.method=="POST":
        name=request.form['note']
        notes.append(name)
        return render_template("home.html", notes=notes)
    else:
        note = request.args.get("note")
        notes.append(note)
        return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, redirect, url_for, request
app = Flask(__name__)
