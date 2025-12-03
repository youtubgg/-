tariff = input("Введите тариф (1 час, 2 часа, 5 часов): ")
money = int(input("Введите сумму денег: "))
if tariff != "1 час" and tariff != "2 часа" and tariff != "5 часов":
    print("Неверный тариф")
else:
    if tariff == "1 час":
        cost = 60
    elif tariff == "2 часа":
        cost = 110
    else:  # 5 часов
        cost = 250
    if money < cost:
        print("Недостаточно средств для оплаты выбранного тарифа")
    else:
        change = money - cost
        coins_10 = change // 10
        remainder = change % 10
        coins_5 = remainder // 5
        remainder = remainder % 5
        coins_2 = remainder // 2
        remainder = remainder % 2
        coin_1 = remainder
        print(f"Оплачен тариф '{tariff}'. Ваша сдача: {coins_10} по 10 руб., {coins_5} по 5 руб., {coins_2} по 2 руб., {coin_1} по 1 руб.")
