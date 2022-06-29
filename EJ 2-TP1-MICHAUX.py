def problemas_monos(a_sonriendo,b_sonriendo):
  global sonriendo
  mono1=True
  mono2=True
  monos=(mono1 or mono2)
  if mono1 or mono2=="si":
      monos=True
  elif mono1 or mono2=="no":
      monos= False
  else:
       print("Tienes que responder con si o no, por favor vuelve a intentarlo")
       consignas()

  if mono1 and mono2:
       sonriendo= True
  elif mono1 and not mono2:
       sonriendo = False
  elif not mon1 and mono2:
       sonriendo= True
  elif not mono1 and not mono2:
       sonriendo= True
  return print(sonriendo)


def consignas():
    consigna1 = str(input("Esta sonriendo el primer mono?: "))
    consigna2 = str(input("El segundo mono esta sonriendo?: "))
    problemas_monos(consigna1,consigna2)
consignas()



