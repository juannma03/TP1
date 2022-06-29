def caracter_perdido(n,str):
  global perdida

  if n or n == 0:
          mitad1 = str[:n]
          mitad2 = str[n + 1:]
          cond1=mitad1 + mitad2
          perdida=cond1
  elif n == -1:
          cond2= str[:-1]
          perdida=cond2
  return perdida
def consignas():
    consigna1 = str(input("Ingrese una palabra:"))
    consignas2= int(input("Ingrese un indice:"))
    caracter_perdido(consigna1,consignas2)
consignas()

