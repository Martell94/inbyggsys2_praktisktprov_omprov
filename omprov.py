#Author: Jacob Martell
#Date: 2023-11-27

listofnumbers = []

def main(): 
   userinput = input("Vilka tabeller vill du beräkna? ")
   userinput = userinput.strip(' ')  
   userinput = userinput.split(' ')
   for i in userinput:
      try:
         calculate(int(i)) 
      except:
         exitprogram()
      
def calculate(number):
   for i in range(1,11):
      print(f'{number} * {i} = {i*number}')
   print("\n")
      
def exitprogram():
   print("Avslutar program.")

if __name__ == "__main__":
   main()