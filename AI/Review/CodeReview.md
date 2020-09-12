# Bullets.java  
>   
> Man, those are some weird and interesting bullet types! I have no idea what some of these do. The 'water' ones, for example, are liquid, yet they have a weird knockback. Do they have some sort of friction? The oil ones have a weird drag, but no damage. Does it go through them, or something?  
> The "normal" bullets, are a strange metal, with a strange shrink Y, with a normal lifetime, and no weird knockback or anything.  
> Now I have to come up with some imaginative name for this! Oh yeah, guess what this is!  
> Well, obviously then you'd come up with a power rating. I have no idea how to rate these, so I'll just number them.  
> Oh yeah, this is for arma 3!  
> So there you have it! Your first experience with Project: Magus! I hope you enjoyed it, because it's going to be a long ride as we try to make this game as good as we possibly can!  
>   
# Items.java  
>   
> The above code has created an array of objects. These objects will serve as the items that you will be able to create and add to your game. You can think of them as "variants" of each other, where each variant has a specific "cost" tied to it.  
> As you can see, in the above example, there are five different types of "copper". Within these copper types are a bunch of copper itself, as well as specific values for each different "value" of copper (thin, regular, heavy, thick and extra-thick). These values are things like "how easily can you slice it", "how much can you bend it" and so on.  
> The first thing you need to do is create a method to create these objects. The class will have a static method called create() that takes in an argument of what kind of object to create, and the constructor takes the values from the object constructor. It looks like this:  
> private static function create(type)  
> Also, you need to be able to access these objects anywhere in your code.  
>
# Event Listener something
> The .on method is used to register an event listener. The listener will be executed when the associated event is triggered. For example:  
>   
> Entity e1 = ...  
> e1.on("added"。Event event)  
> This would add a listener to the 'added' event. When the listener is triggered, the method .on("added", ...) will be executed.  
>   
> The first argument of .on is always the name of the event. All other arguments are arbitrary objects that you would usually pass into a method when it is triggered. The name of the object is arbitrary, but it would be good to follow a convention so that you don't miss any arguments. The easiest way to do this is to prefix all of your methods with an upper case letter. So the lower bound of your method argument names is .STRING().  
>   
> The second argument of .on is the object that initiated the event. This will almost always be the Entity class. The exception to this would be network related events. In these cases, the argument would be null.  
>   
> The third argument is always the trigger that occurred for this event to occur. This can be a constant (e.g. A trigger that always occurs or a static event that always occurs is represented as 'S' in the following code), an expression (e.g. the value of x that caused the event to occur), or a method call (e.g. the method y was called, with argument z).  
>   
> Finally, the .on method takes an arbitrary number of arguments. These arguments are passed to the method when this event is triggered.  
>   
> The following code registers an event listener:  
>   
> e1.on("added", tile, S.tile, 10)  
> This code registers the event listener with any tile that is added. Whenever a tile is added, the tile added event will be triggered. The first parameter of this method is the type of the event. In this case, 'added' is tile. The second parameter is the name of the event. S.tile will always be the instance of the TileStone tile. The third parameter is the index of the event. The event listener will be triggered with an event argument of type Event. The following code is executed when this event is triggered:  
> tile.addTo(10, 1)  
> Here, tile is the object of type Tile. The call addTo(10, 1) is interpreted as a tile addition.  
>   
> The .remove method removes a previously registered event listener. The argument to .remove is the object that was the listener. The listener is completely removed once the method is called on that object. For example:  
> e2.on("added", tile, S.tile, 10)  
> e3.on("added", tile, S.tile, 10)  
> e4.on("added", tile, S.tile, 10)  
> e1.on("added", tile, S.tile, 10)  
> e2.on("removed", e3, S.tile, 10)  
> e3.on("removed", e4, S.tile, 10)  
> e4.on("removed", e1, S.tile, 10)  
> This code registers the listener on all four sides of a square. Whenever a tile is added to any side, two events will be triggered: one for that side and one for the opposite side. This is done by using the syntax 'e1.on(S.tile, e2, 10)'. Here S is a Symbol that represents all four sides of the square. Since there are two e's, this expression will trigger two events when the event occurs: one for each side of the square. This can be used to create more complex behaviors by chaining together multiple expressions.  
> The .remove method will always remove all of the events for a given object. For example, calling e2.on("removed", e3, S.tile, 10) will trigger only the event for side 1 of the square, since e3.on("removed", e4, S.tile, 10) has already been called and removed. In the case where all of the objects are removed, the .on method will trigger nothing.  
>   
> An event is automatically deleted during the process of garbage collection. The following code, for example, is equivalent to the code in the previous section:  
>   
> e2.on("added", tile, S.tile, 10)  
> e3.on("added", S.tile)  
> e4.on("added", S.tile)  
> e1.on("added", tile, S.tile, 10)  
>   
> The first three lines are exactly the same as the previous section. The exception is that the fourth line will be executed instead, and it adds a tile to the square.  
> The built-in symbols are shown below.  
>   
> Symbol Name Description  
>   
> A constant that will be returned to the user when the .on method is used to register an event listener.  
>   
> A constant that will be returned to the user when the .off method is used to unregister an event listener.  
>   
> A constant that will be returned to the user when the .has method is used to check if an event listener is still registered. If the method returns true, it means that the event listener is still active.  
>   
> The following code shows how to create an event listener that executes a function when an entity is created. The code will also remove the listener once the entity is destroyed.  
>   
> In this section, you will learn how to check if an event listener is still active and how to react to that event in a game loop.  
>   
> This example shows how to create a simple event listener. The listener checks if the listener is still active and, if it is, prints a message to confirm that the listener is still active.  
>   
> This section will explain how to create, destroy, and use event listeners.  
>   
> It is possible to use the .on method to check if an event is present, and if so, execute a certain function. This can be useful for creating small notifications, or checking if an event has occurred before executing a different code path.  
>   
> The .on method returns a Boolean value. This value will be true if the event is present, and false if the event is not present.  
>   
> The .off method can be used to remove an event listener. If the .off method is called when an event listener is attached, the attached function will not be executed.  
>   
> The use of the .off method can cause strange effects in some code paths, since it can remove both an event listener and the associated code path. In this situation, it is best to always use the .on method to attach an event listener, instead.  
>   
> The .trigger method can be used to trigger an event when it occurs, similar to .on. Instead of attaching a function to the event, however, the method will attach a function to the event instead.  
> The .trigger method will not remove a previously attached event listener. The attached function will not be executed.  
>   
> The following code shows how to create a listener that executes a function when the player moves their mouse over an entity.   
> In this section, you will create a simple shooter game to learn the usage of the different type of events in HTML5.   
> The game is very simple. It uses the mouse events to move the ship, and the left mouse button to fire the main gun.  
> The main source files for this section are listed below.  
>   
> It is important to understand that events can be nested. In other words, an event can trigger another event. This is very useful when you need something to occur when a specific condition is met.  
> The game loop is responsible for updating the game state. The game loop calls the rendering function under the rendering section and updates the game world based on the changes to the game state.  
> The main game loop function is update(). The function iterates over all entities to see if they should be rendered. For each entity, the update function iterates over all child entities, and renders them.  
>   

>   
# Later that day  
> As you might have guessed, you can only use the API inside of a node.js environment.  
> With this out of the way, you can start making your game work.  
>   
* You say "ITS A FUCKING JAVA"  
> Your game will run on Java, you can't be fucking lazy.  
> You start by creating your object:  
> new Game(screen, "OpenGL", "1.3", 30, 10, GraphicsEnvironment.  
> You make a call to your game:  
> frame = frame - 1;  
> if (frame % 60 == 0)  
> graphics.setColor(Color.yellow);  
> else if (frame % 30 == 0)  
> graphics.setColor(Color.blue);  
> You call the link() method on the Game object:  
> g.link();  
> Now, the game can start!  
> You draw a black circle on the screen, and give it a random size:  
> circle = new Circle(size);  
> graphics.setColor(Color.black);  
> graphics.fill(circle);  
> frame = frame - 1;  
> You create a new Bullet object, and give it a random speed and direction:  
> bullet = new Bullet(Math.random(), Math.random(), 1.0, 1.0);  
> Now, your game is ready to run! Call the run() method on the game object:  
> g.run(frame * 0.1F);  
> This will start the game playing, and stopping when it reaches the end of the level.  
> Good luck!  
* You say "what the fuck ?"  
> You push the arrow key in the opposite direction of your bullet:  
> graphics.fill(bullet.worldY, bullet.worldX, bullet.world width, bullet.world height);  
> You shoot and kill yourself:  
> bullet.x = (width/2); bullet.y = (height/2);  
> You start again, and try to move your bullet:  
> graphics.fill(bullet.worldX, bullet.worldY, bullet.world width, bullet.world height);  
> bullet.x = (width/2 - width/2); bullet.y = (height/2 - height/2);  
> You move right, then up:  
> graphics.fill(bullet.worldX, bullet.worldY, bullet.world width, bullet.world height);  
> bullet.x = (width/2 + width/2); bullet.y = (height/2 + height/2);  
> You move left, then down:  
> graphics.fill(bullet.worldX, bullet.worldY, bullet.world width, bullet.world height);  
> bullet.x = (width/2 - width/2 - width/2); bullet.y = (height/2 - height/2 - height/2);  
> This is really annoying, the movement is not smooth.  
> You maybe you could make a triangle mesh instead of a quad one, to calculate the movement better.  
> You can take a look at the movement code to see how it could be done.  
> You can also try to reduce the amount of frames taken to draw each frame. The movement code is not the most optimized you've seen, some parts of it could be simplified. It is taking more than 10 frames to draw each one of the bullet's frames.  
> In fact this is not a problem to be solved now, you need to reach the end of the level before drawing all the bullets. So, let's begin the design phase.  
> The first thing that comes to mind is the bullets are too fast. The player doesn't react well. So, what can be done about it?  
> You can slow down the movement of the bullet. How? By making them move downward. The bullet's movement is not smooth anyway, so this will make no difference.  
> Another possibility is to use a mesh that produce less movement, like a quadratic one. This could work, but again the bullet's movement would be not smooth.  
> The last possibility is to draw the bullet as a sprite, and change the bullet's speed. You can then use a Fader to fade out the old bullet sprites, making way for the new, faster ones. This will also allow you to have different types of bullets, like ones that fly up and those that go down.  
> You want to choose the last solution, because it is the easiest. The only thing left to do it code the new movement.  
> You create a new object, a SpriteBatch, which will contain all the sprites that you want to create. You decide to have a bullet sprite, a speed up sprite, a bullet sprite with no speed, a bullet sprite with a slow down and a bullet sprite with no slow down:  
> SpriteBatch batch;  
> public void create()  
> You create and initialize a new Bullet object:  
> Bullet bullet;  
> You create the bullet sprite with different speeds:  
> Sprite bulletSpeedUp;  
> Bullet bulletSmooth;  
> bulletSmooth.setSpeed(2);  
> bulletSmooth.setSize(20, 20);  
> bulletSmooth.setFillStyle(Bullet.FillStyle.OUTSIDE, Bullet.COLOR);  
> bulletSmooth.setAlpha(0.4f);  
> bulletSmooth.setFont(new Font("Arial", 12));  
> bulletSmooth.setDrawColor(Color.BLACK);  
> bulletSmooth.draw('-');  
> bulletSmooth.setFillStyle(Bullet.FillStyle.INSIDE, Bullet.COLOR);  
> bulletSmooth.draw('-');  
> bullet.speed = bulletSpeedUp.getCurrentSpeed();  
> bullet.setSize((int)bullet.getSize().width, (int)bullet.getSize().height);  
> You create the bullet with no speed:  
> Bullet bulletNoSpeed;  
> You create the bullet with slow down:  
> Bullet bulletSlowDown;  
> bulletSlowDown.setSpeed(bulletSlowDown.getSpeed()+2);  
> bulletSlowDown.setSize(20, 20);  
> bulletSlowDown.setFillStyle(Bullet.FillStyle.OUTSIDE, Bullet.COLOR);  
> bulletSlowDown.setDrawColor(Color.BLACK);  
> bulletSlowDown.draw('-');  
> bulletSlowDown.setAlpha(0.2f);  
> You create the bullets with no slow down:  
> Bullet bulletNoSlowDown;  
> You create the bullet with a speed of 0:  
> Bullet bulletNoSpeed;  
> bulletNoSpeed.setSize(20, 20);  
> bulletNoSpeed.setFillStyle(Bullet.FillStyle.OUTSIDE, Bullet.COLOR);  
> bulletNoSpeed.setAlpha(0.0f);  
> You create the bullet:  
> Bullet bulletAll;  
> You add the objects created to the sprite batch:  
> batch.add(bullet);  
> batch.add(bulletNoSpeed);  
> batch.add(bulletNoSlowDown);  
> batch.add(bulletSmooth);  
> batch.add(bullet);  
> You display the sprite batch:  
> spriteBatch.draw(batch);  
> This solution is promising, you have 4 types of bullets, and you can add more in the future.  
> But... what's this? You have some strange effects in the game!  
> For example, when you touch an enemy, you see a strange kind of bullet appear out of thin air.  
> This must be caused by the Fader, so you decide to turn it off:  
> fader.setAll(false);  
> And now? What's this? Some strange things start to appear in the game! For example, when you touch the screen, you see some kind of... writing?  
> You can't really tell, but it seems that the words seem to be moving:  
> This is very strange, did you implement a bug in your program?  
> Fixing this bug will be one of the purposes of your next coding, but for now...  
> Well, it's better than nothing.  
>   


