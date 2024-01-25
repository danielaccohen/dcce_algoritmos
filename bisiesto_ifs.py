year=int(input("Indique el año a evaluar"))
if year<1900 or year>2199:
    print("Este año está fuera del rango de evaluación")
else:
    if year%4==0 and not (year%100==0 and not (year%400==0)):
        print("El año "+str(year)+" es bisiesto.")
    else: 
        print("El año "+str(year)+" no es bisiesto.")
leap_interval = (year - 1900) // 4
leap_interval_100 = (year - 1900) // 100
leap_interval_400 = (year - 1900) // 400
result = leap_interval - leap_interval_100 + leap_interval_400
print("El número de años bisiestos hasta "+str(year)+" es "+str(result)+".")
quit()