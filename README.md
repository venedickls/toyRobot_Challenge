![image](https://github.com/venedickls/toyRobot_Challenge/assets/43608289/cff34a5e-4677-4e56-b7a0-fb3153f7f709)# Toy Robot Simulator (Challenge)

This is a simple Python implementation of a toy robot simulator. The simulator allows you to place a toy robot on a 5x5 grid tabletop and issue commands to move and rotate it.

## Instructions

1. Clone the repository to your local machine:


2. Navigate to the directory: .venv/Scripts/toyRobot.py #actual code


3. Run the Python script:


4. Follow the on-screen instructions to interact with the toy robot simulator. You can issue commands such as `place`, `move`, `left`, `right`, `report`, and `exit`.

## Commands

- `place(x, y, direction)`: Place the robot at the specified position (`x`, `y`) and direction (`NORTH`, `SOUTH`, `EAST`, `WEST`).
- `move()`: Move the robot one unit in the direction it is facing.
- `left()`: Rotate the robot 90° anticlockwise.
- `right()`: Rotate the robot 90° clockwise.
- `report()`: Output the current position and direction of the robot.
- `exit`: Exit the program.

## Example
![image](https://github.com/venedickls/toyRobot_Challenge/assets/43608289/3e68bac7-aea5-4095-9766-7b17f877639a)

Enter command (place/move/left/right/report/exit): place(0, 0, 'NORTH')

Enter command (place/move/left/right/report/exit): move()

Enter command (place/move/left/right/report/exit): report()

Output: 0, 1, NORTH

Enter command (place/move/left/right/report/exit): place(0, 0, 'NORTH')

Enter command (place/move/left/right/report/exit): left()

Enter command (place/move/left/right/report/exit): report()

Output: 0, 0, WEST

Enter command (place/move/left/right/report/exit): place(1, 2, 'EAST')

Enter command (place/move/left/right/report/exit): move()

Enter command (place/move/left/right/report/exit): move()

Enter command (place/move/left/right/report/exit): left()

Enter command (place/move/left/right/report/exit): move()

Enter command (place/move/left/right/report/exit): report()

Output: 3, 3, NORTH

Enter command (place/move/left/right/report/exit): 


## Requirements

- Python 3.x
