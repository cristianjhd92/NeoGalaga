# entities/player.py

# Import the Arcade library for working with sprites
import arcade

# Import global settings like screen size, movement speed, and colors
import settings


class Player(arcade.Sprite):
    
    # Player class that represents the user's spaceship.
    # Inherits from arcade.Sprite and handles movement and boundaries.
    

    def __init__(self):
        
        # Constructor: creates and positions the player sprite.
        # Passes the texture correctly as a positional argument.

        # Create a soft-colored square texture to use as the player ship
        texture = arcade.make_soft_square_texture(
            size=40,                  # Width and height of the square (in pixels)
            color=settings.CYAN,     # Use CYAN from the futuristic palette
            outer_alpha=255,         # Border opacity (fully opaque)
            center_alpha=255         # Center opacity (fully opaque)
        )

        # Initialize the sprite with the created texture (as positional argument) and scale
        super().__init__(texture, scale=1.0)

        # Position the player horizontally centered, near the bottom of the screen
        self.center_x = settings.SCREEN_WIDTH // 2
        self.center_y = 60  # Y-position above the screen bottom

        # Set the base speed for left/right movement
        self.speed = settings.PLAYER_MOVEMENT_SPEED

    def update(self):
        
        # Update the player's position. Called every frame.
        # Handles horizontal movement and enforces screen boundaries.
        
        # Apply horizontal movement
        self.center_x += self.change_x

        # Prevent movement beyond the left edge
        if self.left < 0:
            self.left = 0

        # Prevent movement beyond the right edge
        if self.right > settings.SCREEN_WIDTH:
            self.right = settings.SCREEN_WIDTH
