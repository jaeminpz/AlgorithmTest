from operator import truediv

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def get_max_discounted_price(prices,coupons):
    coupons.sort(reverse=True)
    prices.sort(reverse=True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price








def get_max_discounted_price_my(prices, coupons):
    # 이 곳을 채워보세요!
    # 가장 높은 가격과 가장 높은 할인 쿠폰을 적용시켜 sum 값을 모은다.
    # 각 배열을 내림차순으로 정렬
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    prices_len = min(len(prices),len(coupons))
    sum = 0
    for i in range(prices_len):
        if prices[i] is not None and coupons[i] is not None:
            sum += prices[i] * (100-coupons[i]) // 100

    for i in range(prices_len, len(prices)):
        sum += prices[i]

    return sum






print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))