import datetime
nm=input("Enter Your Name Please:")
print("***Welcome",nm,"In this Online Tiket Booking System***")
print("In Bus Total 30 Seats are Available")
seat=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
pname = []
page = []
pcontact=[]
date=[]
new_bus=[]
new_Driver=[]

class Ticket:
    def book_Ticket(self):
        people = int(input("\nEnter number of Ticket you want:"))
        for p in range(people):
            s = int(input("Enter the seat number which you want:"))
            seat.remove(s)
            dt=input("Enter the date Which you want to book Ticket:")
            date.append(dt)
            name = str(input("Name:"))
            pname.append(name)
            age = int(input("Age :"))
            page.append(age)
            contact=int(input("Contact:"))
            pcontact.append(contact)


        x=0
        print("Your Ticket Is Booked Successfully")
        print("\nTotal Ticket : ", people)
        for p in range(1, people + 1):
            print("Ticket : ", p)
            print("Name:", pname[x])
            print("Age:", page[x])
            print("Contact:",pcontact[x])
            x += 1

        a = str(input("\nDo you Perform Any Another Operation?? Yes or NO:"))
        if a == "Yes":
            main()
        else:
            exit()

    def cancle_Ticket(self):
        cancle=int(input("Enter How Many Tickets You want to be Canclled:"))
        for c in range(cancle):
            s=int(input("Enter the seat no which you want to cancalled:"))
            if seat.__contains__(s):
                print("Sorry!!! This Ticket Is not Book so you don't Cancle it")
            else:
                seat.append(s)
                print("Your Ticket is Successfully Canclled")

        a = str(input("\nDo you Perform Any Another Operation?? Yes or NO:"))
        if a == "Yes":
            main()
        else:
            exit()

    def seat_Avilable(self):
        print("This seats Are Avilable Bus:",seat)

        a = str(input("\nDo you Perform Any Another Operation?? Yes or NO:"))
        if a == "Yes":
            main()
        else:
            exit()

    def add_new_bus(self):
        name=input("Enter The Bus Name Which You Want to add:")
        no=input("Enter The Bus Number:")
        new_bus.append(name)
        new_bus.append(no)
        print("New Bus Added Successfully")

        a = str(input("\nDo you Perform Any Another Operation?? Yes or NO:"))
        if a == "Yes":
            main()
        else:
            exit()

    def add_new_driver(self):
        name=input("Enter The name of Driver:")
        age=int(input("Enter the age of Driver:"))
        contact=int(input("Enter The Contact Number of Driver:"))
        experiance=input("Enter The Experiance of Driver in terms of Years:")

        new_Driver.append(name)
        new_Driver.append(age)
        new_Driver.append(contact)
        new_Driver.append(experiance)
        print("New Driver Added Successfully")

        a = str(input("\nDo you Perform Any Another Operation?? Yes or NO:"))
        if a == "Yes":
            main()
        else:
            exit()

    def Pasenger_details(self):
        d=input("Enter The date which you want to check details of pasenger:")
        b=input("Enter The Name of Bus Which you want to Check details of Pasenger:")
        if date.__contains__(d):
            print("Wait we find and Display the Records...")
            print(pname)
            print(page)
            print(pcontact)
        else:
            print("There is no passenger record present in this date")


def main():
    t1=Ticket()
    print("1-Book Ticket")
    print("2-Cancle Ticket")
    print("3-Check Seat Availability")
    print("4-Add new Bus")
    print("5-Add new Driver")
    print("6-Print Pasenger details")
    print("0-Exit")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        t1.book_Ticket()
    if choice==2:
        t1.cancle_Ticket()
    if choice==3:
        t1.seat_Avilable()
    if choice==4:
        t1.add_new_bus()
    if choice==5:
        t1.add_new_driver()
    if choice==6:
        t1.Pasenger_details()
    if choice==0:
        exit()
m1=main()