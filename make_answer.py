import os
import json

def convert_bbox_to_yolo_format(points, img_width, img_height):
    x_center = (points[0] + points[2] / 2) / img_width
    y_center = (points[1] + points[3] / 2) / img_height
    width = points[2] / img_width
    height = points[3] / img_height
    return x_center, y_center, width, height

# 모든 JSON 파일을 순회하기 위한 디렉토리 경로
json_folder_path = 'labels_json'
labels_folder_path = 'labels'

# 'labels' 폴더가 없으면 생성
if not os.path.exists(labels_folder_path):
    os.makedirs(labels_folder_path)

for json_file in os.listdir(json_folder_path):
    if json_file.endswith(".json"):
        with open(os.path.join(json_folder_path, json_file), 'r') as file:
            data = json.load(file)
            
            img_width = data["description"]["imageWidth"]
            img_height = data["description"]["imageHeight"]

            # 결과를 저장할 .txt 파일을 생성/열기
            output_filename = os.path.splitext(json_file)[0] + '.txt'
            with open(os.path.join(labels_folder_path, output_filename), 'w') as txt_file:
                pm_annotations = data["annotations"]["PM"]
                for annotation in pm_annotations:
                    pm_code = int(annotation["PM_code"])
                    shape_type = annotation["shape_type"]

                    if shape_type == "bbox":
                        x_center, y_center, width, height = convert_bbox_to_yolo_format(annotation["points"], img_width, img_height)
                        txt_file.write(f"{pm_code} {x_center} {y_center} {width} {height}\n")
