import requests

def get_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Nếu có lỗi HTTP, sẽ ném ra một exception
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None  # Hoặc có thể raise exception để xử lý ở nơi gọi hàm
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
        return None
