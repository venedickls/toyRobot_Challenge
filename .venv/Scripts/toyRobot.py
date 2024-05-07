class ToyRobot:
    def __init__(self):
        # Initialize robot's attributes
        self.x = None  # x-coordinate
        self.y = None  # y-coordinate
        self.direction = None  # direction
        self.grid_size = 5  # size of the grid

    def place(self, x, y, direction):
        # Place the robot at the specified position and direction
        if self._is_valid_position(x, y):  # Check if position is valid
            self.x = x
            self.y = y
            self.direction = direction.upper()  # Convert direction to uppercase
            print("Robot placed successfully.")
        else:
            print("Invalid placement command. Please ensure the coordinates are within the grid boundaries.")

    def move(self):
        # Move the robot one unit in the direction it is facing
        if self.direction == 'NORTH' and self.y < self.grid_size - 1:
            self.y += 1
        elif self.direction == 'EAST' and self.x < self.grid_size - 1:
            self.x += 1
        elif self.direction == 'SOUTH' and self.y > 0:
            self.y -= 1
        elif self.direction == 'WEST' and self.x > 0:
            self.x -= 1
        else:
            print("Cannot move. This movement will cause the robot to fall off the grid.")

    def left(self):
        # Rotate the robot 90° anticlockwise
        if self.direction == 'NORTH':
            self.direction = 'WEST'
        elif self.direction == 'WEST':
            self.direction = 'SOUTH'
        elif self.direction == 'SOUTH':
            self.direction = 'EAST'
        elif self.direction == 'EAST':
            self.direction = 'NORTH'

    def right(self):
        # Rotate the robot 90° clockwise
        if self.direction == 'NORTH':
            self.direction = 'EAST'
        elif self.direction == 'EAST':
            self.direction = 'SOUTH'
        elif self.direction == 'SOUTH':
            self.direction = 'WEST'
        elif self.direction == 'WEST':
            self.direction = 'NORTH'

    def report(self):
        # Output the robot's current position and direction
        print(f"Output: {self.x}, {self.y}, {self.direction}")

    def _is_valid_position(self, x, y):
        # Check if the given position is within the grid boundaries
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size


def main():
    robot = ToyRobot()
    while True:
        # Prompt the user to enter a command
        command = input("Enter command (place/move/left/right/report/exit): ").lower()
        if command == 'exit':
            print("Exiting program.")
            break
        elif command == 'place':
            # Prompt the user to enter position and direction
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            direction = input("Enter direction (NORTH/SOUTH/EAST/WEST): ").upper()
            robot.place(x, y, direction)
        elif command == 'move':
            robot.move()
        elif command == 'left':
            robot.left()
        elif command == 'right':
            robot.right()
        elif command == 'report':
            robot.report()
        else:
            print("Invalid command. Please enter a valid command.")


if __name__ == "__main__":
    main()
