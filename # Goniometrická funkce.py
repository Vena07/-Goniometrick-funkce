# Goniometrická funkce
import math
option1 = False
option2 = False

úhly = range(1, 360)

funkce = [(úhel, math.sin(math.radians(úhel)), math.cos(math.radians(úhel)), math.tan(math.radians(úhel))) for úhel in úhly]
print("Goniometrická funkce")
výběr1 = str(input("Vyberet si goniometrická funkci (sin / cos / tan): "))
while option1== False:
    if výběr1 == "sin":
     option1 = True
     a = int(input("Vyberte hodnotu pro stranu a: "))
     c = int(input("Vyberte hodnotu pro stranu c: "))
     if a <= 0 and c <= 0 :
       print("Nesmí být negativní hodnota!!")
     else:
       výsledek1 = a/c
       výsledek2 = math.degrees(math.asin(výsledek1))
       print(f"Úhel má velikost : {výsledek2}°")
    
    
    
    elif výběr1 == "cos":
     option1 = True
     b = int(input("Vyberte hodnotu pro stranu b: "))
     c = int(input("Vyberte hodnotu pro stranu c: "))
     if b <= 0 and c <= 0 :
       print("Nesmí být negativní hodnota!!")
     else:
       výsledek1 = b/c
       výsledek2 = math.degrees(math.acos(výsledek1))
       print(f"Úhel má velikost : {výsledek2}°")
    
    
    
    
    
    elif výběr1 == "tan":
     option1 = True
     a = int(input("Vyberte hodnotu pro stranu a: ")) 
     b = int(input("Vyberte hodnotu pro stranu b: "))
     if a <= 0 and b <= 0 :
       print("Nesmí být negativní hodnota!!")
     else:
       výsledek1 = a/b
       výsledek2 = math.degrees(math.atan(výsledek1))
       print(f"Úhel má velikost : {výsledek2}°")