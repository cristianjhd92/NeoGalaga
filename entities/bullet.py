# entities/bullet.py

# Import the Arcade library
import arcade

# Import the settings module for game constants
import settings

# Create a Bullet class that inherits from arcade.Sprite
class Bullet(arcade.Sprite):
    # Bullet class fired by the player.
    # Inherits from arcade.Sprite.
    def __init__(self, start_x, start_y):
        
        # Constructor: creates the bullet at a given position and sets its texture and speed.
        super().__init__()
        # Create a glowing bullet shape (small vertical square)
        self.texture = arcade.make_soft_square_texture(
            # Width and height of the square (in pixels)
            size=10,
            # Use YELLOW_ORANGE from the futuristic palette
            color=settings.YELLOW_ORANGE,
            # Outer and center opacity (fully opaque)
            outer_alpha=255,
            # Center opacity (fully opaque)
            center_alpha=255
        )

        # Set initial position from the player's ship
        self.center_x = start_x
        self.center_y = start_y

        # Move upward at a fixed speed
        self.change_y = settings.BULLET_SPEED

    # Override the update method to handle bullet movement
    def update(self, delta_time: float = 1 / 60):
        
        # Called every frame. Moves the bullet upward.
        # Compatible with SpriteList update (accepts delta_time).
        # Move the bullet upwards
        self.center_y += self.change_y

        # Remove the bullet if it moves beyond the top of the screen
        if self.bottom > settings.SCREEN_HEIGHT:
            # Remove the bullet from the sprite list
            self.remove_from_sprite_lists()
