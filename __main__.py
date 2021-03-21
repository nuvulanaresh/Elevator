from elevator import Elevator

#Elevator commute function which completes the functionality
def elevator_commute(elevator):
    print("Welcome to the ANZ Elevator!!")
    print("Number of floors for the elevator:", elevator.total_floors)
    print("Elevator Starting Floor:", elevator.start_floor)
    print("Please enter the desired floors 1-",elevator.total_floors)
    print("Enter Floor# as -1 when you are done")
    elevator.floors_requested()

#Main function
def main():
    #elevator object instantiated from Elevator class
    elevator=Elevator(total_floors=10,start_floor=5,direction='up')
    elevator_commute(elevator)
    #
    # elevator=Elevator(total_floors=5,start_floor=4,direction='down')
    # elevator_commute(elevator)
    #
    # elevator=Elevator(total_floors=5,start_floor=1,direction='up')
    # elevator_commute(elevator)
    #
    # elevator=Elevator(total_floors=5,start_floor=1,direction='up')
    # elevator_commute(elevator)


if __name__ == '__main__':
    main()