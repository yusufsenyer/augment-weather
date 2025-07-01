from mcp.server.fastmcp import FastMCP
from app import get_current_weather_by_city, get_current_weather_by_coordinates

# Initialize MCP server
mcp = FastMCP("weather-mcp-server")

@mcp.tool()
async def get_weather_by_city(city_name: str) -> str:
    """
    Şehir adına göre güncel hava durumu bilgisini getirir.
    
    Args:
        city_name: Hava durumu bilgisi istenen şehir adı (örn: "Istanbul", "Ankara", "London")
    
    Returns:
        Detaylı hava durumu bilgisi (sıcaklık, nem, rüzgar, basınç vb.)
    """
    weather_response = get_current_weather_by_city(city_name)
    return weather_response

@mcp.tool()
async def get_weather_by_coordinates(latitude: float, longitude: float) -> str:
    """
    Koordinatlara göre güncel hava durumu bilgisini getirir.
    
    Args:
        latitude: Enlem değeri (örn: 41.0082)
        longitude: Boylam değeri (örn: 28.9784)
    
    Returns:
        Detaylı hava durumu bilgisi (sıcaklık, nem, rüzgar, basınç vb.)
    """
    weather_response = get_current_weather_by_coordinates(latitude, longitude)
    return weather_response

if __name__ == "__main__":
    mcp.run(transport="stdio")
