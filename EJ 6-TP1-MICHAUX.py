def hacer10(a,b):
  global suma
  val1 = True
  val2 = True
  valores = (val1 or val2)
  if valores:
      if a<b:
        cond1 = (True)
        suma = (cond1)
      elif b<a:
          con2=(True)
          suma = (con2)
      elif not  a>b and not a<b:
          cond3=(False)
          suma = (cond3)
      return print("Su resultado es: ", suma)
def consignas():
    consigna1 = int(input("Ingrese el primer valor: "))
    consigna2 = int(input("Ingrese el segundo valor:"))
    hacer10(consigna1,consigna2)
consignas()

