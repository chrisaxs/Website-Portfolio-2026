from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Flask looks for index.html inside the 'templates' folder
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)