# Marsh-Effect
Collaborative MA/MSc modular FPS game

Michael Hindley

Intro to Game Programming & Intro to Modeling and Animation

Assignment 2: Modular First Person Game Using Unreal Engine

January 2017

Group Members: Jack Evans, Delainey Ackerman, Omid Karimpour and Luke Sanderson 


#####[Full game found here] (https://github.com/dack91/Marsh-Effect/blob/master/Content/Maps/SUBMISSION.rar) unpack SUBMISSION.rar inside content->maps to play Marsh Effect from Unreal Engine 4. Lighting can be built after unpacking asset to remove "preview" shadow effects.

#####[Link for trailer video] (https://www.youtube.com/watch?v=vUgaSYutqI0)
#####[Link for demo video] (https://www.youtube.com/watch?v=xc1bckeZyOQ)


 Game Description: 
Marsh Effect is a first person survival puzzle game with a sci-fi setting. In the story of the game the Player ship has crashed landed on an alien planet and the Player must repair their ship by exploring the island and collecting fragments from their ship, so they can repair its systems and leave the planet.
The primary mechanic of the game is that that the outside world of the alien planet is toxic and the player can only spend so long outside. To this effect the player must travel as quickly as they can across the map to collect fragments. This features adds a layer of tension and excitement to the gameplay. To this effect the player can also unlock a speeder bike with an unlockable speed boost to travel across the map faster. When the player runs out of oxygen they are teleported back to the ship and do not lose any progress in the game.      
Lastly the player can also mine rocks that can be found around the island, the more rocks the player mines the slower their oxygen is depleted outside the ship. 

Fragments, Puzzles and Rewards: 

Speeder Fragment: 
This is generally the first fragment the player finds as it directly outside the ship. It unlocks accesses to the speeder bike in the ships hanger and greatly increases the players range. 

Engineering Fragment: 
The bottom level of the ship is flooded with a dangerous pink acid that the ship is leaking the player must find this fragment outside the ship so they can complete a timed platform puzzle to activate the pumps in the engine room to drain the fluid. Once this is done the player can collect the speed boost fragments for the speeder bike which further increases the players range.  

Navigation: 
Once this fragment is found the player can complete a simion says style game on the top floor of the ship. Once this is done the player can activate pillars of lights across the maps that will show the location of any reaming fragments. 

Control Fragment: 
This is the key to the ship and is the hardest fragments to get as the player must travel a significant distance to get it. Once the player has this fragment, the player must complete a tower of Hanoi puzzle to unlock the ship control room and finish the game. 

My Contributions: 
I was mainly responsible for the art assets in the game and implementing art assets and visual effects into unreal. 
Landscape: 
I was reasonable for creating the landscape and its shaders as well the road system that runs across the entire level. I primarily used World machine and Zbrush to generate a detail set of creation maps (height map, Splat Map, Flow Map) I imported this into Unreal and set up the landscape shader. The landscape shader features 4 layers (rock,Grass,Sand and flow overlay) I also put a tint effect on each layer to give extra control over the finial look of the terrain. 
Trees, Grass: 
I used speed tree and photoshop to create the model and textures for these assets as a result they auto generate LOD’s as well as integrated wind effects which we sadly were not able to implement in the final version of the game. 
Rocks: 
These were a very simple asset to create, I primarily sculpted them in Zbrush  and used its decimation and UV master to quickly make low res UV unwrapped model, I cleaned this up in Maya made sure the scale was correct and exported it to unreal. Where it was implemented as a minable resource. 
Speeder: As this was one of our main models, which we knew the player would see up close a lot I put a lot of detail into the model, sadly I was not able to complete the texturing of this model in time for the finished game.  
Water shader: this was one of my most technical contributions to the project, the shader was fairly complex and feature many customizable elements. The shader also features two animated normal maps which were blended together to create a complex wave animation the shader also had real-time tessellation based on this normal map animation all of the input variables such as the speed and blending power were customizable in the shader.  


Fragments: I also modelled all of the fragments that the player collected, sadly these do not have a complex texture however a put a lot of care into making a detailed model that fit the look and function of the fragment in the game. 

Team Member contributions: 
Delainey and Luke where very active and involved with the development and the refinement of the game. Delainey was reasonable for creating the modular kit for inside the ship as well as many of the primary mechanics of the game such as the oxygen system the engine room and towers of Hanoi puzzle. The player HUD and UI, sound effects and functionality for inside the ship.  Luke Was very involved with the creation of the speeder bike and its complex systems, as well as other complex systems associated with the speed boost UI. Omid helped me create the models he provided the model for the exterior of the ship as will as the oxygen work bench and engine pump buttons. Jack was responsible for the simion says puzzle associated with the navigation fragment.                            

