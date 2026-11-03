#This is My Project KAYODE TOLUWANI JOSEPH, Matric NO: F/ND/24/3450018
# WORKSHOP ENERGY COST ESTIMATION

#Introducing The Tool
print('WORKSHOP ENERGY COST ESTIMATION')


#First, asking for the amount of tools that will be recorded so as to be able to run the loop in that same amount of time
no_tools = int(input('How Many Tools Are You Going To Be Recording Today: '))

#These are The Lists That Store The Information collected from the user for processing 
tools = []
toolPower = []
time = []
kWh = [] 

#this is the normal nigerian price for electricity per kWh
localTarrif = 209.50

#for loop to ask the name of tools, power rating and the minutes they were used
for tool in range(no_tools):
    #collecting information from users
    toolName = input(f'Please Input The Name Of Number {tool+1}: ')
    power_rating = float(input(f'Please Input The Power Rating Of {toolName} In Watts: '))
    usedTime = int(input(f'Please Input The Amount Of Time Used On {toolName} In Minutes: '))

    #This is appending the information collected from the user to the lists that were created initially
    tools.append(toolName)
    toolPower.append(power_rating)
    time.append(usedTime)

#FUNCTIONS...
#function to convert Minutes To Hours For Suitable Calculations
def minToHr(min):
    min = int(min)
    return min/60

#function to calculate the energy using power and time
def energy(p, t):
    return p*t/1000

#this is the function to calculate the daily costs using the energy and the local tariff
def costCalc(kiloWatts):
    return kiloWatts * localTarrif

#function for estimated monthly energy consumption
def eMonthly(energy):
     return energy * 30

#function for estimated monthly costs
def monthlyCostFunc(monthlyEnergy):
     return monthlyEnergy * localTarrif
     

for savedTool, savedTime in zip(toolPower, time):
        timeConverted = minToHr(savedTime)
        result = energy(savedTool, timeConverted)
        kWh.append(result)


#storing all data to be printed to the user in a variable for flexibility
totalKWh = float(sum(kWh))
dailyCost = costCalc(totalKWh)
monthlyConsumption = eMonthly(totalKWh)
monthlyCost = monthlyCostFunc(monthlyConsumption)


#This is where we print the user output after all the information have been processed.

print("PROCESSED DATA FOR WORKSHOP ENERGY COST ESTIMATOR\n")

#ptinting the name of tool, minutes used and kWh for the day
for p, q, r in zip(tools, time, kWh):
    print(f'Your Tool: {p} Used For: {q} Minutes, Consumed: {r:.2f} kWh For The Day!')




report_data = f"\n DAILY INFORMATION \n The Accumulative Energy Consumed By All Tools For The Day Is: {totalKWh:.2f}kWh\n The Cost Of Energy Today Based On Local Tariff Is: #{dailyCost:.2f}\n\n MONTHLY INFORMATION\n The Estimated Accumulative Energy That Is Expected To Be Consumed Per Month Is: {monthlyConsumption:.2f}kWh \n The Estimated Monthly Cost Should Be: #{monthlyCost:.2f}\n Thank You!"

user_choice = int(input("\n Would You Like To Have A Text File Showing The Statistics \n If Yes Please Input 1 but If No Please Input 0 \n (Note: Picking 0 Will Just Allow The Statistics To Be Printed On The Terminal Alone): "))

if user_choice == 1 :
    #This is Using try and except as a safety net incase the file doesn't save...
    try:
        #working with python in-built open function to write to files 
        with open("workshop_report.txt", "w", encoding="utf-8") as f:
             f.write(report_data)
             print("\nReport saved successfully!")
    except Exception as e:
        print(f"Could not save file: {e}")

elif user_choice == 0:
    #printing Daily cumulative energy and Daily cost
    print('\n DAILY INFORMATION')
    print(f'The Accumulative Energy Consumed By All Tools For The Day Is: {totalKWh:.2f}kWh')
    print(f'The Cost Of Energy Today Based On Local Tariff Is: #{dailyCost:.2f}\n\n')

    #printing Monthly cumulative energy and Monthly costs
    print('MONTHLY INFORMATION')
    print(f'The Estimated Accumulative Energy That Is Expected To Be Consumed Per Month Is: {monthlyConsumption:.2f}kWh')
    print(f'The Estimated Monthly Cost Should Be: #{monthlyCost:.2f}')

else: 
     print("Invalid Input (You Can Either Input 1 or 0)")
     






