from flask import Flask
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form action="/blah" method="post">
                <label for="rotate">
                    Rotate by:
                    <input type="text" id="rotate" name="rot" />
                </label>

                <textarea name="text">
                </textarea>
                
                <input type="submit" value="Submit" />

            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.form["rot"])
    message = request.form["text"]
    return rotation, message
   # encrypted = rotate_string(rotation, message)
   # return '<h1'+encrypted+'</h1>'

app.run()