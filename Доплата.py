def season_of_year(month, day):
    if month < 1 or month > 12:
        return "Месяц должен быть от 1 до 12"
    
    if day < 1 or day > 31:
        return "День должен быть от 1 до 31"
    
    if month == 2 and day > 28:  
        return "В феврале не может быть больше 28 дней!"
    
    if month == 4 and day > 30:  
        return "В апреле не может быть больше 30 дней!"
    
    if month == 6 and day > 30:  
        return "В июне не может быть больше 30 дней!"
    
    if month == 9 and day > 30:  
        return "В сентябре не может быть больше 30 дней!"
    
    if month == 11 and day > 30:  
        return "В ноябре не может быть больше 30 дней!"
    
    
    if month == 12 or month == 1 or month == 2:
        return "Зима"
    
    
    if month == 3 or month == 4 or month == 5:
        return "Весна"
    
    
    if month == 6 or month == 7 or month == 8:
        return "Лето"
    
    
    if month == 9 or month == 10 or month == 11:
        return "Осень"
month = int(input("Введите месяц:"))
day = int(input("Введите день:"))
print(season_of_year(month, day))
    
