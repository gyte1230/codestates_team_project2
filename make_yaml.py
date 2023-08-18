import yaml

# 데이터 설정
class_names = ["오토바이 탑승자", "오토바이 탑승자(보행자도로 통행 위반)", "오토바이 탑승자(안전모 미착용 위반)", "오토바이 탑승자(무단횡단 위반)", "오토바이 탑승자(신호 위반)", "오토바이 탑승자(정지선 위반)", "오토바이 탑승자(횡단보도 주행 위반)",
               "자전거 탑승자", "자전거 캐리어", "자전거 탑승자(보행자도로 통행 위반)", "자전거 탑승자(안전모 미착용 위반)", "자전거 탑승자(무단횡단 위반)", "자전거 탑승자(신호 위반)", "자전거 탑승자(정지선 위반)", "자전거 탑승자(횡단보도 주행 위반)",
               "킥보드 탑승자", "킥보드 캐리어", "킥보드 탑승자(보행자도로 통행 위반)", "킥보드 탑승자(안전모 미착용 위반)", "킥보드 탑승자(무단횡단 위반)", "킥보드 탑승자(신호 위반)", "킥보드 탑승자(횡단보도 주향 위반)", "킥보드 탑승자(동승자 탑승 위반)"]  
train_images_path = "./images/train/"
val_images_path = "./images/val/"

# YOLO용 .yaml 파일 내용 설정
data = {
    "train": train_images_path,
    "val": val_images_path,
    "nc": len(class_names),
    "names": class_names
}

# 파일에 쓰기
with open("data.yaml", "w") as f:
    yaml.dump(data, f)

print("data.yaml has been created!")
