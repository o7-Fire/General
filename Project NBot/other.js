const mineflayer = require('mineflayer')
const { mineflayer: mineflayerViewer } = require('prismarine-viewer')
const { pathfinder, Movements, goals: { GoalNear } } = require('mineflayer-pathfinder')
const navigatePlugin = require('mineflayer-navigate')(mineflayer);
var bloodhoundPlugin = require('mineflayer-bloodhound')(mineflayer);
const pvp = require('mineflayer-pvp').plugin
var sleep = require('sleep');
const vec3 = require('vec3')
var args = process.argv.slice(2);

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
}

function isEquivalent(a, b) {
    // Create arrays of property names
    var aProps = Object.getOwnPropertyNames(a);
    var bProps = Object.getOwnPropertyNames(b);

    // If number of properties is different,
    // objects are not equivalent
    if (aProps.length != bProps.length) {
        return false;
    }

    for (var i = 0; i < aProps.length; i++) {
        var propName = aProps[i];

        // If values of same property are not equal,
        // objects are not equivalent
        if (a[propName] !== b[propName]) {
            return false;
        }
    }

    // If we made it this far, objects
    // are considered equivalent
    return true;
}

function itemToString (item) {
	if (item) {
		return `${item.name} x ${item.count}`
	} else {
		return '(nothing)'
	}
}

function isEmpty(obj) {
	return Object.keys(obj).length === 0;
}

const bot = mineflayer.createBot({
  host: 'ery1hnc7.aternos.me',
  username: (args[0]),
  version: '1.16.5',
  port: 28136
})

var botprefix = "NBot" // change this to something else if you want to change the name in main.py
const mcData = require('minecraft-data')(bot.version)
var pi = 3.14159;
var isRoamingEnabled = false
var others = {}
var friendly = {}
var uselessvar = 0
var uselessvar2 = 0

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
	if (!isEmpty(friendly)) {
		if ((victim.displayName || victim.username).startsWith(botprefix)) {
			if ((attacker.displayName || attacker.username).startsWith(botprefix)) {
				
			} else {
				//bot.chat(`${(victim.displayName || victim.username)} is getting attacked by ${(attacker.displayName || attacker.username)}`)
				bot.pvp.attack(attacker)
			}
		}
	}
});

bot.on('physicTick', () => {
	if (isRoamingEnabled) {
		if (bot.time.time - uselessvar2 > 80) {
			uselessvar2 = bot.time.time
			var tpos = bot.entity.position
			bot.pathfinder.stop()
			bot.pathfinder.setMovements(defaultMove)
			bot.pathfinder.setGoal(new GoalNear(tpos.x + getRandomInt(0, 10) - 5, tpos.y, tpos.z + getRandomInt(0, 10) - 5))
		}
	}
})
	
bot.on('physicTick', () => {
	var friendly2 = {}
	var others2 = {}
	Object.entries(bot.players).forEach(([k,v]) => {
		try {
			playerpos = v.entity.position
			if (v.username.startsWith(botprefix) && v.username !== bot.username) {
				friendly2[v.username] = playerpos.toString()
				//friendly2.push({key: v.username, value: (playerpos.x.toFixed(), playerpos.y.toFixed(), playerpos.z.toFixed())})
			} else if (v.username !== bot.username) {
				others2[v.username] = (playerpos.x.toFixed(), playerpos.y.toFixed(), playerpos.z.toFixed())
				//others2.push({key: v.username, value: (playerpos.x.toFixed(), playerpos.y.toFixed(), playerpos.z.toFixed())})
			}
		} catch (error) {
			// do nothing
		}
	})
	//console.log(`uselessvar: ${uselessvar}, friendly: ${JSON.stringify(friendly2)}, others: ${JSON.stringify(others2)}`)
	// check if theres any nearby allies
	if (!isEmpty(others) && isEmpty(friendly) && uselessvar >= 22) {
		var botpos = bot.entity.position
		//console.log(botpos)
		//bot.chat(`botneedhelp ${botpos.x.toFixed()} ${botpos.y.toFixed()} ${botpos.z.toFixed()}`)
		uselessvar = 0
	} else if (!isEmpty(others) && isEmpty(friendly) && uselessvar === 20) {
		uselessvar = uselessvar + 1
		Object.entries(others2).forEach(([k,v]) => {
			try {
				var botpos = bot.entity.position
				var thevpos = bot.players[k].entity.position
				if (thevpos.x.toFixed() - botpos.x.toFixed() > 0) {
					if (thevpos.z.toFixed() - botpos.z.toFixed() > 0) {
						var posX = thevpos.x.toFixed() - botpos.x.toFixed()
						var posZ = thevpos.z.toFixed() - botpos.z.toFixed()
						if (posX < 7) {
							if (posZ < 7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed() + 7, botpos.y.toFixed(), botpos.z.toFixed() + 7, 1))
							} else {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed() + 7, botpos.y.toFixed(), botpos.z.toFixed(), 1))
							}
						} else {
							if (posZ < 7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed(), botpos.y.toFixed(), botpos.z.toFixed() + 7, 1))
							} else {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed(), botpos.y.toFixed(), botpos.z.toFixed(), 1))
							}
						}
					} else { 
						var posX = thevpos.x.toFixed() - botpos.x.toFixed()
						var posZ = botpos.z.toFixed() - thevpos.z.toFixed()
						if (posX < 7) {
							if (posZ < 7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed() + 7, botpos.y.toFixed(), botpos.z.toFixed() - 7, 1))
							} else {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed() + 7, botpos.y.toFixed(), botpos.z.toFixed(), 1))
							}
						} else {
							if (posZ < 7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed(), botpos.y.toFixed(), botpos.z.toFixed() - 7, 1))
							} else {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed(), botpos.y.toFixed(), botpos.z.toFixed(), 1))
							}
						}
					}
				} else {
					if (thevpos.z.toFixed() - botpos.z.toFixed() > 0) {
						var posX = botpos.x.toFixed() - thevpos.x.toFixed()
						var posZ = thevpos.z.toFixed() - botpos.z.toFixed()
						if (posX < 7) {
							if (posZ < 7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed() - 7, botpos.y.toFixed(), botpos.z.toFixed() + 7, 1))
							} else {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed() - 7, botpos.y.toFixed(), botpos.z.toFixed(), 1))
							}
						} else {
							if (posZ < 7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed(), botpos.y.toFixed(), botpos.z.toFixed() + 7, 1))
							} else {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed(), botpos.y.toFixed(), botpos.z.toFixed(), 1))
							}
						}
					} else {
						var posX = botpos.x.toFixed() - thevpos.x.toFixed()
						var posZ = botpos.z.toFixed() - thevpos.z.toFixed()
						if (posX < 7) {
							if (posZ < 7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed() - 7, botpos.y.toFixed(), botpos.z.toFixed() - 7, 1))
							} else {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed() - 7, botpos.y.toFixed(), botpos.z.toFixed(), 1))
							}
						} else {
							if (posZ < 7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed(), botpos.y.toFixed(), botpos.z.toFixed() - 7, 1))
							} else {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x.toFixed(), botpos.y.toFixed(), botpos.z.toFixed(), 1))
							}
						}
					}
				}
			} catch (error) {
				// do nothing
			}
		})
	} else {
		uselessvar = uselessvar + 1
		/*
		console.log('nope')
		Object.entries(others2).forEach(([k,v]) => {
			console.log("penemy")
		})
		*/
	}
	others = others2
	friendly = friendly2
})

bot.on('chat', (username, message) => {
	if (username === bot.username) return
	if (message.startsWith("say")) {
		bot.chat(message.replace("say ", ""))
	}
	
	if (message.startsWith("bot comexyz ")) {
		const thename = message.split(" ")[2]
		const x = message.split(" ")[3]
		const y = message.split(" ")[4]
		const z = message.split(" ")[5]
		if (thename === bot.username || thename === "all") {
			bot.pathfinder.stop()
			bot.pathfinder.setMovements(defaultMove)
			bot.pathfinder.setGoal(new GoalNear(x, y, z, 1))
		}
	}
	
	if (message.startsWith("bot come ")) {
		const thename = message.split("bot come ")[1]
		if (thename === bot.username || thename === "all") {
			const target = bot.players[username].entity
			if (!target) {
				bot.chat("I don't see you !")
				return
			}
			bot.pathfinder.stop()
			const { x: playerX, y: playerY, z: playerZ } = target.position

			bot.pathfinder.setMovements(defaultMove)
			bot.pathfinder.setGoal(new GoalNear(playerX, playerY, playerZ, 1))
		}
	}
	
	if (message.startsWith("eval ")) {
		var thecode = message.replace("eval ", "")
		eval(thecode)
	}
	
	if (message.startsWith("botneedhelp ") && username.startsWith(botprefix)) {
		var allypos = message.split(" ")
		bot.pathfinder.stop()
		bot.pathfinder.setMovements(defaultMove)
		bot.pathfinder.setGoal(new GoalNear(allypos[1], allypos[2], allypos[3], 10))
	}
	
	if (message === "zxc") {
		var fmessage = `Visible: `
		Object.entries(bot.players).forEach(([k,v]) => {
			try {
				var thevec3 = `${v.entity.position.x.toFixed()} ${v.entity.position.y.toFixed()} ${v.entity.position.z.toFixed()}`  
				fmessage = fmessage + `${k} at ${thevec3}, `
			} catch (error) {
				// do nothing
			}
		})
		bot.chat(fmessage)
	}
	
	if (message === "bot roam") {
		if (isRoamingEnabled) {
			bot.chat("stopped roaming")
			isRoamingEnabled = false
		} else {
			bot.chat("started roaming")
			isRoamingEnabled = true
		}
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
