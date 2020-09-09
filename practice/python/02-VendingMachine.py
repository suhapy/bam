#Vending Machine.py ==> 자통판매기를 시뮬레이션 하는 프로그램

money = int(input("투입한 돈:"))
price = int(input("물건값:"))

change = money-price
print("거스름돈:",change)

coin500s = change//500 #몫이 500원 동전의 개수
change = change % 500 #500으로 나눈 나머지 계산하는 식
coin100s = change //100 #몫이 100원 동전의 개수

print("500원 동전의 개수:",coin500s)
print("100원 동전의 개수:",coin100s)