import torch
from pathlib import Path
from ultralytics import YOLO
from multiprocessing import freeze_support
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

def main():
    # 경로 설정
    img_path = Path("images/train/")
    label_path = Path("labels/train/")

    # data.yaml 파일 경로
    data_yaml_path = 'data.yaml'

    # 모델 초기화
    model = YOLO('yolov8n.pt')

    # 학습 시작
    model.train(data=data_yaml_path, epochs=3, batch=16, imgsz=640, device=0)

    result = model.predict(source='./images/test', save=True)
    

if __name__ == '__main__':
    freeze_support()
    main()
