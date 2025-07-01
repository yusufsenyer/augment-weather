import requests
import json
from typing import Dict, Union

def get_coordinates(city_name: str) -> Union[Dict, str]:
    """
    Şehir adına göre koordinatları bulur
    """
    try:
        geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
        response = requests.get(geocoding_url, params={
            "name": city_name,
            "count": 1,
            "language": "tr",
            "format": "json"
        })
        
        data = response.json()
        
        if not data.get("results") or len(data["results"]) == 0:
            return f"'{city_name}' şehri bulunamadı. Lütfen şehir adını kontrol edin."
        
        location = data["results"][0]
        return {
            "lat": location["latitude"],
            "lon": location["longitude"],
            "name": location["name"],
            "country": location.get("country", "")
        }
    except Exception as e:
        return f"Şehir koordinatları alınırken hata oluştu: {str(e)}"

def get_weather_description(code: int) -> str:
    """
    Weather code'u Türkçe açıklamaya çevirir
    """
    weather_codes = {
        0: "Açık",
        1: "Çoğunlukla açık",
        2: "Parçalı bulutlu",
        3: "Bulutlu",
        45: "Sisli",
        48: "Kırağılı sis",
        51: "Hafif çisenti",
        53: "Orta çisenti",
        55: "Yoğun çisenti",
        56: "Hafif dondurucu çisenti",
        57: "Yoğun dondurucu çisenti",
        61: "Hafif yağmur",
        63: "Orta yağmur",
        65: "Şiddetli yağmur",
        66: "Hafif dondurucu yağmur",
        67: "Şiddetli dondurucu yağmur",
        71: "Hafif kar",
        73: "Orta kar",
        75: "Şiddetli kar",
        77: "Kar taneleri",
        80: "Hafif sağanak",
        81: "Orta sağanak",
        82: "Şiddetli sağanak",
        85: "Hafif kar sağanağı",
        86: "Şiddetli kar sağanağı",
        95: "Gök gürültülü fırtına",
        96: "Hafif dolu ile gök gürültülü fırtına",
        99: "Şiddetli dolu ile gök gürültülü fırtına"
    }
    return weather_codes.get(code, "Bilinmeyen hava durumu")

def get_current_weather_by_city(city_name: str) -> str:
    """
    Şehir adına göre hava durumu bilgisi getirir
    """
    try:
        # Önce şehrin koordinatlarını al
        coordinates = get_coordinates(city_name)
        if isinstance(coordinates, str):  # Hata mesajı
            return coordinates
        
        # Koordinatlarla hava durumu bilgisini al
        weather_url = "https://api.open-meteo.com/v1/forecast"
        response = requests.get(weather_url, params={
            "latitude": coordinates["lat"],
            "longitude": coordinates["lon"],
            "current": [
                "temperature_2m",
                "relative_humidity_2m", 
                "apparent_temperature",
                "precipitation",
                "weather_code",
                "surface_pressure",
                "wind_speed_10m",
                "uv_index"
            ],
            "timezone": "auto"
        })
        
        data = response.json()
        current = data["current"]
        
        # Weather code'u açıklamaya çevir
        description = get_weather_description(current["weather_code"])
        
        # Sonucu formatla
        weather_info = {
            "şehir": coordinates["name"],
            "ülke": coordinates["country"],
            "sıcaklık": f"{round(current['temperature_2m'])}°C",
            "hissedilen": f"{round(current['apparent_temperature'])}°C",
            "durum": description,
            "nem": f"%{current['relative_humidity_2m']}",
            "rüzgar_hızı": f"{current['wind_speed_10m']} km/h",
            "basınç": f"{current['surface_pressure']} hPa",
            "uv_indeksi": current.get('uv_index', 0),
            "yağış": f"{current.get('precipitation', 0)} mm"
        }
        
        # Güzel bir format ile döndür
        result = f"""🌤️ {weather_info['şehir']}, {weather_info['ülke']} Hava Durumu

🌡️ Sıcaklık: {weather_info['sıcaklık']} (Hissedilen: {weather_info['hissedilen']})
☁️ Durum: {weather_info['durum']}
💧 Nem: {weather_info['nem']}
💨 Rüzgar: {weather_info['rüzgar_hızı']}
📊 Basınç: {weather_info['basınç']}
☀️ UV İndeksi: {weather_info['uv_indeksi']}
🌧️ Yağış: {weather_info['yağış']}"""
        
        return result
        
    except Exception as e:
        return f"Hava durumu bilgisi alınırken hata oluştu: {str(e)}"

def get_current_weather_by_coordinates(lat: float, lon: float) -> str:
    """
    Koordinatlara göre hava durumu bilgisi getirir
    """
    try:
        weather_url = "https://api.open-meteo.com/v1/forecast"
        response = requests.get(weather_url, params={
            "latitude": lat,
            "longitude": lon,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature", 
                "precipitation",
                "weather_code",
                "surface_pressure",
                "wind_speed_10m",
                "uv_index"
            ],
            "timezone": "auto"
        })
        
        data = response.json()
        current = data["current"]
        
        # Weather code'u açıklamaya çevir
        description = get_weather_description(current["weather_code"])
        
        # Sonucu formatla
        weather_info = {
            "konum": f"{lat:.2f}, {lon:.2f}",
            "sıcaklık": f"{round(current['temperature_2m'])}°C",
            "hissedilen": f"{round(current['apparent_temperature'])}°C",
            "durum": description,
            "nem": f"%{current['relative_humidity_2m']}",
            "rüzgar_hızı": f"{current['wind_speed_10m']} km/h",
            "basınç": f"{current['surface_pressure']} hPa",
            "uv_indeksi": current.get('uv_index', 0),
            "yağış": f"{current.get('precipitation', 0)} mm"
        }
        
        # Güzel bir format ile döndür
        result = f"""🌤️ {weather_info['konum']} Hava Durumu

🌡️ Sıcaklık: {weather_info['sıcaklık']} (Hissedilen: {weather_info['hissedilen']})
☁️ Durum: {weather_info['durum']}
💧 Nem: {weather_info['nem']}
💨 Rüzgar: {weather_info['rüzgar_hızı']}
📊 Basınç: {weather_info['basınç']}
☀️ UV İndeksi: {weather_info['uv_indeksi']}
🌧️ Yağış: {weather_info['yağış']}"""
        
        return result
        
    except Exception as e:
        return f"Koordinat bazlı hava durumu bilgisi alınırken hata oluştu: {str(e)}"
