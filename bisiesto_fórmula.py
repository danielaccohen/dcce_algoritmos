year=int(input("Indique el año a evaluar"))
if year<1900 or year>2199:
    print("Este año está fuera del rango de evaluación")
else:
    if year%4==0 and not (year%100==0 and not (year%400==0)):
        print("El año "+str(year)+" es bisiesto.")
    else: 
        print("El año "+str(year)+" no es bisiesto.")
def es_bisiesto(year_new):
        return (year_new % 4 == 0 and (year_new % 100 != 0 or year_new % 400 == 0))
q_leap = ((year - 1900) // 4) - ((year - 1900) // 100) + ((year - 1900) // 400)
print(f"El número de años bisiestos hasta {year} es {q_leap}.")
quit()