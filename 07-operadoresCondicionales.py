day = "friday"
hour = 12  # horario de 24 horas 19horas 7pm 19-2 17-> 7pm 7am -> 7horas
meal = "pizza"

if day == "monday" and hour == 12:
    print(f"we are eating {meal}")
elif day != "monday" or hour != 12:
    print(f"we are eating healthy food")
