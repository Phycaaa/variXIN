from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/change', methods=['POST'])
def change():
    shirt = request.form['shirt']
    pants = request.form['pants']
    shoes = request.form['shoes']
    return render_template('index.html', shirt=shirt, pants=pants, shoes=shoes)

if __name__ == '__main__':
    app.run()
