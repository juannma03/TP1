def problema_loro(hablando,hora):
  global despertar
  charla=True
  tiempo=True
  if hablando=="si":
      charla=True
  elif hablando=="no":
      charla= False
  if hora<7:
      tiempo=True
  elif hora>20:
       tiempo=True
  else:
       print("Tienes que ingresar una hora,ingresa nuevamente:")
       consignas()

  if charla and tiempo:
       despertar= True
  elif charla and not tiempo:
       despertar = False
  elif not charla and tiempo:
       despertar= False
  elif not charla and not tiempo:
       despertar= True
  return print(despertar)


def consignas():
    consigna1 = str(input("Esta hablando el mono?: "))
    consigna2 = int(input("Que hora es?:"))
    problema_loro(consigna1,consigna2)
consignas()


