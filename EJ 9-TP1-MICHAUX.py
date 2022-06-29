def no_cadena(str):
  global palabra
  cadena=True
  texto=True
  if texto:
      if str[0:2]=="no":
          cond1 =str
          palabra=cond1
      else:
          cond2="no "+str
          palabra=cond2
      return print("su palabra es",palabra)

def consignas():
    consigna1 = str(input("Ingrese una palabra: "))
    no_cadena(consigna1)
consignas()









