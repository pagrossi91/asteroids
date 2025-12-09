SCREEN_WIDTH = 1280     # width of the game screen
SCREEN_HEIGHT = 720     # height of the game screen

PLAYER_RADIUS = 20      # radius of the player's ship
LINE_WIDTH = 2          # width of the lines that draw the player's ship

PLAYER_TURN_SPEED = 300 # how fast the player turns
PLAYER_SPEED = 200      # how fast the player moves

# Set asteroid properties
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# Set shooting properties
SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3