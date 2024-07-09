from flask import Flask, request, jsonify
from flask_cors import CORS
from weather_api import get_weather_data
from crop_suggestion import suggest_crops
from config import WEATHER_API_KEY

app = Flask(__name__)
CORS(app)  # Cho phép tất cả các nguồn truy cập

@app.route('/api/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Yêu cầu nhập địa điểm'}), 400

    weather_data = get_weather_data(WEATHER_API_KEY, location)
    if not weather_data:
        return jsonify({'error': 'Không thể lấy dữ liệu thời tiết'}), 500

    return jsonify(weather_data)

@app.route('/api/suggestions', methods=['POST'])
def get_crop_suggestions():
    weather_data = request.json
    if not weather_data:
        return jsonify({'error': 'Yêu cầu dữ liệu thời tiết'}), 400

    print(weather_data)  # In dữ liệu thời tiết ra console
    suggestions = suggest_crops(weather_data)
    return jsonify(suggestions)


if __name__ == '__main__':
    app.run(debug=True)