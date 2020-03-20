"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★

예시
<입력>
숫자를 입력하세요 : 5

<출력>
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★


"""
try:
    N = int(input('숫자를 입력하세요 : '))
except ValueError:
    print("정수가 아닙니다.")
    exit()

for j in range(N):
    for i in range(N-j-1):
        print(" ", end='')
    for i in range(j+1):
        print("★", end='')
    print('')
for j in range(N):
    for i in range(j+1):
        print(" ", end='')
    for i in range(N-j-1):
        print("★", end='')
    print('')