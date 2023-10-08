from flask import Flask, jsonify, request
from id_generator import IDGenerator

app = Flask(__name__)
id_generator = IDGenerator()

@app.route('/generate_id', methods=['GET'])
def generate_id():
    id_type = request.args.get('type', 'uuid')
    quantity = min(int(request.args.get('quantity', 1)), 1000)
    ids = id_generator.generate_ids(id_type, quantity)
    return jsonify(ids)

if __name__ == '__main__':
    app.run(debug=True)
