import random

def shop():
    money = random.randint(0, 120)
    print(f"Вова получил {money} рублей на карманные расходы.")

    while money > 0:
        print(f"У Вовы осталось {money} рублей.")
        choice = input("Что будешь покупать? (вода, шоколадка, сок, выход): ").lower()

        if choice == 'выход':
            print("Вова выходит из магазина.")
            break
        elif choice in ['вода', 'шоколадка', 'сок']:
            if choice == 'вода' and money >= 20:
                money -= 20
                print("Вова купил воду за 20 рублей.")
            elif choice == 'шоколадка' and money >= 40:
                money -= 40
                print("Вова купил шоколадку за 40 рублей.")
            elif choice == 'сок' and money >= 60:
                money -= 60
                print("Вова купил сок за 60 рублей.")
            else:
                print("Не хватает денег на покупку.")
        else:
            print("Такого товара нет в магазине. Попробуй ещё раз.")

shop()
