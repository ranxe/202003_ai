number_x = int(input("가로의 숫자를 입력하시오 : "))
number_y = int(input("세로의 숫자를 입력하시오 : "))

for j in range(number_y):
    for i in range(number_x):
        print("★", end='')
    print('')