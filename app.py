from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/yes')
def yes_page():
    return render_template('yes.html')

@app.route('/yes2')
def yes_page():
    return render_template('yes2.html')

@app.route('/yes_yes')
def yes_page():

    return render_template('yes_yes.html')
@app.route('/yes_yes_yes')

def yes_page():
    return render_template('yes_yes_yes.html')

@app.route('/no')
def no_page():
    return render_template('no.html')

@app.route('/no_no')
def no_page():
    return render_template('no_no.html')

@app.route('/no_no_no')
def no_page():
    return render_template('no_no_no.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
