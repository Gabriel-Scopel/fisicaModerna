""" Gabriel Souza Scopel - 222210262    
Kaique da Silva Fernandes - 222210114
Murilo Carvalho Povoa da Silva - 222210346
Matheus T da Silva Arcanjo - 22221020-5 """

import math
pi = math.pi
c = 3e8
v = 3e8
mi = 4*pi*10**-7

def f1():
  
  print("1 - k=2pi/lambida")
  print("2 - k=v/w")
  print("3 - w=2pi/T")
  print("4 - w=2pi*f")
  print("5 - lambida = 2pi/k")
  print("6 - lambida = v/f")
  print("7 - f=w/2pi")
  print("8 - f=v/lambida")
  a=input("Digite o código correspondente a fórmula que você deseja utilizar:")
  if(a == "1"):
    lambida = float(input("Digite o valor de Lambida: "))
    print((2*pi)/lambida, "rad/m")
  elif(a == "2"):
    w = float(input("Digite o valor de w: "))
    print(v/w, "rad/")
  elif(a == "3"):
    T = float(input("Digite o valor de T: "))
    print((2*pi)/T, "rad/s")
  elif(a == "4"):
    f = float(input("Digite o valor de f: "))
    print((2*pi)*f, "rad/s")
  elif(a == "5"):
    k = float(input("Digite o valor de k: "))
    print((2*pi)/k, "m")
  elif(a == "6"):
    f = float(input("Digite o valor de f: "))
    print(v/f, "m")
  elif(a == "7"):
    w = float(input("Digite o valor de w: "))
    print(w/2*pi, "Hz")
  elif(a == "8"):
    lambida = float(input("Digite o valor de lambida: "))
    print(v/lambida, "Hz")
  else:
    print("Digite um comando válido.")
    
    
def f2():
  
  print("1 - Em = c*Bm")
  print("2 - Bm = Em/c")
  print("3 - I = E^2/2mi*c")
  print("4 - I = c*B^2/2mi")
  a=input("Digite o código correspondente a fórmula que você deseja utilizar:")
  if(a=="1"):
    Bm = float(input("Digite o valor de Bm: "))
    print(c*Bm, "V/m")
  elif(a=="2"):
    Em = float(input("Digite o valor de Em: "))
    print(Em/c, "T")
  elif(a=="3"):
    E = float(input("Digite o valor de E: "))
    print((E*E)/2*mi*c, "W/m^2")
  elif(a=="4"):
    B = float(input("Digite o valor de B: "))
    print((c*B*B)/2*mi, "W/m^2")
  else:
    print("Digite um comando válido")
    


def main():
    print("Este programa tem por finalidade realizar cálculos envolvendo Ondas eletromagnéticas. Nele é possível calcular frequência, lambida, número de ondas e frequência angular, Campo Magnético, Intensidade e Campo elétrico \n")
    print("Todas as unidades a serem digitadas devem estas no sistema internacional \n")
  
    print("Integrantes do grupo:")
    print("Gabriel Souza Scopel")
    print("Kaique da Silva Fernandes")
    print("Murilo Carvalho Povoa da Silva")
    print("Matheus Arcanjo")
    print()
    input("Digite Enter para continuar...")
    print("Você deseja calcular f, lambida, k ou w?")
    a = input("Digite S para sim e N para não: ")
     
    if(a=="S"):
        f1()
    elif(a=="N"):
      print("Você deseja calcular Bm, Em ou I?")
      b = input("Digite S para sim e N para não:")
      if(b == "S"):
        f2()
      else:
        print("Reinicie o programa.")
      
        
    else:
        print("Reinicie e digite um comando válido.")

main()