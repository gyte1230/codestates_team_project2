import requests
import urllib.parse
from ultralytics import YOLO
import xml.etree.ElementTree as ET

def main():
    base_url = "https://openapi.its.go.kr:9443/cctvInfo"
    
    params = {
        "apiKey": "test",  # 공개키
        "type": "all",  # 도로유형
        "cctvType": "1",  # CCTV유형
        "minX": "126.800000",  # 최소경도영역
        "maxX": "127.890000",  # 최대경도영역
        "minY": "34.900000",  # 최소위도영역
        "maxY": "35.100000",  # 최대위도영역
        "getType": "xml"  # 출력타입
    }
    
    response = requests.get(base_url, params=params, headers={"Content-type": "text/xml;charset=UTF-8"})
    
    print(f"Response code: {response.status_code}")
    
    if 200 <= response.status_code < 300:
        print(response.text)
    else:
        print(f"Error: {response.text}")
    
    # XML 문자열 파싱
    root = ET.fromstring(response.text)

    # cctvurl 태그 찾기
    cctv_urls = [elem.text for elem in root.findall(".//cctvurl")]

    # source 변수에 저장
    source = cctv_urls[6]

    # Load an official or custom model
    model = YOLO('best_1.pt')  # Load a custom trained model

    # Perform tracking with the model
    results = model.track(source=source, show=True)  # Tracking with default tracker

if __name__ == "__main__":
    main()
