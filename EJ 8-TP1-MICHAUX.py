def pos_negative(a,b,negativa):
  global negacion
  val1 = True
  val2 = True
  con3= True
  valores = (val1 or val2)
  if negativa == "falso":
     con3 = False
  elif negativa == "verdadero":
      con3 = True
  if valores:
      if (a<0 or b<0) and (a>0 or b>0):
        cond1 = (True)
        negacion = (cond1)
      elif a or b<0:
          con2=(True)
          negacion = (con2)
      elif not (a<0 or b<0) and (a>0 or b>0) and not a or b<0 and not negativa=="verdadero":
          cond3=(False)
          negacion = (cond3)
      return print("Su resultado es: ", negacion)

def consignas():
    consigna1 = int(input("Ingrese el primer valor: "))
    consigna2 = int(input("Ingrese el segundo valor:"))
    consigna3 = str(input("El parametro negativa es verdadero o falso?:"))
    pos_negative(consigna1,consigna2,consigna3)
consignas()

