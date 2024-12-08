import random

characters= ["A", "B", "C","D", "E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", "a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "1", "2", "3", "4", "5", "6","7","8", "9","0", "!", "@","$","%","&"]

def generate_pass():
    length= int(input("Enter the no. of character you want in your password: \n"))
    password= ""
    for n in range(0, length):
        char= random.choice(characters)
        password+= char
    print(password)

generate_pass()