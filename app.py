# app.py
from flask import Flask, request, jsonify, render_template  
from flask_cors import CORS  # new
from perfume_detector import check_asthma_trigger, get_perfume_names

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/perfume', methods=['GET'])
def get_perfume():
    name = request.args.get('name')
    message = check_asthma_trigger(name)
    if message == 'Perfume not found':
        return jsonify({'message': message}), 404
    else:
        return jsonify({'message': message}), 200

@app.route('/perfumes', methods=['GET'])
def get_perfumes():
    names = get_perfume_names()
    return jsonify({'perfumes': names}), 200

if __name__ == '__main__':
    app.run(debug=True)