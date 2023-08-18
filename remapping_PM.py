import os
import json

# PM_code의 재매핑 딕셔너리를 정의합니다.
remapping_dict = {13: 0, 14: 1, 15: 2, 16: 3, 17: 4, 18: 5, 19: 6, 20: 7, 21: 8,
                 22: 9, 23: 10, 24: 11, 25: 12, 26: 13, 27: 14, 28: 15, 29: 16, 
                 30: 17, 31: 18, 32: 19, 33: 20, 35: 21, 36: 22}

json_folder_path = 'labels_json'

for json_file in os.listdir(json_folder_path):
    if json_file.endswith(".json"):
        with open(os.path.join(json_folder_path, json_file), 'r') as file:
            data = json.load(file)
            
            pm_annotations = data["annotations"]["PM"]
            for annotation in pm_annotations:
                current_code = int(annotation["PM_code"])
                
                # 재매핑 딕셔너리에서 새 코드를 찾습니다.
                if current_code in remapping_dict:
                    annotation["PM_code"] = remapping_dict[current_code]
                else:
                    print(f"Unexpected PM_code {current_code} in {json_file}")

        # 변경된 데이터로 JSON 파일을 다시 저장합니다.
        with open(os.path.join(json_folder_path, json_file), 'w') as file:
            json.dump(data, file, indent=4)
