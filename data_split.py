import os
import shutil
import random

def ensure_directory_exists(dir_path):
    """지정된 경로의 디렉터리가 존재하지 않으면 생성합니다."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def move_files_by_format(file_list, source_folder, train_folder, val_folder, test_folder, extension):
    ensure_directory_exists(train_folder)
    ensure_directory_exists(val_folder)
    ensure_directory_exists(test_folder)

    for f in file_list['train']:
        shutil.move(os.path.join(source_folder, f + extension), os.path.join(train_folder, f + extension))
    for f in file_list['val']:
        shutil.move(os.path.join(source_folder, f + extension), os.path.join(val_folder, f + extension))
    for f in file_list['test']:
        shutil.move(os.path.join(source_folder, f + extension), os.path.join(test_folder, f + extension))

# 원본 폴더 경로
img_source_folder = './images'
txt_source_folder = './labels'

img_files = {f.split('.')[0] for f in os.listdir(img_source_folder) if f.endswith('.jpg') or f.endswith('.png')}
txt_files = {f.split('.')[0] for f in os.listdir(txt_source_folder) if f.endswith('.txt')}

# 이미지와 텍스트 파일 모두에 존재하는 파일만 선택
common_files = list(img_files & txt_files)

random.shuffle(common_files)

train_ratio = 0.7
val_ratio = 0.2
train_size = int(len(common_files) * train_ratio)
val_size = int(len(common_files) * val_ratio)

train_files = common_files[:train_size]
val_files = common_files[train_size:train_size + val_size]
test_files = common_files[train_size + val_size:]

move_files_by_format({
    'train': train_files,
    'val': val_files,
    'test': test_files
}, img_source_folder, './images/train', './images/val', './images/test', '.jpg')

move_files_by_format({
    'train': train_files,
    'val': val_files,
    'test': test_files
}, txt_source_folder, './labels/train', './labels/val', './labels/test', '.txt')
