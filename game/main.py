import random
#importamos la librería ramdon

#con este proyecto aprenderemos a implementar las tuplas, con nuestro famoso juego de (piedra, papel, tijera)
#! vamos a ello ¡()


options = ('piedra', 'papel', 'tijera')  #implementamos

computer_wins = 0
user_wins = 0

rounds = 1

while True: 
  
  print('*' * 20)
  print('ROUND', rounds)
  print('#' * 20)

  print('computer_wins', computer_wins)
  print('user_wins', user_wins)  
  
  user_option = input('piedra, papel, o tijera ==>>  ')
  user_option = user_option.lower()
  
  rounds += 1
  
 #podemos alertar al usuario cuando ingresa un elemento que no está en la tupla 
 #(otra palabra)
  if not user_option in options:
    print('esa acción que ingresaste, no es válida')
    continue

  computer_option = random.choice(
    options
  )  #aca el computador está eligiendo de forma aleatoria las opciones, al igual que el usuario

  print('user_option ==>>', user_option)  #imprimimos

  print('computer_option ==>>', computer_option)

  if user_option == computer_option:
    print('empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra hgana a tijera')
      print('user gano')
      user_wins =+ 1
    else:
      print('papel gana a tijera')
      print('computer gano')
      computer_wins =+ 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana piedra')
      print('user gano')
      user_wins =+ 1
    else:
      print('tijera gana papel')
      print('computer gano')
      computer_wins =+ 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print("tijera gana papel")
      print('user gano')
      user_wins =+ 1
    else:
      print('piedra gana a tijera')
      print('computer gano')
      computer_wins =+ 1

  if computer_wins == 5:
    print('la computadora es la campeona ')
    break
    
  if user_wins == 5:
    print('el usuario es el campeon')
    break
