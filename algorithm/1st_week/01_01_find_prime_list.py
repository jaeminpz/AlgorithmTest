input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    # 1과 자기자신만 있는게 소수
    primeLis  =[]
    for i in range(2,number):
        count =0
        for j in range(2,i):  # i = 3, j 2~2 자기자신 빼고 count 가 안되도록 코드
            if i % j == 0:
                count +=1
        if count == 0:
            primeLis.append(i)

    return primeLis


result = find_prime_list_under_number(input)
print(result)