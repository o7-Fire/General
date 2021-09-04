const mineflayer = require('mineflayer')
const { mineflayer: mineflayerViewer } = require('prismarine-viewer')
const { pathfinder, Movements, goals: { GoalNear } } = require('mineflayer-pathfinder')
var sleep = require('sleep');

const bot = mineflayer.createBot({
  host: 'ery1hnc7.aternos.me',
  username: 'NexityBot',
  version: '1.16.5',
  //port: 28136
})

var pi = 3.14159;
const RANGE_GOAL = 1
bot.loadPlugin(pathfinder)
const mcData = require('minecraft-data')(bot.version)
const defaultMove = new Movements(bot, mcData)

/*
bot.once('spawn', () => {
  mineflayerViewer(bot, { port: 8090, firstPerson: true }) // port is the minecraft server port, if first person is false, you get a bird's-eye view
})
*/

bot.on('chat', (username, message) => {
  if (username === bot.username) return
  if (message.startsWith("say")) {
	bot.chat(message.replace("say ", ""))
  }
  if (message === "bot come") {
	const target = bot.players[username].entity
    if (!target) {
      bot.chat("I don't see you !")
      return
    }
    const { x: playerX, y: playerY, z: playerZ } = target.position

    bot.pathfinder.setMovements(defaultMove)
    bot.pathfinder.setGoal(new GoalNear(playerX, playerY, playerZ, RANGE_GOAL))
  }
  if (message === "xzc") {
    
  }
})

bot.on('end', function () {
    console.log("Disconnected. Waiting 5 seconds")
    sleep.sleep(5);
     const shell = require('shelljs')
    shell.exec('node main.js')
    throw new Error("rejoining");
});

// Log errors and kick reasons:
bot.on('kicked', console.log)
bot.on('error', console.log)
