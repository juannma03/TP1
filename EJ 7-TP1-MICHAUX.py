def cerca_cien(n):
  global calculo
  val1 = True
  val2 = True
  valores = (val1 or val2)
  if valores:
      if n>=0 and n<=10:
        cond1 = (True)
        calculo = (cond1)
      elif n>=90 and n<=100:
          con2=(True)
          calculo = con2
      elif n>=190 and n<=200:
          con3=(True)
          calculo = (con3)
      elif not  (n>=0 and n<=10) and not (n>=90 and n<=100) and not (n>=190 and n<=200):
         cond4=(False)
         calculo = (cond4)
      return print("Su resultado es: ", calculo)
def consignas():
    consigna1 = int(input("Ingrese un numero entero: "))
    cerca_cien(consigna1)
consignas()

