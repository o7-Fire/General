const mineflayer = require('mineflayer')
const { mineflayer: mineflayerViewer } = require('prismarine-viewer')
const { pathfinder, Movements, goals: { GoalNear } } = require('mineflayer-pathfinder')
const navigatePlugin = require('mineflayer-navigate')(mineflayer);
var bloodhoundPlugin = require('mineflayer-bloodhound')(mineflayer);
const pvp = require('mineflayer-pvp').plugin
var sleep = require('sleep');
const vec3 = require('vec3')
var args = process.argv.slice(2);

function itemToString (item) {
	if (item) {
		return `${item.name} x ${item.count}`
	} else {
		return '(nothing)'
	}
}

const bot = mineflayer.createBot({
  host: 'shdif.myserver.gs',
  username: (args[0]),
  version: '1.16.5',
  //port: 28136
})
const mcData = require('minecraft-data')(bot.version)
var pi = 3.14159;
const RANGE_GOAL = 1

navigatePlugin(bot);
bot.loadPlugin(pathfinder)
bot.loadPlugin(pvp)
bloodhoundPlugin(bot);
bot.bloodhound.yaw_correlation_enabled = true;

const defaultMove = new Movements(bot, mcData)

/*
bot.once('spawn', () => {
  mineflayerViewer(bot, { port: 8090, firstPerson: true }) // port is the minecraft server port, if first person is false, you get a bird's-eye view
})
*/
bot.on('onCorrelateAttack', function (attacker,victim,weapon) {
	if ((victim.displayName || victim.username).startsWith("NBot")) {
		if ((attacker.displayName || attacker.username).startsWith("NBot")) {
			
		} else {
			//bot.chat(`${(victim.displayName || victim.username)} is getting attacked by ${(attacker.displayName || attacker.username)}`)
			bot.pvp.attack(attacker)
		}
	}
});

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
	
	/*
	if (message === "line up") {
		const target = bot.players[username].entity
		if (!target) {
		  bot.chat("I don't see you !")
		  return
		}
		const { x: playerX, y: playerY, z: playerZ } = target.position

		bot.pathfinder.setMovements(defaultMove)
		bot.pathfinder.setGoal(new GoalNear(playerX + args[0].substr(-3), playerY, playerZ, RANGE_GOAL))
	}
	*/
	
	if (message.startsWith("equipblock ")) {
		const mcData = require('minecraft-data')(bot.version)
		let itemsByName
		if (bot.supportFeature('itemsAreNotBlocks')) {
			itemsByName = 'itemsByName'
		} else if (bot.supportFeature('itemsAreAlsoBlocks')) {
			itemsByName = 'blocksByName'
		}
		var blocktoequip = message.replace("equipblock ", "");
		bot.equip(mcData[itemsByName][blocktoequip].id, 'hand', (err) => {
		if (err) {
			bot.chat(`unable to equip ${blocktoequip}: ${err.message}`)
		} else {
			bot.chat(`equipped ${blocktoequip}`)
		}
		})
	}
	
	if (message.startsWith("abuild ")) {
		const messagesplit = message.split(" ") // below, 0 -1 1
		const referenceBlock = bot.blockAt(bot.entity.position.offset(messagesplit[1], messagesplit[2], messagesplit[3]))
		bot.on('move', pb)
		function pb () {
			bot.placeBlock(referenceBlock, vec3(0, 0, 1), (err) => {
				if (err) {
					console.log('cant')
				}
			})
		}
	}
	
	if (message === "attackm") {
		const target = bot.players[username].entity
		looptarget()
		function looptarget () {
			setTimeout(function() {
				bot.navigate.to(target.position);
				
				bot.attack(target)
				looptarget()
			}, 1000)
		}
	}
	
	if (message === "tellinventory") {
		items = bot.inventory.items()
		const output = items.map(itemToString).join(', ')
		if (output) {
			bot.chat(output)
		} else {
			bot.chat('empty')
		}
	}

})
	
/*
bot.on('end', function () {
	console.log("Disconnected. Waiting 5 seconds")
	sleep.sleep(5);
	const shell = require('shelljs')
	shell.exec('node main.js')
	throw new Error("rejoining");
});
*/

// Log errors and kick reasons:
bot.on('kicked', console.log)
bot.on('error', console.log)
