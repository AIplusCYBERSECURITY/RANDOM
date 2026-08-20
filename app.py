from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    return jsonify({
        "status": "success",
        "message": "Python Back-end Connected Successfully!"
    })

if __name__ == '__main__':
    app.run(debug=True)