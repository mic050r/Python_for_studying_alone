# with 키워드
## with open(문자열: 파일경로, 문자열: 모드) as 파일 객체 :
## 텍스트 읽기 : 파일 객체.read()

# 파일을 엽니다.
with open("basic.txt", "r") as file:
    # 파일을 읽고 출력합니다.
    contents = file.read()
print(contents)