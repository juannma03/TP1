Lista_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
def dormimos(dia_semana,vacaciones):
  global dormir
  vac=True
  dia=True
  if vacaciones=="si":
      vac=True
  elif vacaciones=="no":
      vac= False
  if dia_semana in Lista_semana[0:5]:
      dia=True
  elif dia_semana in Lista_semana[5:7]:
       dia=False
  else:
       print("Tienes que ingresar un dia de semana, por favor vuelve intentalo nuevamente")
       consignas()

  if dia and vac:
       dormir= True
  elif dia and not vac:
       dormir = False
  elif not dia and vac:
       dormir= True
  elif not dia and not vac:
       dormir= True
  return print(dormir)


def consignas():
    consigna1 = str(input("Que dia de semana es?: "))
    consigna2 = str(input("Estas de vacaciones?:"))
    dormimos(consigna1,consigna2)
consignas()









