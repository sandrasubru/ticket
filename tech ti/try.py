
        

name=input("Name:")
admno=input("Admission number")
print("1.Angamaly")
print("2.Thrissur")
print("3.Muvattupuzha")    
print("4.Perumbavoor")
print("5.Chalakudy")
print("6.Aluva")
des=int(input("Destination number"))
if des==1:
    print("Angamaly")
    loc="Angamaly"
elif des==2:
    print("Thrissur")
    loc="Thrissur"
elif des==3:
    print("Muvatupuzha")
    loc="Muvatupuzha"
elif des==4:
    print("Perumbavoor")
    loc="Perumbavoor"
elif des==5:
    print("Chalakkudy")
    loc="Chalakudy"
elif des==6:
    print("Aluva") 
    loc="Aluva"
else:
    print("Invalid entry")
a=int(input("enter one way or two way(1 or 2)"))
if a==1:
    s = 80
    print("Fare:",s)
    date=input("enter going date")
    print("Going date:",date)
elif a==2:
    s=160
    print("Fare:",s)
    date=input("enter going date")
    redate=(input("enter return date"))  
    print("Going date:",date)
    print("Return date:",redate)
else:
    print("Invalid entry")   



 #web 2
print("Name of the student:",name)
print("Admission number of student:",admno)
print("Destination:",loc)
print("Total fare:",s)
if a==1:
    print("Going date:",date)
else:
    print("Going date:",date)
    print("Return date:",redate)  

#web 3

print("Your transaction is successfull")
print("Your transaction has failed")          

    


