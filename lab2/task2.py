
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.03  # Ежемесячный рост цен


month = 0
money_capital = 0

while month < 10:
    dengi = spend - salary
    money_capital += dengi
    month += 1
    spend = spend * (1+increase)

print("Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", round(money_capital))