from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)

app.secret_key = 'mykey'

@app.route('/', methods=['GET','POST'])
def index():
    title = 'This is from python!'
    return render_template('index.html', title=title)

@app.route('/postmethod/<name>', methods=['GET','POST'])
def post_js_data(name):
    if name == 'evgenii':
        print(name)
    else:
        print('not evgenii', name)
    return 'https://metmod.com'

if __name__ == '__main__':
    app.run(debug=True)
