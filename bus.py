import pandas as pd 
import datetime 
import os
from Colour import Colour



def clear_screen():
	if os.name == "nt":
		os.system("cls") # just for Windows CMD / Powershell
	else:
		os.system("clear") # MacOS and Linux terminal





       
import csv
def bus_ticket():
    df=pd.read_csv("BusCreation.csv",index_col=0, )
    print(df)
    df = pd.DataFrame(columns=["Bus No", "Departure Date", "Departure Time", "Departure Town", "Arrival Town", "Booking Date", "Booking Time", "Seat"])
    no = int(input("Enter the last three digit of bus no:"))

    for _ in range(no):
        Bus_No =input('\nEnter Bus No: ')
        departure_date =input('\nEnter Departure Date(yyyy-mm-dd): ')
        departure_time =input('\nEnter Departure Time(hh:mm): ')
        departure_town = input('\nEnter Departure Town: ')
        arrival_town =input('\nEnter Arrival Town: ')
        booking_date = input('\nEnter Booking Date(yyyy-mm-dd): ')
        booking_time = input('\nEnter Booking Time(hh:mm): ')
        tic = input("\nWhich seat would you like to have (1-50) : ")
        print("Your ticket is booked")
        print("\n----------------------------------------------Booking Included----------------------------------------------- ")
        df1 = pd.DataFrame(data=[[Bus_No,departure_date,departure_time,departure_town,arrival_town,booking_date,booking_time,tic]],columns=["Bus No", "Departure Date", "Departure Time", "Departure Town", "Arrival Town", "Booking Date", "Booking Time", "Seat"])
        df = pd.concat([df,df1], axis=0)

        df.index = range(len(df.index))
        print(df)
        print('----------------------------------------------------------------------------------------------------------------')
        df.to_csv('BookingBus.csv')
        break

    
    seats = []    
    seats.append([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    seats.append([11,12,13,14,15,16,17,18,19,20   ])
    seats.append([21,22,23,24,25,26,27,28,29,30   ])
    seats.append([31,32,33,34,35,36,37,38,39,40   ])
    seats.append([41,42,43,44,45,46,47,48,49,50   ])
    print("")
    print("======================================")
    for row in seats:
        print(row)
    print("")
    print("======================================")       
    tic = int(input("\nEnter your seat no : "))
    if lst[tic-1]== tic:
        lst.pop(tic-1)
        fname.pop(tic-1)
        lname.pop(tic-1)
        lst.insert(tic-1,Colour.RED + 'B' + Colour.END)
        print("Your ticket is booked")
        bus_booking()
    else:
        print("seat is already booked try other seat")
        

   
    # Bus_No =input('\nEnter Bus No: ')
    # departure_date =str(input('\nEnter Departure Date(yyyy-mm-dd): '.format(Bus_No)))
    # departure_time =str(input('\nEnter Departure Time(hh:mm): '.format(Bus_No)))
    # departure_town = input('\nEnter Departure Town: ')
    # arrival_town =input('\nEnter Arrival Town: ')
    # booking_date = str(input('\nEnter Booking Date(yyyy-mm-dd): '))
    # booking_time = str(input('\nEnter Booking Time(hh:mm): '))
    # tic = int(input("\nWhich seat would you like to have (1-50) : "))
    


def cancel_ticket():
    tic = int(input("Enter seat no:"))
    if lst[tic-1]==tic:
        print("This seat is not booked")
    else:
        lst.pop(tic-1)
        lst.insert(tic-1,tic)
        print("Your ticket cancelled")
        bus_booking()



def check_ticket_detail():
    s = int(input("Enter your seat no:"))
    s = s-1
    if lst[s]==s+1:
        print("This seat is not booked")
        bus_booking()
    else:
        print("This seat is booked.")
        bus_booking()


def price(): 
    col_list = ["BusNo", "DepartureTown","DepartureDate","DepartureTime","ArrivalTown","TotalSeatAvailable","Fare"]
    df = pd.read_csv("BusCreation.csv", usecols=col_list)
    if s==df.loc[0].at["BusNo"]:
        print (df.loc[0].at["Fare"])
        exit()
    elif s==df.loc[1].at["BusNo"]:
        print (df.loc[1].at["Fare"])
        exit()
    elif s==df.loc[2].at["BusNo"]:
        print (df.loc[2].at["Fare"])
        exit()
    elif s==df.loc[3].at["BusNo"]:
        print (df.loc[3].at["Fare"])
        exit()
    else:
        print("Invalid Bus No !")
        exit()

def booking_history():
    print('==== View Booking History ====')
    no = input('\nEnter the Bus No: ')
    print("---------------------------------------------------------------------------------------------------------------")

    if no == "P001":
        df = pd.read_csv("BookingBus.csv")
        df.drop('Unnamed: 0', axis=1, inplace=True)
        df['Fare'] = "RM 25"
        print(df)
    if no == "P002":
        df = pd.read_csv("BookingBus.csv")
        df.drop('Unnamed: 0', axis=1, inplace=True)
        df['Fare'] = "RM 48"
        print(df)
    if no == "P003":
        df = pd.read_csv("BookingBus.csv")
        df.drop('Unnamed: 0', axis=1, inplace=True)
        df['Fare'] = "RM 55"
        print(df)
    if no == "P004":
        df = pd.read_csv("BookingBus.csv")
        df.drop('Unnamed: 0', axis=1, inplace=True)
        df['Fare'] = "RM 56" 
        print(df)


lst=list()
for i in range(1,51):
    lst.append(i)
    fname=list()
for j in range(1,51):
    fname.append(j)
    lname=list()
for k in range(1,51):
    lname.append(k) 
def bus_booking():
    print('\n------------------------------------------------------------')    
    print('                      BUS BOOKING                           ')
    print('------------------------------------------------------------')    
    print("       1. Book Bus Ticket")
    print("       2. Check the Bus Ticket status")
    print("       3. Cancel the ticket")
    print("       4. Check detail of ticket that is booked")
    print("       5. Check for the Price")
    print("       6. View Booking HIstory")
    print("       0. Exit")
    print('------------------------------------------------------------\n') 

    choice = int(input("Enter your option :"))
    exitFromHere = False
    while exitFromHere == False:
        if choice == 0:
            pass
            # user_loggedin(userName)
        elif choice == 1:
            bus_ticket()
            bus_booking()
        elif choice == 2:
            for k in lst:
                print(k,end=" ")
            break
            bus_booking()

        elif choice == 3:
            tic = int(input("Enter seat no:"))
            if lst[tic-1]==tic:
                print("This seat is not booked")
        
            else:
                lst.pop(tic-1)
                lst.insert(tic-1,tic)
                print("Your ticket cancelled")
                print("\nThank You and Goodbye !!\n")
                input('\nPress ANY key to continue.\n')
                exit()
        elif choice == 4:
            s = int(input("Enter your seat no:"))
            s = s-1
            if lst[s]==s+1:
                print("This seat is not booked")
                bus_booking()
            else:
                print("This seat is booked.")
                bus_booking()  
                
                check_ticket_detail()
                
                
        elif choice == 5:
            s=input("Enter your Bus No:")
            col_list = ["BusNo", "DepartureTown","DepartureDate","DepartureTime","ArrivalTown","TotalSeatAvailable","Fare"]
            df = pd.read_csv("BusCreation.csv", usecols=col_list)
            if s==df.loc[0].at["BusNo"]:
                print (df.loc[0].at["Fare"])
                exit()
            elif s==df.loc[1].at["BusNo"]:
                print (df.loc[1].at["Fare"])
                exit()
            elif s==df.loc[2].at["BusNo"]:
                print (df.loc[2].at["Fare"])
                exit()
            elif s==df.loc[3].at["BusNo"]:
                print (df.loc[3].at["Fare"])
                exit()
            else:
                print("Invalid Bus No !")
                exit()
        elif choice == 6:
            booking_history()
            print("---------------------------------------------------------------------------------------------------------------")
            # Stop temporarily before re-displaying the menu
            input('\nPress ANY key to continue.')
            exit()
        elif choice == '':
            bus_booking()
            exitFromHere == True
bus_booking()


