# main.py

# Import the main Arcade library
import arcade

# Import game settings (screen size, colors, movement speed, etc.)
import settings

# Import game entities
from entities.player import Player
from entities.bullet import Bullet
from entities.enemy import Enemy

# Main game class for NeoGalaga
class NeoGalagaGame(arcade.Window):
    
    # Main game window that handles setup, updates, rendering, and input.
    
    def __init__(self):
        super().__init__(
            settings.SCREEN_WIDTH,
            settings.SCREEN_HEIGHT,
            settings.SCREEN_TITLE
        )

        # Set futuristic space background color
        arcade.set_background_color(settings.DARK_SPACE)

        # Initialize placeholders for sprite lists and player
        self.player = None
        self.player_list = None
        self.bullet_list = None
        self.enemy_list = None
        self.score = 0  # Player's score

        # Create a reusable text object to display the score
        # Use positional arguments (text, x, y, color, font_size) as required by current arcade version
        # Only 'font_name' can be passed as keyword argument here
        self.score_text = arcade.Text(
            "Score: 0",                                # Initial text displayed at game start
            10,                                        # X position (left margin of the screen)
            settings.SCREEN_HEIGHT - 30,              # Y position (slightly below top edge)
            settings.WHITE,                           # Text color (from color palette in settings)
            settings.FONT_SIZE_MEDIUM,                # Font size (defined in settings)
            font_name=settings.DEFAULT_FONT           # Font used (must be available or downloaded)
        )

    def setup(self):
        
        # Sets up the game state, initializes player, enemies, and bullets.
        
        # Create the player sprite and add it to the player list
        self.player = Player()
        # Set the player to be the center of the screen
        self.player_list = arcade.SpriteList()
        # Add the player to the sprite list for rendering and updating
        self.player_list.append(self.player)
        # Create a list for bullets and enemies
        self.bullet_list = arcade.SpriteList()
        # Create a list for enemies
        self.enemy_list = arcade.SpriteList()
        # Create enemies in a grid pattern across the screen
        for x in range(100, settings.SCREEN_WIDTH - 100, 100):
            # Create an enemy at the specified x position and a fixed y position
            enemy = Enemy(start_x=x, start_y=settings.SCREEN_HEIGHT - 80)
            # Set a downward movement speed for the enemy
            self.enemy_list.append(enemy)

    # Override the on_draw method to handle rendering
    def on_draw(self):
        # Called automatically by Arcade to draw the screen each frame.
        # Clear the screen and draw all sprites
        self.clear()
        # Draw the player, bullets, and enemies
        self.player_list.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()

        # Draw score text using the Text object (more efficient than draw_text)
        self.score_text.draw()  # Draw score in top-left corner

    # Override the on_update method to handle game logic
    def on_update(self, delta_time):
        # Called automatically each frame to update game logic.
        # Update the player, bullets, and enemies
        self.player_list.update()
        self.bullet_list.update()
        self.enemy_list.update()

        # Check for collisions between bullets and enemies
        for bullet in self.bullet_list:
            # Check if the bullet is still in the game world
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            # If the bullet hits an enemy, remove both the bullet and the enemy
            if hit_list:
                # Remove the bullet and all enemies it hit
                bullet.remove_from_sprite_lists()
                # Remove each enemy that was hit by the bullet
                for enemy in hit_list:
                    # Remove the enemy from the game world
                    enemy.remove_from_sprite_lists()
                    self.score += 100  # Add points per enemy destroyed

        # Update the score text to reflect the new score
        self.score_text.text = f"Score: {self.score}"

    # Override the on_key_press method to handle input
    def on_key_press(self, key, modifiers):
        # Handles key press events.
        # If the left or right arrow key is pressed, set the player's speed       
        if key in (arcade.key.LEFT, arcade.key.A):
            # Move left when the left arrow key or 'A' is pressed
            self.player.change_x = -self.player.speed
        # If the right arrow key or 'D' is pressed, set the player's speed
        elif key in (arcade.key.RIGHT, arcade.key.D):
            # Move right when the right arrow key or 'D' is pressed
            self.player.change_x = self.player.speed
        # If the space bar is pressed, create a bullet and add it to the bullet list
        elif key == arcade.key.SPACE:
            # Create a new bullet at the player's current position
            bullet = Bullet(self.player.center_x, self.player.top)
            # Set the bullet's speed and direction
            self.bullet_list.append(bullet)

    # Override the on_key_release method to handle input
    def on_key_release(self, key, modifiers):
        # Handles key release events to stop movement.
        
        # If the left or right arrow key is released, stop the player's movement
        if key in (arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D):
            # Stop the player when the left or right arrow key or 'A' or 'D' is released
            self.player.change_x = 0


# Only run the game if this script is executed directly
if __name__ == "__main__":
    game = NeoGalagaGame()   # Create game window
    game.setup()             # Set up game entities
    arcade.run()             # Start the game loop (calls on_draw, on_update, etc.)
