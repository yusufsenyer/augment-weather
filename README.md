# 🌤️ Weather MCP Server

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org) [![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io) [![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://docker.com) [![Smithery](https://img.shields.io/badge/Smithery-Deploy%20Ready-orange.svg)](https://smithery.ai)

**Open-Meteo API kullanarak hava durumu bilgisi sağlayan MCP server**

_Smithery.ai ile tek tıkla deploy edin!_

## ✨ Özellikler

- 🌍 **Şehir Adı ile Hava Durumu** - İstanbul, Ankara, London gibi şehir adları ile sorgulama
- 📍 **Koordinat ile Hava Durumu** - Enlem/boylam koordinatları ile detaylı bilgi
- 🆓 **Tamamen Ücretsiz** - Open-Meteo API kullanır, API key gerektirmez
- 🚀 **Smithery Ready** - Tek tıkla deploy
- 🐳 **Docker Desteği** - Konteyner olarak çalıştırma
- 🇹🇷 **Türkçe Destek** - Hava durumu açıklamaları Türkçe

## 🎯 Hızlı Başlangıç

### 1. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 2. Server'ı Çalıştırın

```bash
python server.py
```

### 3. Test Edin

Server çalışmaya başladığında MCP protokolü üzerinden hava durumu sorgulayabilirsiniz!

## 🛠️ Kullanılabilir Araçlar

### `get_weather_by_city`
Şehir adına göre hava durumu bilgisi getirir.

**Parametreler:**
- `city_name` (string): Şehir adı (örn: "Istanbul", "Ankara", "London")

**Örnek Kullanım:**
```
İstanbul'un hava durumu nasıl?
```

### `get_weather_by_coordinates`
Koordinatlara göre hava durumu bilgisi getirir.

**Parametreler:**
- `latitude` (float): Enlem değeri (örn: 41.0082)
- `longitude` (float): Boylam değeri (örn: 28.9784)

**Örnek Kullanım:**
```
41.0082, 28.9784 koordinatlarının hava durumu nasıl?
```

## 🚀 Deploy

### Smithery.ai ile Deploy

1. Bu repository'yi GitHub'a push edin
2. [Smithery.ai](https://smithery.ai) hesabınıza giriş yapın
3. Repository'nizi bağlayın
4. Tek tıkla deploy edin! 🎉

### Docker ile Deploy

```bash
# Container'ı build edin
docker build -t weather-mcp-server .

# Container'ı çalıştırın
docker run weather-mcp-server
```

### Manuel Deploy

```bash
pip install -r requirements.txt
python server.py
```

## 📊 Hava Durumu Bilgileri

Server aşağıdaki bilgileri sağlar:

- 🌡️ **Sıcaklık** - Güncel sıcaklık (°C)
- 🌡️ **Hissedilen Sıcaklık** - Gerçek hissedilen sıcaklık
- ☁️ **Hava Durumu** - Açık, bulutlu, yağmurlu vb.
- 💧 **Nem Oranı** - Bağıl nem (%)
- 💨 **Rüzgar Hızı** - km/h cinsinden
- 📊 **Atmosfer Basıncı** - hPa cinsinden
- ☀️ **UV İndeksi** - Güneş ışınları şiddeti
- 🌧️ **Yağış Miktarı** - mm cinsinden

## 🔧 Konfigürasyon

`.env` dosyasında aşağıdaki ayarları yapabilirsiniz:

```env
# MCP Server Name (opsiyonel)
MCP_SERVER_NAME=weather-mcp-server

# Log Level (opsiyonel)
LOG_LEVEL=INFO
```

## 📱 Mobil Uygulama Entegrasyonu

Bu MCP server'ı mobil uygulamanızda kullanmak için:

1. MCP client kütüphanesini mobil uygulamanıza entegre edin
2. Server'ın endpoint'ini yapılandırın
3. `get_weather_by_city` veya `get_weather_by_coordinates` araçlarını çağırın

## 🤝 Katkıda Bulunma

1. Repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🌟 Destek

Bu proje işinize yaradıysa:

- ⭐ **Star verin** - Mutlu oluruz! 😊
- 🐦 **Paylaşın** - Diğer geliştiricilerle paylaşın
- 🛠️ **Katkıda bulunun** - Topluluk için geliştirmeler yapın

---

**Open-Meteo API ile güçlendirilmiştir** 🚀
