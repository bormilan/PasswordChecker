#import for use upper and lowercase alphabet
import string
#import to use random number generator and shuffle
import random

def read():
    #variables for the data
    users = []
    passwords = []

    file = input("Please add the file where you want to read this:")
    file = correct(file)

    try:
        #read the file and append data to variables
        with open(file, "r") as f:
            for line in f:
                users.append(line.split(",")[0])
                temp = line.split(",")[1]
                passwords.append(temp.rstrip())
    except IOError:
        print("File not found !")
    #return both
    return users,passwords

#check the strength
def check(pw):
    #initalize different chars to compare
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = ("0123456789")
    symbols = ("!+-=?#%*@&^$_")
    #variable for count char types
    items = 0
    #boolians if a type was in the string earlier
    is_lower = False
    is_upper = False
    is_number = False
    is_symbol = False
    #loop for count types
    for i in range(len(pw)):
        if pw[i] in lower and not is_lower:
            items += 1
            is_lower = True
        elif pw[i] in upper and not is_upper:
            items += 1
            is_upper = True
        elif pw[i] in symbols and not is_symbol:
            items += 1
            is_symbol = True
        elif pw[i] in numbers and not is_number:
            items += 1
            is_number = True

    #find out what strength is this
    if len(pw) > 10 and items == 4:
        return "STRONG"
    elif len(pw) > 8 and items == 3:
        return "MODERATE"
    else:
        return "WEAK"

#write the different data
def write(users,pws,strengths):
    file = input("Please add the file where you want to write it:")
    file = correct(file)
    with open(file, "w") as f:
        for i in range(len(users)):
            f.write(users[i] + "," + pws[i] + "," + strengths[i] + "\n")

    print("The result can be found in the file named: '" + file + "'")

#make the file path to python compatible
def correct(filepath):
    newpath = ""
    #change all "\"-chars into "/"-char
    for i in range(len(filepath)):
        if filepath[i] == "\\":
            newpath += "/"
        else:
            newpath += filepath[i]

    #add the correct file extention if the user not enter it well
    if ".txt" not in filepath:
        newpath += ".txt"

    #return the path in the correct format
    return newpath

def pwGenerator():
    #initalize some char sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = ("0123456789")
    symbols = ("!+-=?#%*@&^$_")

    #some variables what the program will usde
    pwlength = 0
    newPw = []

    #endless loop to create a storng password
    while True:
        #generating random numbers of the chars for each type
        random_l = random.randint(1,5)
        random_u = random.randint(1,5)
        random_n = random.randint(1,5)
        random_s = random.randint(1,5)
        # sum them for the full length of the password
        pwlength += random_l + random_u + random_n + random_s

        #add random chars from the sets
        for i in range(random_l):
            temp = random.randint(1,len(lower)-1)
            newPw.append(lower[temp])

        for i in range(random_u):
            temp = random.randint(1,len(upper)-1)
            newPw.append(upper[temp])

        for i in range(random_n):
            temp = random.randint(1,len(numbers)-1)
            newPw.append(numbers[temp])

        for i in range(random_s):
            temp = random.randint(1,len(symbols)-1)
            newPw.append(symbols[temp])

        #shuffle it to make chars sequence random then return the new password
        random.shuffle(newPw)
        pwstring = ''.join(newPw)
        if pwlength > 10:
            return pwstring

def save(name,pw):
    file = input("Please add the file where you want to write it:")
    file = correct(file)

    with open(file, "a") as f:
        f.write(name + ", " + pw + '\n')

#main function what asks the user which option te user wants
def main():
    print("Hello, press 1 for checking the strength of passwords from a .txt file")
    print("or press 2 for create a new user with a 'strong' password")

    #ask which option the user want and call the function for it
    while True:
        option = input()
        if option == "exit":
            print("This program is courtesy of Mason Middaugh")
            break
        elif option == "1":
            #read the data from the txt file
            temp = read()
            users = temp[0]
            passwords = temp[1]

            #check the passwords' stength and write them to file
            strengths = []
            for i in range(len(passwords)):
                #give strength all of them
                strengths.append(check(passwords[i]))

            #tell the user the number of passwords checked
            print(str(len(users)) + " password checked")

            #call write function
            write(users,passwords,strengths)

        elif option == "2":
            #infinite loop what ends when the user gives a maximum 20 character long username
            while True:
                newName = input("please add the new user's name(max.20 chars):")
                if len(newName) <= 20:
                    break
                else:
                    print("The name is too long ! Please try again !")

            while True:
                #generate a new strong password
                newPw = pwGenerator()
                #print it to the user and ask if its good
                print("New Account:")
                print("Username: " + newName + " Password: " + newPw)

                #loop what ends when the user add a valid input
                while True:
                    answer = input("Do you want to save this password ?(y/n): ")
                    if answer in "yn":
                        break
                    else:
                        print("Invalid input ! Please try again !")

                #if user want to save this account call the save funvtion and end this loop and go back to the main loop
                if answer == "y":
                    save(newName,newPw)
                    return
                #if user dont want to, start a new loop what asks the user if he want to try a new password or just exit this function
                elif answer == "n":
                    #loop what ends when the user add a valid input
                    while True:
                        nextanswer = input("Do you want to try a new password ?(y/n):")
                        if nextanswer in "yn":
                            break
                        else:
                            print("Invalid input ! Please try again !")

                    #if user want to try a new password, then continues the loop at the start with a new password
                    if nextanswer == "y":
                        continue
                    #if user dont want to try a new password then ends this loop and go back to the main
                    elif nextanswer == "n":
                        return

        #if the user input was invalid, ask the user to try again
        else:
            print("Invalid option ! Please try again !")

main()
