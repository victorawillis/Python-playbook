# import math library
import math

# declare constants
paintcan_area = 350
paintcan_time = 6
hourly_labor = 62.25

# allow user to repeatedly perform calculation
option = 'y'
while (option == 'y'):

    # ask for surface area (sqft)
    check = 1
    while (check == 1):
        print("Enter the surface area to be painted in sqft: ")
        try:
            surface_area = float(input())
            check = 0
            
            if (surface_area <= 0):
                print("Input must be greater than zero.")
                check = 1
                
        except ValueError:
            check = 1
            print("Input must be a number.")

    # ask for price per gallon of paint
    check = 1
    while (check == 1):
        print("Enter the paint price per gallon: ")
        try:
            paint_price = float(input())
            check = 0

            if (paint_price <= 0):
                print("Input must be greater than zero.")
                check = 1
        except ValueError:
            print("Input must be a number.")

    # calculate pricing
    hours = ( surface_area / paintcan_area ) * paintcan_time
    gallons = math.ceil(surface_area / paintcan_area)
    paint_total = gallons * paint_price
    labor = hours * hourly_labor
    job_total = labor + paint_total

    # print results
    print("Gallons of paint:", gallons)
    print("Hours of labor: %.2f" % round(hours, 2))
    print("Cost of paint: $%.2f" % round(paint_total, 2))
    print("Labor charges: $%.2f" % round(labor, 2))
    print("Total cost of the paint job: $%.2f" % round(job_total, 2))
    print("\nEnter 'y' to perform another estimate.")
    option = input()
    
