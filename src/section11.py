# Section11
# 파이썬 예외처리의 이해
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import pandas as pd
import csv

# 읽기

# 예제1
with open('./resource/sample1.csv', 'r', encoding='cp949') as f:
    reader = csv.reader(f)
    # next(reader) Header 스킵
    # 확인
    print(reader)
    print(type(reader))
    # print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        print(c)

# 예제2 (구분자 설정)
with open('./resource/sample2.csv', 'r', encoding='cp949') as f:
    reader = csv.reader(f, delimiter='|')  # 구분자 선택
    # next(reader) Header 스킵
    # 확인
    print(reader)
    print(type(reader))
    # print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        print(c)

# 예제3 (Dict 변환)
with open('./resource/sample1.csv', 'r', encoding='cp949') as f:
    reader = csv.DictReader(f)  # 딕셔너리 형태로 읽어들임
    # 확인
    print(reader)
    print(type(reader))
    # print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        for k, v in c.items():
            print(k, v, end=' | ')
        print()

print()


# 쓰기

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

with open('./resource/sample3.csv', 'w', newline='') as f:  # newline='' 테스트
    wt = csv.writer(f)
    # print(dir(wt)) # dir 확인
    print(type(wt))
    for v in w:
        wt.writerow(v)

# 예제5
with open('./resource/sample3.csv', 'w') as f:
    wt = csv.writer(f)
    # print(dir(wt)) # dir 확인
    print(type(wt))
    wt.writerows(w)  # 한번에 씀

print()


# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# pip install pandas 설치 필요
# pip install xlrd   설치 필요
# pip install openpyxl 설치 필요

# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등 있으나 pandas를 주로 사용(openpyxl, xlrd) 포함

# 참조 : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html

xlsx = pd.read_excel('./resource/sample.xlsx')
# sheetname='시트명' 또는 숫자(1, 2, 3, ...), header=3(몇 번째 열을 헤더로 지정할 것인지), skiprow=1(스킵할 행) 실습

# 상위 데이터 확인
print(xlsx.head())  # 첫 5줄
print()

# 데이터 확인
print(xlsx.tail())  # 끝 5줄
print()

# 데이터 구조
print(xlsx.shape)  # (20, 7) (행, 열)

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)  # 열에 인덱싱 여부
xlsx.to_csv('./resource/result.csv', index=False)
