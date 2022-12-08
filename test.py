import datetime
now = datetime.datetime.now()
hour = now.hour


if hour > 0 and hour <=6:
    print("Доброе ночи!")

elif hour > 6 and hour <=12:
    print("Доброе утро!")

elif hour > 12 and hour <=18:
    print("Добрый день!")

elif hour >18 and  hour <=24:
    print("Добрый вечер!")
    
    # закончили
