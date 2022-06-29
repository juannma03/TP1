def diferencia21(a,b):
  global diferencia
  val1=True
  val2=True
  if b == 21:
      val2 = True
  elif b == 20:
      val2 = False
  if a==int:
     val1 = True
  elif a==str or a== float:
      val1=False
      print("Incorrecto, has ingresado un decimal, por favor ingresa un entero:")
      consignas()
  #else:
   #   val1=False
    #  print("Incorrecto, has ingresado un texto, por favor ingresa un entero:")
     # consignas()

  if val1 and val2:
    if b>a :
       cond1=b-a
       diferencia=(cond1)
    elif b==a:
  #elif val1 and val2 and a==b:
      diferencia=(0)
    return print("Su resultado es: ",diferencia)

def consignas():
    consigna1 =int(input("Ingresa un valor entero:"))
    b = 21
    diferencia21(consigna1,b)
consignas()








