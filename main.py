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

        # Placeholder for the enemy sprite list (initialized in setup)
        self.bullet_list = None

        # Placeholder for the enemy sprite list (initialized in setup)
        self.enemy_list = None


    # Set up the initial game state (called once at the beginning).
    def setup(self):
        
        # Used to create the player, enemy lists, bullets, score, etc.

        # Create an instance of the Player class
        self.player = Player()

        # Set the player's initial position to the center of the screen
        self.bullet_list = arcade.SpriteList()


        self.enemy_list = arcade.SpriteList()

        # Create a basic grid formation (5 enemies in a row)
        for x in range(100, settings.SCREEN_WIDTH - 100, 100):
            enemy = Enemy(start_x=x, start_y=settings.SCREEN_HEIGHT - 80)
            self.enemy_list.append(enemy)



    # Called every frame to draw all game elements on the screen.
    def on_draw(self):
        
        arcade.start_render()     # Clear the screen and prepare for drawing
        self.player.draw()        # Draw the player sprite
        self.bullet_list.draw()   # Draw all bullets in the bullet list
        self.enemy_list.draw()    # Draw all enemies in the enemy list


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
        elif key == arcade.key.SPACE:
            bullet = Bullet(self.player.center_x, self.player.top)
            self.bullet_list.append(bullet)
        
        # Update the player and enemy lists
        self.enemy_list.update()



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
