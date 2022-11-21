import requests
import os

API_key = os.getenv("API_KEY", None)
API_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric"

def get_request(lat,lon,key):
    requests_url = API_url.format(lat=lat,lon=lon,key=key)
    json = requests.get(requests_url).json()
    return json

def get_weather(json):
    weather_condition = json["weather"][0]["id"]
    temperature = json["main"]["temp"]
    humidity = json["main"]["humidity"]
    return weather_condition, temperature, humidity

def map_condition(id):
    match id:
        case 200, 201, 202, 210, 211, 212, 221, 230, 231, 232:
            return "THUNDERSHOWER"
        case 300, 310, 500, 520:
            return "LIGHT_RAIN"
        case 301, 311, 313, 321, 501, 521, 531:
            return "MODERATE_RAIN"
        case 302, 312, 314, 502, 522:
            return "HEAVY_RAIN"
        case 503:
            return "STORM"
        case 504:
            return "SEVERE_STORM"
        case 511:
            return "ICE_RAIN"
        case 600, 615, 620:
            return "LIGHT_SNOW"
        case 601, 616, 621:
            return "MODERATE_SNOW"
        case 602, 622:
            return "HEAVY_SNOW"
        case 611, 612, 613:
            return "SLEET"
        case 701, 711, 721:
            return "HAZE"
        case 731:
            return "DUSTSTORM"
        case 761, 762:
            return "DUST"
        case 741:
            return "FOGGY"
        case 751:
            return "SAND"
        case 771:
            return "BLUSTERY"
        case 781:
            return "TORNADO"
        case 800:
            return "CLEAR"
        case 801:
            return "PARTLY_CLOUDY1"
        case 802:
            return "PARTLY_CLOUDY2"
        case 803:
            return "MOSTLY_CLOUDY1"
        case 804:
            return "MOSTLY_CLOUDY2"


if __name__ == "__main__":
    eiffel_tower = get_request(lat=48.85, lon=2.29, key=API_key)
    weather_id, temperature, humidity = get_weather(eiffel_tower)
    condition = map_condition(weather_id)

    print(f"Humidity: {humidity:.1f} \nTemperature: {temperature:.1f} \nWeather Condition: {condition}")