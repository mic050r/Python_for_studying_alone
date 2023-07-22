# 파일 객체 = open(문자열: 파일경로, 문자열: 읽기 모드)
# 파일을 닫을 때는 파일객체.close()

# 파일을 엽니다.
file = open("basic.txt", "w")
# 파일에 텍스트를 씁니다.
file.write("Hello Python Programming...!")

# 파일을 닫습니다.
file.close()