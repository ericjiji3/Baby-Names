#  File: BabyNames.py

#  Description:

#  Student Name:  Eric Ji

#  Student UT EID:  ej6638

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 9/11/19

#  Date Last Modified: 9/13/19

import operator

#Creates a dictionary of babynames as the key and their popularity rankings as the values
def babynamedic():
    file = open("names.txt", "r")
    babyname = {}
    list1 = []

    for x in file.readlines():
        baby = x.split()
        #converts values to integers
        list1 = list(map(int, baby[1:]))
        babyname[baby[0]] = list1

    return babyname

def menu(dict):
    cont = True
    while cont == True:
        #Prints menu
        print("1. Search for names")
        print("2. Display data for a name")
        print("3. Display all names that appear in one decade")
        print("4. Display all names that appear in all decades")
        print("5. Display all names that are more popular every decade")
        print("6. Display all names that are less popular every decade")
        print("7. Quit")
        user = input("Enter number: ")
        print()
        user = int(user)

        #1
        if user == 1:
            name = input("Enter name: ")
            if name in dict:
                print("True")
                print()
            else:
                print("False")
                print()
        #2
        if user == 2:
            name1 = input("Enter name: ")
            if name1 in dict:
                print("By decade (1900 - 2000):", dict[name1])
                print()
            else:
                print("This is not a name in the data base")
                print()
        #3
        if user == 3:
            decade = input("Enter decade: ")
            decade = int(decade)
            #Makes decade into a single integer
            decade = int((decade - 1900)/10)
            list2 = []
            #Creates list of tuples
            for i in dict:
                if(dict[i][decade] != 0):
                    k = (i, dict[i][decade])
                    list2.append(k)
            #sorts the second half of each tuple in the list
            list2.sort(key=lambda tup: tup[1])
            print(list2)
            print()
        #4
        if user == 4:
            notZero = True
            list3 = []
            #Checks to see if there is a zero in the key values
            for l in dict:
                if 0 in dict[l]:
                    notZero = False
                else:
                    notZero = True
                if notZero == True:
                    list3.append(l)

            print(list3)
            print()
        #5
        if user == 5:
            list4 = []
            for j in dict:
                #assigns variable a boolean by checking if all variables are in increasing order
                increasing = all(v < b for v, b in zip(dict[j], dict[j][1:]))
                if increasing == True:
                    list4.append(j)
            print(list4)
            print()
        #6
        if user == 6:
            list5 = []
            for n in dict:
                #assigns variable a boolean by checking if all variables are in decreasing order
                decreasing = all(prev > next for prev, next in zip(dict[n],dict[n][1:]))
                if decreasing == True:
                    list5.append(n)
            print(list5)
            print()


        #7
        if user == 7:
            break
if __name__ == '__main__':
    menu(babynamedic())

