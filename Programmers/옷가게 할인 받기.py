def solution(price):
    # answer = 0
    # if 10 <= price < 100000:
    #     answer = price
    # elif price >= 500000:
    #     answer = price / (100/80)
    # elif 500000 > price >= 300000:
    #     answer = price / (100/90)
    # elif 300000 > price >= 100000:
    #     answer = price / (100/95)
    # else:
    #     answer = price
    temp = 1
    if price >= 500000:
        temp = 0.8
    elif price >= 300000:
        temp = 0.9
    elif price >= 100000:
        temp = 0.95
    return int(price * temp)


    
