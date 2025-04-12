# main.py

# Import the main Arcade library
import arcade

# Import game settings (screen size, colors, movement speed, etc.)
import settings

# Import the Player class from the entities folder
from entities.player import Player

# Import the Bullet class from the entities folder
from entities.bullet import Bullet

# Import the Enemy class from the entities folder
from entities.enemy import Enemy


# Main game class for NeoGalaga.
class NeoGalagaGame(arcade.Window):
    
    # Inherits from arcade.Window to manage window behavior, game loop, and rendering.

    # Constructor: sets up the game window and background color.
    def __init__(self):
        super().__init__(
            settings.SCREEN_WIDTH,     # Width of the game window
            settings.SCREEN_HEIGHT,    # Height of the game window
            settings.SCREEN_TITLE      # Title shown on the window bar
        )

        # Set the futuristic space background color
        arcade.set_background_color(settings.DARK_SPACE)

        # Initialize object placeholders (they will be created in setup())
        self.player = None
        self.bullet_list = None
        self.enemy_list = None

    # Set up the initial game state (called once at the beginning).
    def setup(self):
        
        # Used to create the player, enemy list, bullet list, etc.
        # Create an instance of the Player class
        self.player = Player()

        # Initialize bullet and enemy sprite lists
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Create a basic grid formation (5 enemies in a row)
        for x in range(100, settings.SCREEN_WIDTH - 100, 100):
            enemy = Enemy(start_x=x, start_y=settings.SCREEN_HEIGHT - 80)
            self.enemy_list.append(enemy)

    # Called every frame to draw all game elements on the screen.
    def on_draw(self):
        
        # Handles drawing everything on the screen each frame.
        arcade.start_render()         # Clear the screen and prepare for drawing
        self.player.draw()            # Draw the player sprite
        self.bullet_list.draw()       # Draw all bullets in the bullet list
        self.enemy_list.draw()        # Draw all enemies in the enemy list

    # Called every frame to update game logic (movement, collisions, etc.).
    def on_update(self, delta_time):
        
        # Handles game logic updates like movement and collisions.
        # Update player, bullets, and enemies
        self.player.update()
        self.bullet_list.update()
        self.enemy_list.update()

        # Check for bullet-enemy collisions
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            # If the bullet hits any enemies, remove them
            if hit_list:
                bullet.remove_from_sprite_lists()  # Remove the bullet
                for enemy in hit_list:
                    enemy.remove_from_sprite_lists()  # Remove each enemy hit

    # Called when the player presses a key.
    def on_key_press(self, key, modifiers):
        
        #Used to start movement or fire a bullet when a key is pressed.
        # Set the player's velocity based on the key pressed
        if key in (arcade.key.LEFT, arcade.key.A):
            self.player.change_x = -self.player.speed
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.player.change_x = self.player.speed

        # Fire a bullet when the spacebar is pressed
        elif key == arcade.key.SPACE:
            bullet = Bullet(self.player.center_x, self.player.top)
            self.bullet_list.append(bullet)

    # Called when the player releases a key.
    def on_key_release(self, key, modifiers):
    
        #Stops horizontal movement when a key is released.
        if key in (arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D):
            self.player.change_x = 0


# Run this only if the file is executed directly
if __name__ == "__main__":
    game = NeoGalagaGame()   # Create the game window
    game.setup()             # Initialize game content (player, bullets, enemies)
    arcade.run()             # Start the main game loop (render + update)
