x=input("Indique el año a evaluar")
year=int(x)
if year<1900 or year>2199:
    print("Este año está fuera del rango de evaluación")
else:
    if year%4==0 and not (year%100==0 and not (year%400==0)):
        print("El año "+x+" es bisiesto.")
    else: 
        print("El año "+x+" no es bisiesto.")
q_leap=0
year_to_evaluate=1900
while year_to_evaluate<=year:
    if year_to_evaluate%4==0 and not (year_to_evaluate%100==0 and not (year%400==0)):
        q_leap+=1
        year_to_evaluate+=4
    else: 
        year_to_evaluate+=1
q_leap_2=str(q_leap)
print("La cantidad de años bisiestos entre 1900 y "+x+" es "+q_leap_2+".")
quit()                                                                                                                                                          