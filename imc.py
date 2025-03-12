peso = float(input("digite seu peso "))
altura = float(input("digite sua alturar"))
imc = peso / (altura * altura)
if(imc <1.65):
     print("desnutrido" , imc)
if(imc <=24.5):
    print("normal" , imc)
if(imc< 20.7):
     print("sobre peso" , imc)
else: 
     print("obeso" , imc)