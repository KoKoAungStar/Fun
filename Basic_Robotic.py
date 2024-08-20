import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the robot (astrobot)
robot = turtle.Turtle()
robot.shape("triangle")
robot.color("white")
robot.penup()  # Don't draw when the robot moves
robot.speed(1)

# Function to move the robot forward
def move_forward():
  robot.forward(10)

# Function to turn the robot left slightly
def turn_left():
  robot.left(10)

# Function to turn the robot right slightly
def turn_right():
  robot.right(10)

# Function to simulate obstacle detection
def detect_obstacle():
  # Simulate an obstacle at position (100, 100)
  if robot.distance(100, 100) < 50:
    return True
  return False

# Main loop
while True:
  if detect_obstacle():
    print("Obstacle detected! Adjusting course.")
    turn_right()  # Adjust direction to avoid the obstacle
  else:
    move_forward()  # Keep moving forward
