class rover:
    def __init__(self):
        """All the variables are initialised here."""
        self.x = 0
        self.y = 0
        self.orientation = 'N'
        self.left = 'L'
        self.right = 'R'
        self.move = 'M'
        self.north = 'N'
        self.south = 'S'
        self.east = 'E'
        self.west = 'W'
        self.instruction = ''
        self.xmax = 0
        self.ymax = 0

    def set_values(self, xmax, ymax, x, y, orientation, instruction):
        """This function gets the input from main and sets all the variables of class."""
        self.xmax = xmax
        self.ymax = ymax
        self.x, self.y, self.orientation = x, y, orientation
        self.instruction = instruction

    def execute_instruction(self):
        """This function iterates over each of the instruction and calls the respective command function."""
        for steps in self.instruction:
            if steps is self.left:
                self.rotate_left()
            elif steps is self.right:
                self.rotate_right()
            elif steps is self.move:
                self.move_forward()
            else:
                print("Wrong Instruction.")

    def move_forward(self):
        """Moves the rover based on the present orientation the the rover.
           Assuming that the rover won't move after the plateau edge is reached."""
        if self.orientation == self.north and self.y < int(self.ymax):
            self.y = self.y + 1
        elif self.orientation == self.east and self.x < int(self.xmax):
            self.x = self.x + 1
        elif self.orientation == self.south and self.y > 0:
            self.y = self.y - 1
        elif self.orientation == self.west and self.x > 0:
            self.x = self.x - 1

    def rotate_left(self):
        """Turns the rover left."""
        if self.orientation == self.north:
            self.orientation = self.west
        elif self.orientation == self.east:
            self.orientation = self.north
        elif self.orientation == self.south:
            self.orientation = self.east
        elif self.orientation == self.west:
            self.orientation = self.south

    def rotate_right(self):
        """Turns the rover right."""
        if self.orientation == self.north:
            self.orientation = self.east
        elif self.orientation == self.east:
            self.orientation = self.south
        elif self.orientation == self.south:
            self.orientation = self.west
        elif self.orientation == self.west:
            self.orientation = self.north

    def final_position(self):
        """Returns the final position."""
        return self.x, self.y, self.orientation


def main():
    xmax, ymax = input("Grid size: " ).split()
    rovers_list = []
    final_position = []
    for item in range(2):
        r = rover()
        x, y, orientation = input("Rover's coordinates and orientation: ").split()
        instruction = input("Instructions for rover: ")
        r.set_values(xmax, ymax, int(x), int(y), orientation.upper(), instruction.upper())
        rovers_list.append(rover)
        r.execute_instruction()
        position = r.final_position()
        final_position.append(position)
    #count = 1
    for x,y,z in final_position:
        print (x,y,z)
        
        #count+=1

if __name__ == '__main__':
    main()