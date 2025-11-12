from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаем запросы с фронтенда

@app.route('/api/message', methods=['GET'])
def get_message():
    """API endpoint, возвращающий сообщение"""
    return jsonify({
        'message': 'Когда будем работать пацаны?'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
