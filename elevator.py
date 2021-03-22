class Elevator:
    # Initializing the elevator behaviour variables
    def __init__(self,total_floors,start_floor,direction):
        #Total Floors for the Elevator
        self.total_floors=total_floors
        #Floor Starting position
        self.start_floor=start_floor
        #Initalizing the requested floor list
        self.floor_list=[]
        #Door close option indicating the end of floor inputs from passengers
        self.door_close=-1
        #Tracks current floor while elevator is in motion
        self.track_floor=start_floor
        #Initializing the floors variable
        self.floors=0
        #Direction whether 'up' or 'down'
        self.direction=direction

    #function which takes floor inputs from people and does input validations
    def floors_requested(self):
        while (self.floors != self.door_close):
            while True:
                try:
                    #floor inputs validation
                    self.floors = int(input("Enter Floor# (or) -1 for door close:"))
                except:
                    print("Please enter -1 for door close (or) desired floors 1-",self.total_floors)
                    continue
                if (self.floors not in range(1, self.total_floors + 1) and self.floors!=-1):
                    print("Please enter -1 for door close (or) desired floors 1-",self.total_floors)
                    continue
                break

            if (self.floors == self.door_close):
                break
            elif((self.direction=='up' and self.floors>self.start_floor and self.floors <= self.total_floors) or (self.direction == 'down' and self.floors<self.start_floor and self.floors > 0)):
                self.floor_list.append(self.floors)
        #depending on the direction, the elevator will travel either up or down
        if(self.direction=='up'):
            self.travel_up(self.start_floor,self.floor_list)
        elif(self.direction=='down'):
            self.travel_down(self.start_floor,self.floor_list)
    
    #travel up function planning the elevator steps
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
    
    #travel down function planning the elevator steps 
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
