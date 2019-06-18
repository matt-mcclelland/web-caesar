from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form method='POST'>
        <label> Rotate by:
            <input name="rot" type="text" value="0" />
        </label>
        <textarea name="text" value="text" />{msg}</textarea>
        <input type="submit" value="Submit Query" />
    </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted = rotate_string(text, rot)

    return form.format(msg=encrypted)


@app.route("/")
def index():
    if request.args.get('encrypted'):
        encrypted  = request.args.get('encrypted')
    else:
        encrypted  = ''
    return form.format(msg=encrypted)

app.run()