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
        # Find the index of the opening parenthesis
        paren_index = command.find('(')
        # Extract the substring before the opening parenthesis
        command_str = command[:paren_index].strip()  # Remove leading/trailing whitespace

        if command_str == 'exit':
            print("Exiting program.")
            break
        elif command_str == 'place':
            # Extract the coordinates and direction
            comma_index = command.find(',')
            x_start = paren_index + 1
            x_end = comma_index
            y_start = comma_index + 2  # Skip the comma and space
            y_end = command.find(',', y_start)
            direction_start = y_end + 3  # Skip the comma, space, and single quote
            direction_end = command.find("'", direction_start)

            # Extract and convert the coordinates
            x = int(command[x_start:x_end].strip())
            y = int(command[y_start:y_end].strip())
            direction = command[direction_start:direction_end].strip().upper()

            robot.place(x, y, direction)
        elif command_str == 'move':
            robot.move()
        elif command_str == 'left':
            robot.left()
        elif command_str == 'right':
            robot.right()
        elif command_str == 'report':
            robot.report()
        else:
            print("Invalid command.")
            break


if __name__ == "__main__":
    main()
