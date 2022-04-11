def problema_1():
  peperronmike = input("Deme un numero: ")
  alchile = input("Deme otro numero: ")
  if peperronmike == alchile:
   print("Son iguales")
  if peperronmike > alchile:
   print(str(peperronmike) + " Es mayor a: " + str(alchile))
  if alchile > peperronmike:
   print(str(alchile) + " Es mayor que :" + str(peperronmike))


def problema_2():
  impar_o_par = input("Deme un numero: ")
  if int(impar_o_par) % 2 == 0:
   print("Es un numero par")
  else:
   print("Es un numero impar")


def problema_3():
  nombre = input("Registre su nombre aca: ")
  edad = input("Deme su edad: ")
  sexo = input("Deme su sexo (masculino o femenino): ")
  if int(edad) >= 62 and sexo == "masculino":
   print(nombre + " usted es masculino y tiene mas de 62 años entonces se puede jubilar")
  elif int(edad) < 62 and sexo == "masculino":
   print(nombre + " usted es masculino pero como tiene menos de 62 años, no se puede jubilar")
  elif int(edad) >= 57 and sexo == "femenino":
   print(nombre + " usted es mujer y tiene la edad necesaria para jubilarse.")
  elif int(edad) < 57 and sexo == "femenino":
   print(nombre + " Anausted es mujer pero no cumple con la edad requerida, no se puede jubilar")


def problema_4():
  nombre = input("Deme su nombre: ")
  sexo = input("Deme su sexo (masculino o femenino): ")
  edad = input("Deme su edad: ")
  if int(edad) >= 18 and sexo == "masculino":
    print(nombre + " usted puede prestar servicio militar porque tiene la edad necesaria y es hombre")
  elif int(edad) < 18 and sexo == "masculino":
    print(nombre + " usted es hombre pero no puede prestar servicio militar ya que no cumple con la edad necesaria")
  elif int(edad) >= 18 and sexo == "femenino":
    print(nombre + " usted es mujer, lo que quiere decir que tenga la edad que tenga no puede prestar servicio")
  elif int(edad) < 18 and sexo == "femenino":
    print(nombre + " usted es mujer y de paso es menor, lo que quiere decir que no puede prestar servicio")


def esto_solo_sirve_para_multiplicar_por_12_y_restar_los_valores_dados():
  año_de_inicio = int(input("Digite su año de inicio: "))
  print(str(año_de_inicio))
  año_final = int(input("Digite su año final: "))
  print(str(año_final))
  diferencia_en_años = int(año_final) - int(año_de_inicio)
  diferencia_en_meses = int(diferencia_en_años) * 12
  print("La diferencia en meses es: " + str(diferencia_en_meses) + " y la diferencia en años es: " + str(diferencia_en_años))


def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

 # print(my_beard_description)

def ejercicios_strings_y_metodos_de_strings_codeacademy():
 highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
 #print(highlighted_poems)

 highlighted_poems_list = highlighted_poems.split(",")
 #print(highlighted_poems_list)

 highlighted_poems_stripped = []
 for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip(" "))
  #print(highlighted_poems_stripped)

 highlighted_poems_details = []
 for pepe in highlighted_poems_stripped:
  highlighted_poems_details.append(pepe.split(":"))
  #print(highlighted_poems_details)

 titles = []
 poets = []
 dates = []
 for pepe in (highlighted_poems_details): 
   titles.append(pepe[0])
   poets.append(pepe[1])
   dates.append(pepe[-1])
 

 for frases in range(0,len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}".format(titles[frases], poets[frases], dates[frases]))
#ejercicios_strings_y_metodos_de_strings_codeacademy()


"""""""""
# Esto de abajo no sirve xd
def esto_me_puede_servir_para_entender_los_imports():
  from matplotlib import pyplot as plt
  import random

  numbers_a = range(1, 13)
  numbers_b = random.sample(range(1000), 12)
  plt.plot(numbers_a, numbers_b)
  plt.show()

# esto_me_puede_servir_para_entender_los_imports()
# lo de arriba no sirve pa un culo aca
"" "" "" """


# LO DE ABAJO SI SIRVE :D
def a_ver_si_esto_me_ayuda_un_poco_para_entender_los_imports_y_eso():
  # Import Decimal below:
  from decimal import Decimal

  # Fix the floating point math below:
  two_decimal_points = Decimal("0.2") + Decimal("0.69")
  print(two_decimal_points)

  four_decimal_points = Decimal("0.53") * Decimal("0.65")
  print(four_decimal_points)
#a_ver_si_esto_me_ayuda_un_poco_para_entender_los_imports_y_eso()



def Numeros_multiplos_por_5():
  multiplos_comprobacion = True
  while multiplos_comprobacion == True:
   n = int(input("Ingrese un numero positivo que sea multiplo de 5: "))
   if n % 5 == 0:
     for i in range(0, n+1, 5):
       print(i)
     multiplos_comprobacion = False  
   else: 
     print("Tu numero no es divisible por 5. Intenta de nuevo")

#Numeros_multiplos_por_5()


def numeros_impares_dados_por_teclado():
  comprobacion = True
  while comprobacion == True:
   n = int(input("¿Hasta que numero quiere que sean impares y los leeremos todos: "))
   if n % 2 == 1:
     for juansi in range(1, n+1, 2):
       print(juansi)
     comprobacion = False  
   else:
     print("No se puede realizar porque usted digito un numero par")
#numeros_impares_dados_por_teclado()


def factoriales_de_un_numero():
  n = int(input("Deme un numero pa sacarle el factorial: "))
  pepe = 1
  for i in range(1, n+1, 1):
    pepe = (i*pepe)
  print("El factorial de: " + str(n) + " Es: " + str(pepe))
#factoriales_de_un_numero()

"""""""""""""""
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

for pepe in user_ids.keys():
  print(pepe)
"""""""""

# LO DE ABAJO ES SUPER IMPORTANTE PORQUE ES UN CODIGO QUE UTILIZA LOOPS Y DICCIONARIOS Y ALGUNAS FUNCIONES PARA LOS DICCIONARIOS, JUEGO DE MESA SCRABBLE
# LEELO BIEN PARA ENTENDER LOS DICCIONARIOS, FUNCIONES, Y LOOPS
# CUANDO QUIERAS LE QUITAS LAS COMILLAS PARA PROBARLO 

def diccionarios_funciones_loops_y_cosas_para_entender_lo_que_mas_necesito_reforzar():
 letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
 points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
 letter_to_points = {key:value for key, value in zip(letters, points)}
 #print(letter_to_points)
 letter_to_points[" "] = 0


 def score_word(word):
   point_total = 0
   for letter in word:
     point_total += letter_to_points.get(letter, 0)
   return point_total 

 brownie_points = score_word("BROWNIE")
 print(brownie_points)

 player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
 player_to_points = {}
 for player, words in player_to_words.items():
   player_points = 0
   for word in words:
     player_points += score_word(word)
   player_to_points[player] = player_points
 print(player_to_points)
#diccionarios_funciones_loops_y_cosas_para_entender_lo_que_mas_necesito_reforzar()


def ejercicio_1_pagina_web():
  n = input("Deme una palabra cualquiera y la repetiremos 10 veces: ")
  for repeat in range(10):
    print(n)
#ejercicio_1_pagina_web()



def ejercicio_2_pagina_web():
  edad = int(input("Deme su edad: "))
  for años in range(1, edad+1, 1):
   print("Has pasado por estos años: " + str(años))
#ejercicio_2_pagina_web()



def ejercicio_3_pagina_web():
  n = int(input("Escriba un numero: "))
  for juancho in range(n, -1, -1):
    print(juancho)
#ejercicio_3_pagina_web()



def clases_metodos_y_atributos():
  class Circle:
   pi = 3.14
   def __init__(self, diameter):
     print("Creating circle with diameter {d}".format(d=diameter))
     # Add assignment for self.radius here:
     self.radius = diameter / 2
  
  
   def circumference(self):
     return 2 * self.pi * self.radius



  medium_pizza = Circle(12)
  teaching_table = Circle(36)
  round_room = Circle(11460)

  print(medium_pizza.circumference())
  print(teaching_table.circumference())
  print(round_room.circumference())

#clases_metodos_y_atributos()