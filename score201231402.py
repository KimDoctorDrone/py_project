 
def average():                                          #과제의 평균값 구하기
    s = 0
    n = int(input("과제의 갯수는: "))

    for i in range(1,n+1):                              #합계 누적하기
        a = float(input("%d번째 과제의 점수: "%(i)))
        s+=a                                            #s=s+a

   
    
    mid = int(input("중간고사 성적을 입력해주세요?"))

    fin = int(input("기말고사 성적을 입력해주세요?"))
    


    H = a * 0.4                                         #비율 지정

    M = mid * 0.3

    F = fin * 0.3



    score = H + M + F                                   #등급 정하기
    if 100 >= score >= 90:
        grade = "A"
    elif 90 > score >= 80:
        grade = "B"
    elif 80 > score >= 70:
        grade = "C"
    elif 70 > score >= 60:
        grade = "D"
    elif score < 60:
        grade = "F"
    
    
    print("\n총점이 %d점이므로"%s)
    print("과제의 평균은 %.2f점입니다."%(s/n))
    
    print("과제 반영점수(40%)" , H, "중간 반영점수(30%)" , M, "기말 반영점수(30%)" , F)
    print("성적은" + grade + "입니다.")

average()                                               #실행
