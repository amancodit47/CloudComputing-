from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

with app.app_context():
    db.create_all()
    if not User.query.first():
        db.session.add(User(username="admin", password="1234"))
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == "POST":
        u = request.form['username']
        p = request.form['password']
        if User.query.filter_by(username=u, password=p).first():
            message = "Login Successful"
        else:
            message = "Invalid Credentials"

    with open("login.html") as f:
        html = f.read()

    return html.replace("{{message}}", message)

if __name__ == "__main__":
    app.run(debug=True)