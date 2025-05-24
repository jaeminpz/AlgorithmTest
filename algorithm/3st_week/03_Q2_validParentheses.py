#강의
def is_correct_parenthesis(string):
    # 구현해보세요!
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")
        elif string[i] == "(":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))




#my
def is_correct_parenthesis(string):
    # 구현해보세요!
    # 첫번째에 ) 마지막에 ( 가 나오면 False
    # 그게 아니면 ( 횟수와 ) 횟수가 같으면 True
    length = len(string)
    balance = 0
    for ch in string:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1

        if balance < 0:
            return False
    return balance == 0



print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
print(is_correct_parenthesis("())("))