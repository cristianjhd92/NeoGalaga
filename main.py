# main.py
# Import the Arcade library
import arcade

# Import global settings (screen size, colors, etc.)
import settings


class NeoGalagaGame(arcade.Window):
    
    #Main game class. Inherits from arcade.Window and controls the game loop,
    #including drawing, updating, and input handling.

    def __init__(self):
        
        #Constructor. Initializes the game window and background color.
        
        super().__init__(
            settings.SCREEN_WIDTH,      # Window width (from settings.py)
            settings.SCREEN_HEIGHT,     # Window height
            settings.SCREEN_TITLE       # Window title
        )

        # Set the background color using the DARK_SPACE from the color palette
        arcade.set_background_color(settings.DARK_SPACE)

        # Game objects will be initialized in the setup() method
        # (e.g., player sprite, enemy list, score, etc.)

    def setup(self):
        
        # Set up the game variables. This method is called once when the game starts,
        # and can be reused to reset the game state.

        pass  # To be filled with initial game logic (e.g., create sprites)

    def on_draw(self):
        
        # Render the screen. Called automatically by the Arcade library every frame.
        
        arcade.start_render()  # Clear the screen and start drawing

        # All draw calls (sprites, UI, background elements) will go here


# Main function: starts the game only if this file is run directly
if __name__ == "__main__":
    game = NeoGalagaGame()  # Create game window instance
    game.setup()            # Initialize game variables and sprites
    arcade.run()            # Run the main game loop (calls on_draw continuously)
