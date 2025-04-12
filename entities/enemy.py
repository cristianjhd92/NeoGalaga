# entities/enemy.py

# Import necessary modules
import arcade
import settings

# Base class for enemies. Enemies descend or follow patterns.
class Enemy(arcade.Sprite):
    
    # Constructor: creates the enemy at a given position with a basic shape and color.
    def __init__(self, start_x, start_y):
        
        super().__init__()

        # Placeholder shape: soft-colored square
        self.texture = arcade.make_soft_square_texture(
            size=30,
            color=settings.MAGENTA,      # Enemy color (magenta for now)
            outer_alpha=255,
            center_alpha=255
        )

        # Position the enemy at the given starting coordinates
        self.center_x = start_x
        self.center_y = start_y

        # Placeholder movement (no movement yet)
        self.change_y = 0

    # Called every frame to update the enemy's behavior.
    def update(self, delta_time: float = 1/60):
        
        # For now, enemies are static. Movement will be added later.
        self.center_y += self.change_y

        # Future: remove or bounce if off screen, or implement movement pattern
