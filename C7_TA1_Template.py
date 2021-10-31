# Import pygame library
import pygame
pygame.init() 
# Create a game screen and set its title
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Breakout Game")
# Define the RGB color combinations of rectangle objects
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,150,0)
YELLOW = (255,255,0)
# Create a paddle and a ball rectangle objects
paddle = pygame.Rect(300,500,60,10)
ball = pygame.Rect(200,250,10,10)
# Define variables to track ball and paddle movement
ballx = -1
bally = -1
paddlex = 2
# Create red, orange and yellow bricks using list comprehension
bricksR=[pygame.Rect(10 + i* 100,60,80,30) for i in range(7)]
bricksO=[pygame.Rect(10 + i* 100,100,80,30) for i in range(7)]
bricksY=[pygame.Rect(10 + i* 100,140,80,30) for i in range(7)]

# Create a variable to store player score and name it as "score", assign 0 as its value



# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill(DARKBLUE)
    # Check for user input to move the paddle
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x<540: 
                paddle.x+=2
        if event.key == pygame.K_LEFT:
            if paddle.x>0:
                paddle.x-=2
                
    pygame.draw.line(screen, WHITE, [0, 38], [600, 38], 2)
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    
    # Insert code to display score text here



    
    # Update x and y position of the ball on screen 
    ball.x = ball.x + ballx
    ball.y = ball.y + bally
    # Limiting ball movement on screen along x-axis
    if ball.x >= 590:
      ballx = -ballx
    if ball.x <= 10:
      ballx = -ballx
    # Limiting ball movement on screen along y-axis
    if ball.y >= 590:
      bally = -bally
    if ball.y <= 10:
      bally = -bally
    pygame.draw.rect(screen,WHITE ,ball)
    # Check for paddle and ball collision and change the ball direction if they collided
    if paddle.collidepoint(ball.x, ball.y):
        bally = -bally
    
    # Draw Red bricks on screen 
    for i in bricksR:
        pygame.draw.rect(screen,RED,i)
        
    # Code for red brick and ball collision here
    
        # Remove red brick using "collidepont()" function
        
            
            # Reverse ball direction upon collision
            
            
            # Increase player score by 3
            
            
    pygame.time.wait(8)
    pygame.display.flip()       
pygame.quit(  )