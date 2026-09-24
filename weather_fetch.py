"""
서울 강남구 날씨 & 미세먼지 자동 수집 스크립트
출처: Open-Meteo (https://open-meteo.com) — 무료, API 키 불필요
저장: C:/claude-work/weather.txt
"""

import urllib.request
import json
from datetime import datetime

# 서울 강남구 좌표
LAT = 37.5172
LON = 127.0473
OUTPUT_FILE = "C:/claude-work/weather.txt"

WEATHER_CODES = {
    0: "맑음", 1: "대체로 맑음", 2: "부분적으로 흐림", 3: "흐림",
    45: "안개", 48: "안개(결빙)",
    51: "이슬비(약)", 53: "이슬비", 55: "이슬비(강)",
    61: "비(약)", 63: "비", 65: "비(강)",
    71: "눈(약)", 73: "눈", 75: "눈(강)",
    80: "소나기(약)", 81: "소나기", 82: "소나기(강)",
    95: "뇌우", 99: "뇌우(우박)"
}

def fetch_json(url):
    with urllib.request.urlopen(url, timeout=10) as res:
        return json.loads(res.read().decode("utf-8"))

def dust_grade(pm10, pm25):
    """미세먼지 등급 판정 (환경부 기준)"""
    if pm10 <= 30:      g10 = "좋음"
    elif pm10 <= 80:    g10 = "보통"
    elif pm10 <= 150:   g10 = "나쁨"
    else:               g10 = "매우나쁨"

    if pm25 <= 15:      g25 = "좋음"
    elif pm25 <= 35:    g25 = "보통"
    elif pm25 <= 75:    g25 = "나쁨"
    else:               g25 = "매우나쁨"

    return g10, g25

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    try:
        # 날씨 데이터
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={LAT}&longitude={LON}"
            f"&current=temperature_2m,apparent_temperature,"
            f"relative_humidity_2m,wind_speed_10m,weather_code"
            f"&timezone=Asia%2FSeoul"
        )
        w = fetch_json(weather_url)["current"]

        # 대기질 데이터
        air_url = (
            f"https://air-quality-api.open-meteo.com/v1/air-quality"
            f"?latitude={LAT}&longitude={LON}"
            f"&current=pm10,pm2_5,us_aqi"
            f"&timezone=Asia%2FSeoul"
        )
        a = fetch_json(air_url)["current"]

        sky     = WEATHER_CODES.get(w["weather_code"], f"코드:{w['weather_code']}")
        pm10_g, pm25_g = dust_grade(a["pm10"], a["pm2_5"])

        output = f"""{'=' * 50}
서울 강남구 날씨 & 미세먼지  |  {now}
{'=' * 50}
[날씨]
  날씨 상태  : {sky}
  기온       : {w['temperature_2m']}°C  (체감 {w['apparent_temperature']}°C)
  습도       : {w['relative_humidity_2m']}%
  풍속       : {w['wind_speed_10m']} km/h

[미세먼지]
  PM10       : {a['pm10']:.1f} μg/m³  ({pm10_g})
  PM2.5      : {a['pm2_5']:.1f} μg/m³  ({pm25_g})
  AQI        : {a['us_aqi']}

출처: Open-Meteo (api.open-meteo.com)

"""

        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(output)

        print(f"[{now}] 저장 완료 → {OUTPUT_FILE}")

    except Exception as e:
        error_msg = f"[{now}] 오류 발생: {e}\n"
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(error_msg)
        print(f"오류: {e}")

if __name__ == "__main__":
    main()
