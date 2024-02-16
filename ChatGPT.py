import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the dimensions of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Set the size of the paddles and ball
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 80
BALL_WIDTH = 20

# Set the speed of the ball
BALL_SPEED = 5

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the caption of the screen
pygame.display.set_caption("Pong")

# Set the font for the score
font = pygame.font.Font(None, 36)

# Create the paddles
player1_paddle = pygame.Rect(50, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH,
                             PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(SCREEN_WIDTH / 2 - BALL_WIDTH / 2, SCREEN_HEIGHT / 2 - BALL_WIDTH / 2, BALL_WIDTH, BALL_WIDTH)

# Set the initial velocity of the ball
ball_velocity = [BALL_SPEED, BALL_SPEED]

# Set the initial scores
player1_score = 0
player2_score = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_paddle.move_ip(0, -5)
    if keys[pygame.K_s]:
        player1_paddle.move_ip(0, 5)
    if keys[pygame.K_UP]:
        player2_paddle.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        player2_paddle.move_ip(0, 5)

    # Move the ball
    ball.move_ip(ball_velocity[0], ball_velocity[1])

    # Check for collisions with the walls
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_velocity[1] = -ball_velocity[1]
    if ball.left <= 0:
        player2_score += 1
        ball_velocity = [BALL_SPEED, BALL_SPEED]
        ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    if ball.right >= SCREEN_WIDTH:
        player1_score += 1
        ball_velocity = [-BALL_SPEED, -BALL_SPEED]
        ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Check for collisions with the paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_velocity[0] = -ball_velocity[0]

    # Clear the screen
    screen.fill(BLACK)

    # Draw the paddles and ball
    pygame.draw.rect(screen, WHITE, player1_paddle)
    pygame.draw.rect(screen, WHITE, player2_paddle)
    pygame.draw.rect(screen, WHITE, ball)

    # Draw the score
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)