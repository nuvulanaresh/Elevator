class Elevator:
    # Initializing the elevator variables
    def __init__(self,total_floors,start_floor,direction):
        #Total Floors for the Elevator
        self.total_floors=total_floors
        #Floor Starting position
        self.start_floor=start_floor
        #Initalizing the floor list
        self.floor_list=[]
        #Door close option indicating the end of inputs from people
        self.door_close=-1
        #Tracks current floor while elevator is in motion
        self.track_floor=start_floor
        #Initializing the floors
        self.floors=0
        #Direction whether 'up' or 'down'
        self.direction=direction

    #function which takes inputs from
    def floors_requested(self):
        while (self.floors != self.door_close):
            while True:
                try:
                    self.floors = int(input("Enter Floor#:"))
                except ValueError:
                    print("Please enter valid input")
                    continue
                break
            if (self.floors == self.door_close):
                break
            elif((self.direction=='up' and self.floors>self.start_floor) or (self.direction == 'down' and self.floors<self.start_floor)):
                self.floor_list.append(self.floors)

        if(self.direction=='up'):
            self.travel_up(self.start_floor,self.floor_list)
        elif(self.direction=='down'):
            self.travel_down(self.start_floor,self.floor_list)

    def travel_up(self,start_floor,floor_list):
        self.track_floor = self.start_floor
        self.floor_list.sort()
        for i in self.floor_list:
            floor_diff = abs(self.track_floor - i)
            for j in range(floor_diff):
                print("UP_1")
            print("OPEN_DOOR")
            print("CLOSE_DOOR")
            self.track_floor = i

    def travel_down(self,start_floor,floor_list):
        self.track_floor = self.start_floor
        self.floor_list.sort()
        for i in self.floor_list[::-1]:
            floor_diff = abs(self.track_floor - i)
            for j in range(floor_diff):
                print("DOWN_1")
            print("OPEN_DOOR")
            print("CLOSE_DOOR")
            self.track_floor = i

