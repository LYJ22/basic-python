<<<<<<< HEAD
#정수 입력받아 시, 분, 초로 변경, n초 형태
time = int(input("초를 입력:"))
second = time % 60
minute = (time // 60) % 60
hour = (time // 3600)
=======
#정수 입력받아 시, 분, 초로 변경, n초 형태
time = int(input("초를 입력:"))
second = time % 60
minute = (time // 60) % 60
hour = (time // 3600)
>>>>>>> 17108c910fc3e57d0f45d8b91272f53eeee3fcb6
print(hour, "시", minute, "분", second, "초")