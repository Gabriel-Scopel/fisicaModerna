""" Gabriel Souza Scopel - 222210262    
Kaique da Silva Fernandes - 222210114
Murilo Carvalho Povoa da Silva - 222210346
Matheus Arcanjo """

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
    print((2*pi)/lambida)
  elif(a == "2"):
    w = float(input("Digite o valor de w: "))
    print(v/w)
  elif(a == "3"):
    T = float(input("Digite o valor de T: "))
    print((2*pi)/T)
  elif(a == "4"):
    f = float(input("Digite o valor de f: "))
    print((2*pi)/f)
  elif(a == "5"):
    k = float(input("Digite o valor de k: "))
    print((2*pi)/k)
  elif(a == "6"):
    f = float(input("Digite o valor de f: "))
    print(v/f)
  elif(a == "7"):
    w = float(input("Digite o valor de w: "))
    print(w/2*pi)
  elif(a == "8"):
    lambida = float(input("Digite o valor de lambida: "))
    print(v/lambida)
  else:
    print("Digite um comando válido.")
    
    
    
def Em():
    Em = float(input("Digite o valor de Em:"))
    Bm = Em/c
    I = Em**2/(2*mi*c)
    print(f"Bm: {Bm:.2e}", Bm)
    print(f"I: {I:.2e}",I)

def Bm():
    Bm = float(input("Digite o valor de Bm:"))
    Em = c*Bm
    I = Bm**2/2*mi
    print(f"Em: {Em:.2e}", Em)
    print(f"I: {I:.2e}",I)
    
def I():
    I = float(input("Digite o valor de I:"))
    Em = sqrt(I*2*mi*c)
    Bm = sqrt(I*2*mi)
    print(f"Bm: {Bm:.2e}",Bm)
    print(f"Em: {Em:.2e}", Em)

def f():
    f = float(input("Digite o valor de f:"))
    w = 2*pi*f
    lambida = c/f
    k = f/(c*2*pi)
    print(f"w: {w:.2e}", w)
    print(f"lambida: {lambida:.2e}", lambida)
    print(f"k: {k:.2e}",k)
    
def lambida():
    lambida = float(input("Digite o valor de lambida:"))
    k = (2*pi)/lambida
    f = c/lambida
    w = c*2*pi/lambida
    print(f"w: {w:.2e}",w)
    print(f"f: {f:.2e}", f)
    print(f"k: {k:.2e}", k)
    
def k():
    k = float(input("Digite o valor de k: "))
    lambida = (2*pi)/k
    f = k*c*2*pi
    w = k*c*4*pi
    print(f"w: {w:.2e}", w)
    print(f"lambida: {lambida:.2e}", lambida)
    print(f"f: {f:.2e}", f)
    
def w():
    w = float(input("Digite o valor de w:"))
    f = w/(2*pi)
    lambida = c*2*pi/w
    k = w/(c*4*pi)
    print(f"f:{f:.2e}", f)
    print(f"lambida: {lambida:.2e}",lambida)
    print(f"k: {k:.2e}",k)




def main():
    
   # print("Você deseja calcular f, lambida, k ou w?")
    print("Digite S para sim e N para não")
    a = input("Você deseja calcular f, lambida, k ou w?")
    if(a=="S"):
        f1()
    elif(a=="N"):
        print("a")
        
    else:
        print("Reinicie e digite um comando válido.")
    
    
    """ count = input('qual formula? ')
    
    if count == '1':
        Em()
    elif count == '2':
        Bm() 
    elif count == '3':
        I()
    elif count == '4':
        f()
    elif count == '5':
        lambida()
    elif count == '6':
        k()
    elif count == '7':
        w()
    else:
        print("Você digitou um comando inválido.") """

main()