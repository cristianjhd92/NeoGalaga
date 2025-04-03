# main.py

# Import the main Arcade library
import arcade

# Import game settings (screen size, colors, movement speed, etc.)
import settings

# Import the Player class from the entities folder
from entities.player import Player

#Main game class for NeoGalaga.
class NeoGalagaGame(arcade.Window):
    
    #Inherits from arcade.Window to manage window behavior, game loop, and rendering.

    #Constructor: sets up the game window and background color.
    def __init__(self):
        
        super().__init__(
            settings.SCREEN_WIDTH,     # Width of the game window
            settings.SCREEN_HEIGHT,    # Height of the game window
            settings.SCREEN_TITLE      # Title shown on the window bar
        )

        # Set the futuristic space background color
        arcade.set_background_color(settings.DARK_SPACE)

        # Placeholder for the player sprite (initialized in setup)
        self.player = None

    # Set up the initial game state (called once at the beginning).
    def setup(self):
        
        #Used to create the player, enemy lists, bullets, score, etc.

        # Create an instance of the Player class
        self.player = Player()

    # Called every frame to draw all game elements on the screen.
    def on_draw(self):
        
        arcade.start_render()     # Clear the screen and prepare for drawing
        self.player.draw()        # Draw the player sprite

    #Called every frame to update game logic (movement, collisions, etc.).
    def on_update(self, delta_time):
        
        #delta_time = time passed since last frame (not used here yet).

        self.player.update()      # Update player position based on velocity

    # Called when the player presses a key.
    def on_key_press(self, key, modifiers):
        
        #Used to start movement in a direction.
        
        # Set the player's velocity based on the key pressed
        if key in (arcade.key.LEFT, arcade.key.A):
            self.player.change_x = -self.player.speed
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.player.change_x = self.player.speed

    # Called when the player releases a key.
    def on_key_release(self, key, modifiers):
       
        #Stops movement in that direction.
        
        # Stop the player's horizontal movement when the key is released
        if key in (arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D):
            self.player.change_x = 0


# Run this only if the file is executed directly
if __name__ == "__main__":
    game = NeoGalagaGame()   # Create the game window
    game.setup()             # Initialize game content (player, etc.)
    arcade.run()             # Start the main game loop (render + update)
