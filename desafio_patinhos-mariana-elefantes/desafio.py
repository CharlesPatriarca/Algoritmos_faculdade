#1 Patinhos

for patinhos in range(5, 0, -1):
    print(f"{patinhos} patinhos foram passear")
    print("Além das montanhas para brincar")
    print("A mamãe gritou: Quá, quá, quá, quá")
    if patinhos > 1:
        print(f"Mas só {patinhos-1} patinhos voltaram de lá\n")
    else:
        print("Mas nenhum patinho voltou de lá!\n")



#2 Elefantes
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for elefantes in n:
    print(elefantes, 'elefante incomodam muita gente')
    elefantes += 1
    print(elefantes, 'elefantes', 'incomodam ' * elefantes, 'muito mais')



#3 Mariana
print("Mariana conta")

print()

for numero in range(1, 11):

  print(f"Mariana conta {numero}")


  for i in range(1, numero + 1):
    print(f"É {i}", end=" ")


  print()
  print(f"Ana, viva a Mariana, viva a Mariana")
  print()
