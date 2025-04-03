# entities/player.py

# Import the Arcade library for working with sprites
import arcade

# Import global settings like screen size, movement speed, and colors
import settings

# Player class that represents the user's spaceship
class Player(arcade.Sprite):
    
    #Player class that represents the user's spaceship.
    #This class inherits from arcade.Sprite, allowing us to use built-in movement and drawing.

     # Constructor: creates and positions the player sprite.
    def __init__(self):
        
        # Call the parent class constructor with no texture for now
        super().__init__()

        # Create a soft-colored square as the player's placeholder texture
        # In future updates, this can be replaced with a sprite image
        self.texture = arcade.make_soft_square_texture(
            size=40,                  # Width and height of the square (in pixels)
            color=settings.CYAN,     # Use CYAN from our futuristic palette
            outer_alpha=255,         # Border opacity (fully opaque)
            center_alpha=255         # Center opacity (fully opaque)
        )

        # Position the player at the horizontal center, near the bottom of the screen
        self.center_x = settings.SCREEN_WIDTH // 2
        self.center_y = 60  # Slightly above the bottom

        # Set the base speed for left/right movement
        self.speed = settings.PLAYER_MOVEMENT_SPEED

    #Update the player's position. Called every frame by the game loop.
    def update(self):
    
        #Applies horizontal movement and prevents the player from going off-screen.
        
        # Move the player horizontally based on the velocity set by key presses
        self.center_x += self.change_x

        # Prevent the player from moving beyond the left edge
        if self.left < 0:
            self.left = 0

        # Prevent the player from moving beyond the right edge
        if self.right > settings.SCREEN_WIDTH:
            self.right = settings.SCREEN_WIDTH
