top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    # 레이저 방향은 오른쪽에서 왼쪽으로
    # 자신보다 높은 곳에서 index 출력
    # 뒤 배열부터 돌아서 앞으로 간다

    index =[0] * len(heights)

    for i in range(len(heights)-1,0,-1):
        for j in range(i-1, -1, -1):
            if heights[i] <= heights[j]:
                index[i] = j+1
                break
    return index


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))