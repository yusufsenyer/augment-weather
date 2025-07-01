#!/usr/bin/env python3
"""
MCP Server'ı lokal olarak test etmek için basit script
"""

import asyncio
from app import get_current_weather_by_city, get_current_weather_by_coordinates

async def test_weather_functions():
    """Hava durumu fonksiyonlarını test et"""
    
    print("🧪 Weather MCP Server Test Başlıyor...\n")
    
    # Test 1: Şehir adı ile hava durumu
    print("📍 Test 1: İstanbul hava durumu")
    print("-" * 50)
    try:
        istanbul_weather = get_current_weather_by_city("Istanbul")
        print(istanbul_weather)
        print("✅ İstanbul testi başarılı!\n")
    except Exception as e:
        print(f"❌ İstanbul testi başarısız: {e}\n")
    
    # Test 2: Farklı şehir
    print("📍 Test 2: Ankara hava durumu")
    print("-" * 50)
    try:
        ankara_weather = get_current_weather_by_city("Ankara")
        print(ankara_weather)
        print("✅ Ankara testi başarılı!\n")
    except Exception as e:
        print(f"❌ Ankara testi başarısız: {e}\n")
    
    # Test 3: Koordinat ile hava durumu
    print("📍 Test 3: Koordinat ile hava durumu (İstanbul)")
    print("-" * 50)
    try:
        coord_weather = get_current_weather_by_coordinates(41.0082, 28.9784)
        print(coord_weather)
        print("✅ Koordinat testi başarılı!\n")
    except Exception as e:
        print(f"❌ Koordinat testi başarısız: {e}\n")
    
    # Test 4: Hatalı şehir adı
    print("📍 Test 4: Hatalı şehir adı")
    print("-" * 50)
    try:
        error_test = get_current_weather_by_city("XYZInvalidCity123")
        print(error_test)
        print("✅ Hata yönetimi testi başarılı!\n")
    except Exception as e:
        print(f"❌ Hata yönetimi testi başarısız: {e}\n")
    
    print("🎉 Tüm testler tamamlandı!")

def test_mcp_tools():
    """MCP araçlarını simüle et"""
    
    print("\n🔧 MCP Araçları Simülasyonu")
    print("=" * 60)
    
    # MCP tool simülasyonu
    async def simulate_get_weather_by_city(city_name: str):
        """get_weather_by_city aracını simüle et"""
        return get_current_weather_by_city(city_name)
    
    async def simulate_get_weather_by_coordinates(latitude: float, longitude: float):
        """get_weather_by_coordinates aracını simüle et"""
        return get_current_weather_by_coordinates(latitude, longitude)
    
    # Test senaryoları
    test_cases = [
        ("get_weather_by_city", "London"),
        ("get_weather_by_city", "Tokyo"),
        ("get_weather_by_coordinates", 40.7128, -74.0060),  # New York
        ("get_weather_by_coordinates", 48.8566, 2.3522),    # Paris
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🧪 MCP Test {i}:")
        print("-" * 30)
        
        if test_case[0] == "get_weather_by_city":
            city = test_case[1]
            print(f"Tool: get_weather_by_city")
            print(f"Parameter: city_name = '{city}'")
            print("Response:")
            try:
                result = asyncio.run(simulate_get_weather_by_city(city))
                print(result)
                print("✅ Başarılı")
            except Exception as e:
                print(f"❌ Hata: {e}")
        
        elif test_case[0] == "get_weather_by_coordinates":
            lat, lon = test_case[1], test_case[2]
            print(f"Tool: get_weather_by_coordinates")
            print(f"Parameters: latitude = {lat}, longitude = {lon}")
            print("Response:")
            try:
                result = asyncio.run(simulate_get_weather_by_coordinates(lat, lon))
                print(result)
                print("✅ Başarılı")
            except Exception as e:
                print(f"❌ Hata: {e}")

if __name__ == "__main__":
    # Ana test fonksiyonunu çalıştır
    asyncio.run(test_weather_functions())
    
    # MCP araçları simülasyonu
    test_mcp_tools()
    
    print("\n" + "="*60)
    print("🚀 MCP Server'ınız hazır!")
    print("Çalıştırmak için: python server.py")
    print("="*60)
