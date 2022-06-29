def suma_doble(a,b):
  global suma
  val1 = True
  val2 = True
  valores = (val1 or val2)
  if valores:
      if a<b:
        cond1 = (b+ a)
        suma = (cond1)
      elif b<a:
          con2=(b+a)
          suma = (con2)
      elif not  a>b and not b<a:
          cond3=((b + a) * 2)
          suma = (cond3)
      return print("Su resultado es: ", suma)
def consignas():
    consigna1 = int(input("Ingrese el primer valor: "))
    consigna2 = int(input("Ingrese el segundo valor:"))
    suma_doble(consigna1,consigna2)
consignas()



