alphabet = "abcdefghijklmnopqrstuvwxyz"

def cipher(x,y):
    z = ""
    for i in x:
        j = alphabet.find(i)
        j += y
        j %= len(alphabet)
        z += alphabet[j]
    return z

def decipher(a,b):
    c = ""
    for i in a:
        g = alphabet.find(i)
        g -= b
        g %= len(alphabet)
        c += alphabet[g]
    return c

def inpnum():
    while 1:
        x = input("Pin: ")
        if x.isdecimal():
            return int(x)
        print("please enter number")
         
while 1:
    command = input("Cipher or Decipher [c/d] ")
    if command == "c":
        content = input("->")
        pin = inpnum()
        print(cipher(content,pin))
    elif command == "d":
        content = input("->")
        pin = inpnum()
        print(decipher(content,pin))
    elif command == "exit" or command == "quit":
        break
    else:
        print(f"{command}, unknow command!")
