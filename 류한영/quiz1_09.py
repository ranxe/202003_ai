"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F

예시
<입력>
score : 88

<출력>
A

"""
try:
    N = int(input('score : '))
except ValueError:
    print("Not integer.")
    exit()

if 0 <= N & N < 21:
    print("F")
elif 20 < N & N < 41:
    print("D")
elif 40 < N & N < 61:
    print("C")
elif 60 < N & N < 81:
    print("B")
elif 80 < N & N < 101:
    print("A")
else:
    print("Enter only 0 to 100")