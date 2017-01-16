####Delainey Ackerman
####Intro to Game Programming & Intro to Modeling and Animation
####Assignment 2: Modular First Person Game Using Unreal Engine
####January 2017
####Group Members: Jack Evans, Michael Hindley, Omid Karimpour, and Luke Sanderson

#####[Full game found here] (https://github.com/dack91/Marsh-Effect/blob/master/Content/Maps/SUBMISSION.rar) unpack SUBMISSION.rar inside content->maps to play Marsh Effect from Unreal Engine 4. Lighting can be built after unpacking asset to remove "preview" shadow effects.

#####[Link for trailer video] (https://www.youtube.com/watch?v=vUgaSYutqI0)
#####[Link for demo video] (https://www.youtube.com/watch?v=xc1bckeZyOQ)

######Game Description:
*Marsh Effect* is a survival puzzle game played from a first person perspective. The player has crash landed on an alien island and must recover fragments of his ship scattered across the island to solve puzzles repairing the ship. Once all fragments are recovered and puzzles solved, the player gains access to the cockpit and wins the game. 

The player can only survive outside of the ship for a limited amount of time determined by his access to oxygen. To speed travel across the island and provide the player with an interesting gameplay feature, the player has a hovering speeder bike to race across beaches, swerve through forests, and jump across road gaps while searching for ship fragments. After collecting a ship fragment, the player returns to the ship and uses it to solve a puzzle and fix one aspect of the ship. If the player’s oxygen supply is depleted while outside the ship, the player and the speeder are immediately returned to the hanger of the ship.

In addition to the ship fragments, the player can also find specialized rocks around the island he can mine and use a workbench inside the ship to convert them to increase their oxygen levels outside of the ship. Spare oxygen tanks are also scattered across the island and can be picked up and immediately add a small resupply of oxygen while outside exploring.  


######Ship Fragments, Puzzles, & Rewards:
* Speeder Fragment
  * This missing part of the player's speeder is easy to located directly outside of the ship and is used to gain access to the speeder bike in the ship's hanger bay
  * There is no associated puzzle, simply a learning mechanic that picking up a fragment allows the player to gain an advantage in exploring the island
  * The reward is being able to drive the speeder bike which greatly increases the radius of exploration from the ship

* Engineering Fragment
  * The engine room in the ship is flooded with a toxic liquid, this fragment activates moving platforms in the room which allow the player to reach three pump control buttons
  * After activating the platforms with the fragment, the player must press all three buttons within a time limit to activate pumps and drain the flood
  * Once the flood is drained, a speed boost for the speeder bike is found on the bottom level of the engine room, allowing the player to use intervals of boosting to reach farther parts of the island

* Navigation Fragment
  * Finding this navigation dish activates a Simon Says type color matching game inside the ship
  * After repeating the color sequence to install the dish, the player gains access to a tracking system for all remaining ship fragments
  * A pillar of light will visually locate the remaining fragments, while the HUD will now display the player's distance from each fragment

* Control Fragment
  * This ignition key gains access to the control panel located just outside of the cockpit of the ship
  * Once accessed, the control panel is a Towers of Hanoi sequencing puzzle
  * After all control disks are moved to the final position of the puzzle, the cockpit door unlocks and the game is won

######My Contributions
For implementing all gameplay mechanics, game management, and UI I used Unreal Blueprints.
* Player State & Game State
  * I set up the MyPlayer Blueprint to have the base movement, looking, and jumping functionality of a first person game. Then I also used this blueprint as the main access point for all other blueprints to determine what the player has access to by tracking fragment inventory, his oxygen and health levels, and location and rotation within the world.
  * The OxygenManager Blueprint is the main game state manager I set up to monitor if the player is inside or outside of the ship and to effect the player's oxygen levels appropriately. Knowing that the game will always start with the player inside of the ship, I used a trigger on the hanger door opening to toggle between custom events determining indoor and outdoor behavior. While inside, the player regains oxygen up to max capacity, while outside, oxygen levels are depleted. Once oxygen levels hit empty, the player and all his items are reset to the ship hanger. This uses the spawn location of both the player and speeder bike saved in the MyPlayer blueprint to return everything to its initial position. 


* Ship Puzzles
  * The engine room puzzle consists of traversing moving platforms to reach three buttons located on stationary platforms and press all three buttons within the time limit. The puzzle is activated once the player finds the engine fragment. To implement the puzzle I used two separate blueprints. The first contains a single moving platform which in the game editor can be placed in the scene and can set the direction and distance the platform moves as well as the speed at which it moves. Any number of these platforms can be dropped into a scene to create any configuration of vertical and horizontal movement and speed. 
  * The main puzzle is handled by EngineFlood Blueprint and contains the toxic flood and three pump buttons. The player dies and resets to the hanger if any part of the player contacts the flood, this also resets all the buttons. Once the player presses the first button a timer sound starts playing indicated the time limit to push the remaining two buttons. Buttons can be pressed in any order, if the timer runs out an alarm sound plays and all buttons reset. Once the player presses all three buttons before the time expires, the flood drains through the floor and the speeder bike speed boost fragment can be picked up.

  * The Towers of Hanoi puzzle for the control room fragment similarly uses two blueprints. The first is simply HanoiDisk blueprint and is used as a class containing a disk number, peg location, and the physical model of the disk. The main blueprint is TowersOfHanoi which represents the puzzle as three arrays, one for each peg, which each array holding a stack of HanoiDisks. The puzzle setup initializes five disks of increasing size and adds them to the first peg array so that the largest peg is on the bottom of the stack and disks decrease in size moving to the top of the stack. The puzzle also initializes the control room Door Blueprint to start as locked. The disks and pegs are visible but unmovable until the player acquires the control fragment.
  * Once the control fragment is found, the puzzle unlocks and provides the Player with UI text indicating the player can use the 1, 2, and 3 keyboard keys to pick up disks from the three pegs and place them on another peg. The puzzle physically moves the top disk from the selected peg and places it on the top of the stack on the destination peg. The blueprint also monitors and enforces the rules of Hanoi not allowing the player to place a larger disk on top of a smaller disk. This is done by maintaining each peg array as pieces are moved and comparing the disk number attribute of the current top disk with the disk number value of the disk the player is trying to move. Once all disks are legally moved to the final peg the control room door is unlocked and the player can walk through to win the game.  

* Fragment Inventory and Functionality
  * Each of the fragment blueprints holds the fragment object which can simply be picked up by the player when he walks into the fragment. This updates the matching fragment inventory in MyPlayer and plays the same sound across all fragments indicating a successful pickup. The player's HUD, as discussed below, is also updated to reflect successful acquisition. Updating the MyPlayer fragment inventory then allows the player access to something on the ship previously locked to them. For instance, picking up the speeder fragment allows the player to mount and drive the previously locked speeder bike, while the engine fragment activates moving platforms and the pump control buttons.

* Player HUD Graphics and Functionality
  * Using Unreal's UMG blueprints for UI I used attributes from MyPlayer to display a helpful player HUD. The first main component was a progress bar representing the player's oxygen levels. The simple bar depletes as oxygen is used, as the player's oxygen reaches desperately low levels, the progress bar color fades from green to red, the entire screen is overlaid with and increasingly opaque red layer, and loud heartbeat and heavy breathing is played. 
  * At the top of the screen I implemented a sliding compass UI so as the player turns, the compass displays the player's direction. This is linked to MyPlayer by getting the player rotation while walking or the camera's rotation while the player pawn is possessed while driving the speeder bike. 
  * The other main UI component is the fragment inventory where I designed greyed out icons of each fragment, once the fragment is picked up by the player, the icon fills in with color corresponding to colored floor markers within the ship which aid the player in finding the part of the ship associated with each fragment.
  * I also implemented a separate UI blueprint to display help text throughout the game. This is used by puzzles to convey information about finding the fragment and by puzzles and active objects, like the elevator and mining rocks, as to what key to press to cause the appropriate action.  

* Elevators and Doors
  * The elevator blueprint allows the player to call the lift to whichever level of the ship the player is on, and then ride the lift up or down to any of the ship's three main levels. I used timeline animation inside Blueprints to smoothly transition the platform from one level to another, and trigger boxes to monitor what level the lift is on as well as what level the player is calling the lift to.
  * The doors use a simple trigger and timeline animation to open and close as the player approaches and leaves each door. Doors also have an attribute editable in the game editor to toggle whether they can be opened or not. This easily allowed us to lock doors and use them to permanently seal off a path inside the ship or to temporarily lock doors like the one going to the control room until the puzzle is solved. 

* Modular Kit for Ship Interior
  * I designed, modeled, UV mapped, and textured kit pieces to form the corridors and rooms within the ship. This includes the half-level pieces used in the engine room to create a mezzanine level with a slightly lower space for the toxic engine flood, and full level stairs and elevators to create any vertical configuration of the multi-level ship.

* Python Script for bulk FBX export from Maya
  * Using appropriate Maya commands I wrote a python script that can bulk edit and export models. The script can rename all selected items to a naming convention, then using that convention it will move each piece to the origin, delete object history, freeze transformations, make the object double-sided, export the model, and then return the object's previous settings and location within the scene in Maya. I used this script frequently while iterating the modular kit and then again while UV mapping and texturing the kit. 

* Sound Effects
  * I used effects from [Free Sound] (https://www.freesound.org) to provide feedback to the user. This includes feedback like a button sound when the player presses any of the three buttons in the engine room puzzle, a timer sound after pressing the first button to indicate that the player has a time limit to press the other buttons, an elevator sound after calling the lift so the player knows it is on its way, and a consistent success sound when ship fragments are picked up and when their associated puzzles are solved.

* Fragment Placement and Play Through Balance Testing
  * I placed the fragments and oxygen bonuses throughout the island and tested their placement as well as the ship puzzles to balance the game and make sure the player can reach all ship fragments and complete all puzzles. This also led to significant blueprint debugging as I found and fixed problems such as the UI for the speeder boost breaking after dying from oxygen deprivation two time. 

######Main Team Member Contributions
Michael and Luke were both very involved along with me to create and iterate the main game idea and mechanics. Luke then took on the huge task of creating the functionality of the speeder bike including the speed boost and the linked UI for the boost progress bar. Michael took on the bulk of the modeling and shader blueprints, creating the landscape, roads, trees, water shader, and terrain texture, as well as most of the in game models outside of the modular kit including the speeder bike and ship fragments. Jack delivered a great color sequencing Simon Says puzzle for the navigation fragment, and Omid provided a model for the exterior of the ship, oxygen conversion workbench, and engine room pump control buttons.
