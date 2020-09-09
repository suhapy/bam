#coffesales.py

americano_price=2000
cafrlatte_price=3000
capucino_price=3500

#판매개수를 input()함수로 입력 받는다.
americanos=int(input("아메리카노 판매개수:"))
cafelattes=int(input("카페라테 판매개수:"))
capucinos=int(input("카푸치노 판매기수:"))

#매출계산
sales = americano_price * americanos
sales = sales + cafrlatte_price * cafelattes
sales = sales + capucino_price * capucinos

print("총매출은",sales,"원 입니다.")