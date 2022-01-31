#use python 3.10.1 and use match case

from sys import exit

def menu(): #membuat menu untuk dipilih
    print("==================================")
    print("| Chose 1 for Average            |")
    print("| Chose 2 for Max                |")
    print("| Chose 3 for Average and Max    |")
    print("| Chose 4 for Display Data       |")
    print("==================================")
    print("")

def rerata(s): #membuat rata rata tabungan dari 4 minggu
    average = sum(s) / 4
    return average

def maximum(s): #membuat tabungan terbesar dari 4 minggu tsb
    maks = max(s)
    return maks

def displayData(): #menampilkan data yang didapatkan jika mengetik nama A
    with open("data.txt") as f:
        a = f.readlines()
        s = a[idx].split()
        k = [int(a[idx]) for a[idx] in s[1:]]
        print(s[0], ":", k)
        print("Laptop Cost :",s[1])
        print("Savings week one to four :",s[2:])

with open("data.txt") as f:
    a = f.readlines()  # tiap baris dalam file
    name = [i.split()[0] for i in a]
    print("Who do you want to search?")
    query = input("Enter Name : ")
    print("--------------------------")
    print("")

    idx = 0
    try:
        idx = name.index(query)
        menu()
    except:
        print("Name not found!")
        exit(0)#berhasil = 0

    chose = int(input("Enter A Number: "))
    print("")
    s = a[idx].split()
    s = [int(i) for i in s[2:]]

    match chose: #file handling
        case 1:
            print("Average :", rerata(s))
        case 2:  # default
            print("Max :", maximum(s))
        case 3:
            print("Average :", rerata(s))
            print("Max :", maximum(s))
        case 4:
            displayData()
