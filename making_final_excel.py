import os
import pandas as pd

# 폴더 경로 설정
data_folder = 'data_preprocessed'

# data_folder 내의 모든 엑셀 파일 리스트
excel_files = [f for f in os.listdir(data_folder) if f.endswith('.xlsx')]

# 각 엑셀 파일에 대해 작업 수행
for excel_file in excel_files:
    file_path = os.path.join(data_folder, excel_file)
    
    # 엑셀 파일 불러오기
    df = pd.read_excel(file_path)
    
    # 'site' 열 생성 및 데이터 추가
    df['site'] = df['item_id'].apply(lambda x: f'https://www.zigbang.com/home/officetel/items/{x}')
    
    # 수정된 데이터프레임을 같은 파일명으로 저장
    df.to_excel(file_path, index=False, engine='openpyxl')

print("작업 완료")
