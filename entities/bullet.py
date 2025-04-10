# entities/bullet.py

# Import the Arcade library
import arcade
# Import the settings module for game constants
import settings

#Bullet class fired by the player.
#Inherits from arcade.Sprite.
class Bullet(arcade.Sprite):
    
    
    # Constructor: creates the bullet at a given position and sets its texture and speed.
    def __init__(self, start_x, start_y):
        # Call the parent constructor with no image
        super().__init__()

        # Create a glowing bullet shape (small vertical rectangle)
        self.texture = arcade.make_soft_square_texture(
            size=10,
            color=settings.YELLOW_ORANGE,
            outer_alpha=255,
            center_alpha=255
        )

        # Start position: typically from the player's current position
        self.center_x = start_x
        self.center_y = start_y

        # Vertical movement speed (moves upwards)
        self.change_y = settings.BULLET_SPEED

    # Called every frame. Moves the bullet upward.
    # Destroys the bullet if it goes off-screen.
    def update(self):
        # Move the bullet upwards
        self.center_y += self.change_y

        # Remove the bullet if it moves beyond the top of the screen
        if self.bottom > settings.SCREEN_HEIGHT:
            self.remove_from_sprite_lists()
