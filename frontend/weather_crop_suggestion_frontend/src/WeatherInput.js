import React, { useState } from 'react';
import axios from 'axios';

function WeatherInput() {
    const [location, setLocation] = useState('');
    const [weatherData, setWeatherData] = useState({});
    const [cropSuggestions, setCropSuggestions] = useState([]);

    const fetchWeather = async () => {
        try {
            const response = await axios.get(`http://localhost:5000/api/weather?location=${location}`);
            const weatherData = response.data;
    
            if (!weatherData || !weatherData.main || !weatherData.main.temp) {
                console.error('Invalid weather data:', weatherData);
                return;
            }

            // Chuyển đổi nhiệt độ từ Kelvin sang Celsius
            weatherData.main.temp = weatherData.main.temp - 273.15;

            setWeatherData(weatherData);
        } catch (error) {
            console.error('Error fetching weather:', error);
        }
    };

    const getSuggestions = async () => {
        try {
            console.log('Sending weather data for suggestions:', weatherData);
            const suggestionsResponse = await axios.post('http://localhost:5000/api/suggestions', weatherData);
            const data = suggestionsResponse.data;
            console.log('Crop Suggestions:', data);
            setCropSuggestions(data);
        } catch (error) {
            console.error('Error fetching suggestions:', error);
        }
    };

    return (
        <div className="container">
    <div className="input-data-container">
        <div className="input-section">
            <input
                type="text"
                placeholder="Nhập địa điểm"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
            />
            <button onClick={fetchWeather}>Lấy Thời Tiết</button>
            <button onClick={getSuggestions}>Gợi Ý Cây Trồng</button>
            <div className="weather-data">
                <h2>Dữ Liệu Thời Tiết</h2>
                {weatherData.main && (
                    <div>
                        <p><strong>Nhiệt độ:</strong> {weatherData.main.temp.toFixed(2)} °C</p>
                        <p><strong>Độ ẩm:</strong> {weatherData.main.humidity}%</p>
                        <p><strong>Áp suất:</strong> {weatherData.main.pressure} hPa</p>
                        <p><strong>Tốc độ gió:</strong> {weatherData.wind.speed} m/s</p>
                        <p><strong>Mô tả:</strong> {weatherData.weather[0].description}</p>
                    </div>
                )}
            </div>
        </div>
        <div className="data-section">
            <div className="crop-suggestions">
                <h2>Gợi Ý Trồng Cây</h2>
                {cropSuggestions.map((crop, index) => (
                    <div key={index}>
                        <h3>{crop.name}</h3>
                        <p><strong>Điều kiện thích hợp:</strong> {crop.conditions}</p>
                        <p><strong>Quy trình trồng:</strong> {crop.care}</p>
                        <p><strong>Thời gian thu hoạch:</strong> {crop.harvest_time}</p>
                        <p><strong>Bón phân, chăm sóc:</strong> {crop.fertilization}</p>
                    </div>
                ))}
            </div>
        </div>
    </div>
</div>

    );
}

export default WeatherInput;
