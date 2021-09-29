from random import randint
p=input("parit")
x=randint(1,6)
print("l'ordinateur a choix.",x)
if((x%2==0)and(p.upper()=="P"))or((x%2==1)and(p.upper()=="I")):
    print("gagnant")
else:
    print("perdant")
    
