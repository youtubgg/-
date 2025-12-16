time = input("Введите время:")
kolvo = time.count(" ")
if kolvo != 0:
    ind = time.index(" ")
if kolvo != 1:
    print("Неверный ввод")
else:
    if time[0:ind].isdigit() == False or time[ind:len(time)].isdigit() == False:
        print("Неверный ввод")
    else:
        hours = int(time[0:ind])
        minutes = int(time[ind:len(time)])
        if not (0 <= hours <= 23):
             print("Введены недопустимые данные: часы должны быть от 0 до 23.")
        elif not (0 <= minutes <= 59):
             print("Введены недопустимые данные: минуты должны быть от 0 до 59.")
        else:
            if hours == 0 and minutes == 0:
                print("полночь")
            elif hours == 12 and minutes == 0:
                print("полдень")
            else:
                if 0 <= hours < 6:
                    period = "ночи"
                elif 6 <= hours < 12:
                    period = "утра"
                elif 12 <= hours < 18:
                    period = "дня"
                else:
                    period = "вечера"
                display_hours = hours if hours <= 12 else hours - 12
                if display_hours == 0:
                    display_hours = 12
                if display_hours == 1:
                    hour_word = "час"
                elif 2 <= display_hours <= 4:
                    hour_word = "часа"
                else:
                    hour_word = "часов"
                result = f"{display_hours} {hour_word}"
                if minutes > 0:
                    if minutes == 1:
                        minute_word = "минута"
                    elif 2 <= minutes <= 4:
                        minute_word = "минуты"
                    else:
                        minute_word = "минут"
                    result += f" {minutes} {minute_word}"
                result += f" {period}"
                if minutes == 0:
                    result += " ровно"
                print(result)
