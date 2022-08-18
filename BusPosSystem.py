#Modules
from datetime import date, timedelta
import re
from traceback import print_tb


#Data Structures
trip_info = ["Bus No.12","Dhaka to chittagong", "8:00 pm","Kallanpur Bus Terminal Dhaka", "Chittagong Port Bus Terminal", date.today() + timedelta(days=3)]
bus_info =  [
    #Seat No. Ticket No. Seat Avability Price
    ["A1","D1B1T01",False,2000], ["A2","D1B1T02",False,2000], ["A3","D1B1T03",False,2000], ["A4","D1B1T04",False,2000],
    ["B1","D1B1T05",False,2000], ["B2","D1B1T06",False,2000], ["B3","D1B1T07",True,2000], ["B4","D1B1T08",True,2000],
    ["C1","D1B1T09",True,2000], ["C2","D1B1T10",True,2000], ["C3","D1B1T11",True,2000], ["C4","D1B1T12",True,2000],
    ["D1","D1B1T13",False,2000], ["D2","D1B1T14",False,2000], ["D3","D1B1T15",False,2000], ["D4","D1B1T16",False,2000]
            ]

passenger_info = [
    #First Name,Last Name, Age, Gender, Seat Number, Amount Paid ,Buying Date, Expiration Date
    ["Mubashir","Tawhid",19,"Male","A1","D1B1T01",2000,"13th-Aug-22","17th-Aug-22"], ["Ozaire","Wasit",20,"Male","A2","D1B1T02",2000,"13th-Aug-22","17th-Aug-22"],
    ["Shams","Habib",20,"Male","A3","D1B1T03",2000,"13th-Aug-22","17th-Aug-22"],["Adrika","Wasita",21,"Female","A4","D1B1T04",2000,"13th-Aug-22","17th-Aug-22"],
    ["Noshin","Hossain",21,"Female","B1","D1B1T05",2000,"13th-Aug-22","17th-Aug-22"],["Tasnuva","Tahsin",21,"Female","B2","D1B1T06",2000,"13th-Aug-22","17th-Aug-22"],
    ["Ahnaf","Ahmed",23,"Male","D1","D1B1T13",2000,"13th-Aug-22","17th-Aug-22"],["Wahed","Shezan",21,"Male","D2","D1B1T14",2000,"13th-Aug-22","17th-Aug-22"],
    ["Aqib","Hossain",23,"Male","D3","D1B1T15",2000,"13th-Aug-22","17th-Aug-22"],["Zaman","Mantaka",19,"Male","B1","D1B1T16",2000,"13th-Aug-22","17th-Aug-22"]
                 ] 



def VerifyPassengerInfo(name,age,gender):
    name = name.upper()
    isValid = False
    letterCount = 0
    #Verify Name 
    for letter in name:
        if((letter >= "A" and letter <= "Z" and letter != "") or (letter == " " and letterCount > 2)):
            letterCount += 1
            isValid = True
        else:
            return False
    #Verify Age
    if(age >= 0 and age <  150):
        isValid = True
    else:
        return False
    #Verify Gender
    if(gender == "MALE" or gender == "FEMALE" or gender == "OTHER"):
        isValid = True
    else:
        return False
    
    return isValid

def ShowAvailbeSeats(): #Print All the  seats which are available
    availableSeatList = []  #To keep track of available Seats
    for i in range(len(bus_info)):
        if(bus_info[i][2] == True):
            ticketList = [bus_info[i][0],bus_info[i][1]]
            availableSeatList.append(ticketList)
    print("Seat No. Ticket No.")
    for i in range(len(availableSeatList)):
        ticketString = "{0:8} {1:9}" .format(availableSeatList[i][0],availableSeatList[i][1],)
        print(ticketString)

def SeatStatus(seatNum):
    for i in range(len(bus_info)):
        if(seatNum == bus_info[i][0]):
            if(bus_info[i][2] == False):
                return print("Seat is available for booking")
            else:
                return print("Seat is already booked.")
        elif(i == len(bus_info) - 1 and seatNum != bus_info[i][0]):
            return print("Invalid Seat No. was entered.")

def CheckTicketAvaibility(ticket,wantIndex): #Check if the ticket is available
    tikAvailable = False
    count = 0
    for i in range(len(bus_info)):
        if(bus_info[i][2] == True and tikAvailable == False):
            if(bus_info[i][0] == ticket.upper()):
                count = i
                tikAvailable = True
    if(wantIndex):
        return count
    else:
        return tikAvailable
                                                
def SoldOut(): #Check if all the tickets are sold out
    isSoldOut = True
    for i in range(len(bus_info)):
        if(bus_info[i][2] == True):
            isSoldOut = False
    return isSoldOut

def FindTicket(seatNum):
    for i in range(len(bus_info)):
        if(bus_info[i][0] == seatNum.upper()):
            ticket = bus_info[i][1]
    print(ticket)
    return ticket
    
def ShowAllSeats():
    print("\nSeat No. | Ticket No. | Avaibility | Amount")
    for i in range(len(bus_info)):
        print("{0:9} {1:11} {2:11} {3:6}" .format(bus_info[i][0],bus_info[i][1],bus_info[i][2],bus_info[i][3]))

def BookTicket(passengerCount): #Allow the user to book ticket
    if(SoldOut()):
        return print("Sorry, we are sold out :( ")
    
    for i in range(passengerCount):
        canBook =  False
        cancelBook = "" #Initial Variables
        toAdd = []
        tik = ""
        if(i < 1):
            allPassengers = [] #To make sure we do not empty the list after first run of loop

        while(canBook != True and cancelBook != "Y"):
            pFirstName = input("Enter Passenger First Name: ")
            pLastName = input("Enter Passenger Last Name: ")
            pAge = int(input("Enter {}'s Age: " .format(pFirstName + " " + pLastName)))
            pGender = input("Enter {}'s Gender: " .format(pFirstName + " " + pLastName))  #Take Passenger Info and  verify data
            canBook = VerifyPassengerInfo(pFirstName + " " + pLastName,pAge,pGender.upper())
            if(canBook == False):
                print("\nPlease enter valid passenger details.") #If wrong data allow user to exit the booking
                cancelBook = input("Enter Y for yes,Press Enter to continue \nDo you want to cancel booking: ").upper()
            else:

                ShowAvailbeSeats() #Show which seats are available
                selectSeat = False
                while not selectSeat and cancelBook != "Y":  #To buy ticket
                    chooseSeat = input("Enter Seat Number: ")
                    selectSeat = CheckTicketAvaibility(chooseSeat,False) 
                    if(not selectSeat):
                        print("Enter Valid Seat No.")  #Allow user to cancel booking if desired seat not available
                        cancelBook = input("Enter Y for yes,Press Enter to continue \nDo you want to cancel booking: ").upper()
            if(cancelBook != "Y" and canBook == True):
                bus_info[CheckTicketAvaibility(chooseSeat,True)][2] = False
                toAdd = [pFirstName,pLastName,pAge,pGender[0].upper() + pGender[1:6],chooseSeat.upper(),FindTicket(chooseSeat),2000, date.today().strftime("%d-%b-%y") ,date.today() + timedelta(days=4)]
                allPassengers.append(toAdd)
                print(allPassengers)
                 #Add and complete booking
                print("\nCongratulations You have successfully booked your ticket!\n")
    
                print("\n--Your Trip and Ticket Details--")

                print(trip_info[0])
                print("Route: ",trip_info[1])
                print("Time: ",trip_info[2])
                print("Pickup Location: ",trip_info[3])    #Print Data to customer
                print("Drop off Location: ",trip_info[4])
                print("Journey Date: ",trip_info[5])

                print("\nFirst Name |   Last Name   | Age | Gender | Seat |  Ticket  | Amount |       Date       |   Expiration date ")
                for i in range(len(allPassengers)):                                                                      #0fname              1lname               2age                 3gender              4seat                   5ticket           6amount               7date buying                                     8date expiry
                    print("{0:10}   {1:10}    {2:3}    {3:6}    {4:4}   {5:7} {6:6}bdt        {7:10}           {8}".format(allPassengers[i][0],allPassengers[i][1],allPassengers[i][2],allPassengers[i][3],allPassengers[i][4],allPassengers[i][5],allPassengers[i][6],allPassengers[i][7],passenger_info[i][8]))
                    passenger_info.append(allPassengers[i])
    
        

def CancelReservation(seatNum): #Function to cancel Reservation
    for i in range(len(passenger_info)):
        if(passenger_info[i][4] == seatNum):  #Find which passenger wants to cancel
            confrim = input("Are you sure you want to cancel your reservation?\n*WE HAVE NO REFUND POLICY \nEnter Y to continue, to cancel press any key: ")
            if(confrim.upper() == "Y"): #Confermation Input
                for seat in range(len(bus_info)):
                    if(bus_info[seat][0] == seatNum):
                        bus_info[seat][2] = True    #Change value of bus ticket available to True
                        print("Your reservation have been succesfully canceled.")
                removed_data = passenger_info.pop(i)
                print("\nData Remove: \"\nFirst Name |   Last Name   | Age | Gender | Seat |  Ticket  | Amount |       Date       |   Expiration date ")  #Print data
                print("{0:10}   {1:10}    {2:3}     {3:6}   {4:4}   {5:7} {6:6}bdt        {7:10}              {8}".format(removed_data[0],removed_data[1],removed_data[2],removed_data[3],removed_data[4],removed_data[5],removed_data[6],removed_data[7],removed_data[8]))
                return
        elif(i == len(passenger_info) -1 and passenger_info[i][3] != seatNum):
            print("Seat enterted is invalid")
                        
def UpdateSeats(oldSeat,newSeat):
    for i in range(len(passenger_info)):
        if(passenger_info[i][4] == oldSeat):
            passenger_info[i][4] = newSeat
            passenger_info[i][6] += 500
    

def ChangeSeat(seatNum):
    for i in range(len(bus_info)):
        if(seatNum == bus_info[i][0]):
            if(bus_info[i][2] != False):   #Check if seat entered can be changed
                return print("Seat Number Enter not valid")         
    
    canBook =  False
    cancelBook = "" #Initial Variables
    ShowAvailbeSeats()
    while  canBook != True and cancelBook != "Y":
        chooseSeat = input("Enter seat number you want to change to: ")
        canBook = CheckTicketAvaibility(chooseSeat,False)    #Take input of which seat user wants
        if(not canBook):                                     #and check thats is valid
            print("Please Enter Valid Seat")
            cancelBook = input("Enter Y for yes,Press Enter to continue \nDo you want to cancel booking: ").upper()
    
    if(cancelBook != "Y"):
        UpdateSeats(seatNum,chooseSeat)
        for i in range(len(bus_info)):
            if(bus_info[i][0] == chooseSeat):
                 bus_info[i][2] = False
                        
            if(bus_info[i][0] == seatNum):
                bus_info[i][2] = True           #Output chages4
                print("Congratulations your seat {} has been changed to {} and you have been charged extra 500Bdt".format(seatNum,chooseSeat)) 


def ShowDatabase():
    print("\n1.Trip Info")
    print("2.Bus Details")
    print("3.Passenger List")
    print("4.For every Table")
    choice = int(input("Select Table: "))

    if(choice == 1):
        print("\n" + trip_info[0])
        print("Route: ",trip_info[1])
        print("Time: ",trip_info[2])
        print("Pickup Location: ",trip_info[3])    #Print Data to customer
        print("Drop off Location: ",trip_info[4])
        print("Journey Date: ",trip_info[5])
    elif(choice == 2):
        ShowAllSeats()
    elif(choice == 3):
        print("\nFirst Name |   Last Name   | Age | Gender | Seat |  Ticket  | Amount |       Date       |   Expiration date ")
        for x in range(len(passenger_info)):
            print("{0:10}   {1:10}    {2:3}     {3:6}   {4:4}   {5:7} {6:6}bdt        {7:10}              {8}" .format(passenger_info[x][0],passenger_info[x][1],passenger_info[x][2],passenger_info[x][3],passenger_info[x][4],passenger_info[x][5],passenger_info[x][6],passenger_info[x][7],passenger_info[x][8]))
    elif(choice == 4):
        print("\n" + trip_info[0])
        print("Route: ",trip_info[1])
        print("Time: ",trip_info[2])
        print("Pickup Location: ",trip_info[3])    #Print Data to customer
        print("Drop off Location: ",trip_info[4])
        print("Journey Date: ",trip_info[5])

        print("\n--Bus Info--")
        ShowAllSeats()

        print("\n--Passenger Info--")
        print("\nFirst Name |   Last Name   | Age | Gender | Seat |  Ticket  | Amount |       Date       |   Expiration date ")
        for x in range(len(passenger_info)):
            print("{0:10}   {1:10}    {2:3}     {3:6}   {4:4}   {5:7} {6:6}bdt        {7:10}              {8}" .format(passenger_info[x][0],passenger_info[x][1],passenger_info[x][2],passenger_info[x][3],passenger_info[x][4],passenger_info[x][5],passenger_info[x][6],passenger_info[x][7],passenger_info[x][8]))
    



#Menu
option = -1
print("\n---Welcome to Dhaka Chit Mini Bus Servies---")
print("CSC101 FINAL PROJECT by Mojtoba Zaman Mantaka")
while option != 0:
    print("             MENU                       \n")
    print("1.Book Ticket")
    print("2.Withdraw Reservation")
    print("3.Change Seat")
    print("4.Show Database")
    print("5.Find Specific Seat Status")
    print("0.Exit\n")
    option = int(input("Enter Choice: "))

    if(option == 1):
        passengerCount = int(input("How many Tickets do you wish to buy: "))
        BookTicket(passengerCount)
    elif(option == 2):
        #Print Passenger Details
        print("\nFirst Name | Last Name | Age | Gender | Seat | Amount |     Date     | Expiration date ")
        for x in range(len(passenger_info)):
            print("{0:10} {1:14}{2:3}    {3:6}   {4:4} {5:5}Bdt  {6:11}   {7}".format(passenger_info[x][0],passenger_info[x][1],passenger_info[x][2],passenger_info[x][3],passenger_info[x][4],passenger_info[x][5],passenger_info[x][6],passenger_info[x][7]))
        
        seatNum = input("Please enter the Seat No. :")
        CancelReservation(seatNum)
    elif(option == 3):
        seatNum = input("Please enter the Seat No. :")
        ChangeSeat(seatNum)
    elif(option == 4):
        ShowDatabase()
    elif(option == 5):
        seat = input("Enter Seat No. : ").upper()
        SeatStatus(seat)
    else:
        print("Please Choose a valid option.")
                  
