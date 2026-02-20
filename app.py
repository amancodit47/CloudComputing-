from flask import Flask, request

app = Flask(__name__)

# Static Credentials
STATIC_USERNAME = "admin"
STATIC_PASSWORD = "1234"

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == STATIC_USERNAME and password == STATIC_PASSWORD:
            message = "Login Successful!"
        else:
            message = "Invalid Username or Password"

    return f"""
    <html>
    <head>
        <title>Login</title>
    </head>
    <body>
        <h2>Login Form</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required><br><br>
            <input type="password" name="password" placeholder="Password" required><br><br>
            <button type="submit">Login</button>
        </form>
        <p>{message}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
