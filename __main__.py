from elevator import Elevator

#Elevator commute function which completes the functionality
def elevator_commute(elevator):
    print("Welcome to the ANZ Elevator!!")
    print("Number of floors for the elevator:", elevator.total_floors)
    print("Elevator is at floor #"+str(elevator.start_floor))
    print("Elevator is going",elevator.direction)
    print("Please enter the desired floors 1-",elevator.total_floors)
    elevator.floors_requested()

#Main function
def main():
    # elevator object instantiated from Elevator class
    elevator=Elevator(total_floors=5,start_floor=1,direction='up')
    elevator_commute(elevator)

    # Below are some additional Unit Tests
    # elevator=Elevator(total_floors=5,start_floor=5,direction='down')
    # elevator_commute(elevator)


    # elevator=Elevator(total_floors=5,start_floor=2,direction='up')
    # elevator_commute(elevator)
    #
    # elevator=Elevator(total_floors=5,start_floor=4,direction='down')
    # elevator_commute(elevator)
    #
    # elevator=Elevator(total_floors=5,start_floor=3,direction='up')
    # elevator_commute(elevator)

    # elevator=Elevator(total_floors=10,start_floor=3,direction='up')
    # elevator_commute(elevator)

    # elevator=Elevator(total_floors=10,start_floor=7,direction='down')
    # elevator_commute(elevator)

if __name__ == '__main__':
    main()