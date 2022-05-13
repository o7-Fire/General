var express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs')

const mineflayer = require('mineflayer')
const mineflayerViewer = require('prismarine-viewer').mineflayer
const { pathfinder, Movements, goals: { GoalNear } } = require('mineflayer-pathfinder')
const navigatePlugin = require('mineflayer-navigate')(mineflayer);
var bloodhoundPlugin = require('mineflayer-bloodhound')(mineflayer);
const armorManager = require('mineflayer-armor-manager')
const autoeat = require("mineflayer-auto-eat")
var blockFinderPlugin = require('mineflayer-blockfinder')(mineflayer);
const inventoryViewer = require('mineflayer-web-inventory')
//const {autoCrystal} = require('mineflayer-autocrystal')
const pvp = require('mineflayer-pvp').plugin

var sleep = require('sleep');
const { Vec3 } = require('vec3')
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
  host: 'testing2b.aternos.me',
  username: (args[0]),
  version: '1.16.5',
  port: 49884
})

var botprefix = "NBot" // change this to something else if you want to change the name in main.py
var botowner = "Nexity" // to prevent people hijacking your bot
var botpassword = "shitfuck" // for servers with authme / authentication
const mcData = require('minecraft-data')(bot.version)
var pi = 3.14159;
var isRoamingEnabled = false
var isAutototemEnabled = false
var isAutoFishingEnabled = false
var isMiningEnabled = false
var others = {}
var friendly = {}
var uselessvar = 0
var uselessvar2 = 0
var uselessvar3 = 0
var a1 = false

let itemsByName
if (bot.supportFeature('itemsAreNotBlocks')) {
	itemsByName = 'itemsByName'
} else if (bot.supportFeature('itemsAreAlsoBlocks')) {
	itemsByName = 'blocksByName'
}

navigatePlugin(bot);
bot.loadPlugins([armorManager, pathfinder, autoeat, pvp, blockFinderPlugin]);
//bot.loadPlugin(autoCrystal)
bloodhoundPlugin(bot);
bot.bloodhound.yaw_correlation_enabled = true;
let mcAssets = require('minecraft-assets')(bot.version)

const defaultMove = new Movements(bot, mcData)

function trymine(idoftheblock) {
    if (isMiningEnabled) {
        bot.findBlock({
            point: bot.entity.position,
            matching: idoftheblock,
            maxDistance: 256,
            count: 15,
        }, function(err, blocks) {
            if (err) {
                // do nothing
            }
            if (blocks.length) {
                var block = blocks[Math.floor(Math.random()*blocks.length)]
                bot.pathfinder.stop()
                bot.pathfinder.setMovements(defaultMove)
                bot.pathfinder.setGoal(new GoalNear(block.position.x, block.position.y-1, block.position.z, 0))
                function trymine2() {
                    setTimeout(function() {
                        if (bot.blockAt(new vec3(block.position.x, block.position.y, block.position.z)).name !== "air") {
                            trymine2()
                        } else {
                            trymine(idoftheblock)
                        }
                    }, 100)
                }
                trymine2()
            } else {
                // do nothing
            }
        });
    }
}

bot.once('spawn', () => {
    var botport = Number.parseInt(args[0].replace(botprefix, ""))

    //inventory viewer
    inventoryViewer(bot, {port: 5200 + botport})

    //prismarine viewer
    mineflayerViewer(bot, { port: 5100 + botport })
    // Draw the path followed by the bot
    const path = [bot.entity.position.clone()]
    bot.on('move', () => {
        if (path[path.length - 1].distanceTo(bot.entity.position) > 1) {
            path.push(bot.entity.position.clone())
            bot.viewer.drawLine('path', path)
        }
    })

    // mainframe
	const app = express();
	var http = require('http').Server(app);
    var io = require('socket.io')(http);
	// Parse URL-encoded bodies (as sent by HTML forms)
    app.use(bodyParser.urlencoded({
        extended: true
    }));
    // Parse JSON bodies (as sent by API clients)
    app.use(express.json());

	app.get ('/', function(req, res){
		res.send(`
		    <body style="background-color:darkgray">
            Bot Name: ${args[0]}<br/>
            Bot Position: ${bot.entity.position.toString()}<br/><br/>
            All online players: ${Object.keys(bot.players).join(", ")}<br/><br/>
            <form method="post">
                <label for="sdrcawtcast">Bot say (text):</label>
                <input type="text" id="sdrcawtcast" name="message">
            </form>
            <form method="post">
                <label for="dvrygsdrvry">Goto (playername):</label>
                <input type="text" id="dvrygsdrvry" name="navigate">
            </form>
            <form method="post">
                <label for="svtretyrevyt">Goto (x) (y) (z):</label>
                <input type="text" id="svtretyrevyt" name="gotoxyz">
            </form>
            <form method="post">
                <label for="ertsrvegdsrgv">Mine (block_name) / (stop):</label>
                <input type="text" id="ertsrvegdsrgv" name="mine">
            </form>
            <form method="post">
                <label for="cvbnvbcnbvc">Attack (playername):</label>
                <input type="text" id="cvbnvbcnbvc" name="attack">
            </form>
            <form method="post">
                <label for="fdgdfgryretdfg">Drop item (itemname) (amount):</label>
                <input type="text" id="fdgdfgryretdfg" name="drop">
            </form>
            Go to <a href="http://localhost:${5100 + botport}">here</a> to see prismarine viewer<br/>
            Go to <a href="http://localhost:${5200 + botport}">here</a> to see bot inventory (images)<br/>
		`)
	});

    app.post('/', (req, res) => {
        console.log(req.body);
        if (req.body.message) {
            bot.chat(req.body.message.toString())
            res.send(`<a href="http://localhost:${5000 + botport}">go back</a>`);
        }
        if (req.body.navigate) {
            const target = bot.players[req.body.navigate].entity
            if (!target) {
                res.send(`Cannot see the player to navigate.<br/><a href="http://localhost:${5000 + botport}">go back</a>`)
                return
            }
            bot.pathfinder.stop()
            const { x: playerX, y: playerY, z: playerZ } = target.position

            bot.pathfinder.setMovements(defaultMove)
            bot.pathfinder.setGoal(new GoalNear(playerX, playerY, playerZ, 1))
            res.send(`Found player to navigate.<br/><a href="http://localhost:${5000 + botport}">go back</a>`);
        }
        if (req.body.gotoxyz) {
            var xyz = req.body.gotoxyz.split(" ")
            bot.pathfinder.stop()
            bot.pathfinder.setMovements(defaultMove)
            bot.pathfinder.setGoal(new GoalNear(xyz[0], xyz[1], xyz[2], 1))
            res.send(`Navigating to the specified route.<br/><a href="http://localhost:${5000 + botport}">go back</a>`);
        }
        if (req.body.mine) {
            if (req.body.mine == "stop") {
                isMiningEnabled = false
                res.send(`Stopped mining.<br/><a href="http://localhost:${5000 + botport}">go back</a>`);
            } else {
                var theid = mcData[itemsByName][req.body.mine.toString()].id
                trymine(theid)
                res.send(`Started mining.<br/><a href="http://localhost:${5000 + botport}">go back</a>`);
            }
        }
        if (req.body.attack) {
            try {
                bot.pvp.attack(bot.players[req.body.attack.toString()].entity)
                res.send(`Started attacking.<br/><a href="http://localhost:${5000 + botport}">go back</a>`);
            } catch (error) {
                res.send(`Could not find the person to attack.<br/><a href="http://localhost:${5000 + botport}">go back</a>`);
            }
        }
        if (req.body.drop) {
            try {
                bot.toss(mcData[itemsByName][req.body.drop.split(" ")[0]].id, null, req.body.drop.split(" ")[1], (err) => {
                    if (err) {
                        // do nothing
                    } else {
                        res.send(`Threw the item.<br/><a href="http://localhost:${5000 + botport}">go back</a>`);
                    }
                })
            } catch (error) {
                res.send(`unable to find block.<br/><a href="http://localhost:${5000 + botport}">go back</a>`);
            }
        }
    });
	http.listen(5000 + botport, function(){
		// do nothing
	});
	bot.autoEat.options.priority = "foodPoints"
	bot.autoEat.options.bannedFood = []
	bot.autoEat.options.eatingTimeout = 3
	bot.chat("/login " + botpassword)
})

//quarry(2, 3, 200, 12, 3, 210)
// quarry(-232, 1, 234, -200, 3, 250)
function quarry(x1, y1, z1, x2, y2, z2){
	for (var newy = y1; newy <= y2; newy++) {
		for (var newx = x1; newx <= x2; newx++) {
			for (var newz = z1; newz <= z2; newz++) {
			    function trymine() {
			        setTimeout(function() {
                        var theblock = bot.blockAt(new vec3(newx, newy, newz))
                        if (theblock.name !== "air") {
                            bot.pathfinder.stop()
                            bot.pathfinder.setMovements(defaultMove)
                            bot.pathfinder.setGoal(new GoalNear(newx, newy-1, newz, 0))
                            function trymine2() {
                                setTimeout(function() {
                                    if (theblock.name !== "air") {
                                        trymine2()
                                    } else {
                                        trymine()
                                    }
                                }, 100)
                            }
                            trymine2()
                        }
                    }, 100)
                }
                trymine()
			}
		}
	}
}

function theautofish() {
	setTimeout(function() {
		if (isAutoFishingEnabled && a1 === false) {
			var istherenearbywater = false
			bot.findBlock({point: bot.entity.position, matching: 8, maxDistance: 10, count: 1,}, function(err, blocks) {
				if (err) {
					bot.chat("error while trying to find water")
				}
				if (blocks.length) {
					istherenearbywater = true
					bot.lookAt(blocks[0].position)
				} else {
					//
				}
			});
			bot.findBlock({point: bot.entity.position, matching: 9, maxDistance: 10, count: 1,}, function(err, blocks) {
				if (err) {
					bot.chat("error while trying to find water")
				}
				if (blocks.length) {
					istherenearbywater = true
					bot.lookAt(blocks[0].position)
				} else {
					//
				}
			});
			setTimeout(function() {
				bot.equip(bot.inventory.findInventoryItem("fishing_rod"), 'hand', (err) => {
					if (err) {
						bot.chat("no fishing rod in inventory")
					} else {
						function fishingEnd(err) {
							if (err) throw err;

							setTimeout(() => {
								if (isAutoFishingEnabled) {
									bot.fish(fishingEnd)
								}
							}, 30); //no problem
						}
						bot.fish(fishingEnd)
					}
				})
			}, 3000)
		}
		a1 = isAutoFishingEnabled
		theautofish()
	}, 2000)
}
theautofish()


  bot.once('spawn', function () {
  setInterval(() => {
    const entity = bot.nearestEntity()
    if (entity !== null) {
      if (entity.type === 'player') {
        bot.lookAt(entity.position.offset(0, 1.6, 0))
      } else if (entity.type === 'mob') {
        bot.lookAt(entity.position)
      }
    }
  }, 50)
})

function showVillagers () {
	const villagers = Object.keys(bot.entities).map(id => bot.entities[id]).filter(e => e.entityType === mcData.entitiesByName.villager.id)
	const closeVillagersId = villagers.filter(e => bot.entity.position.distanceTo(e.position) < 3).map(e => e.id)
	bot.chat(`found ${villagers.length} villagers`)
	bot.chat(`villager(s) you can trade with: ${closeVillagersId.join(', ')}`)
}

function showInventory () {
	bot.inventory.slots
	.filter(item => item).forEach((item) => {
		bot.chat(stringifyItem(item))
	})
}

async function showTrades (id) {
	const e = bot.entities[id]
	switch (true) {
    		case !e:
      			bot.chat(`cant find entity with id ${id}`)
      			break
    		case e.entityType !== mcData.entitiesByName.villager.id:
      			bot.chat('entity is not a villager')
      			break
    		case bot.entity.position.distanceTo(e.position) > 3:
      			bot.chat('villager out of reach')
      			break
    		default: {
      			const villager = await bot.openVillager(e)
      			villager.close()
      			stringifyTrades(villager.trades).forEach((trade, i) => {
        			bot.chat(`${i + 1}: ${trade}`)
      			})
    		}
  	}
}

async function trade (id, index, count) {
	const e = bot.entities[id]
	switch (true) {
    		case !e:
      			bot.chat(`cant find entity with id ${id}`)
      			break
    		case e.entityType !== mcData.entitiesByName.villager.id:
     			bot.chat('entity is not a villager')
      			break
    		case bot.entity.position.distanceTo(e.position) > 3:
      			bot.chat('villager out of reach')
      			break
    	default: {
      		const villager = await bot.openVillager(e)
      		const trade = villager.trades[index - 1]
      		count = count || trade.maxTradeuses - trade.tooluses
      		switch (true) {
        		case !trade:
          			villager.close()
          			bot.chat('trade not found')
          			break
        		case trade.disabled:
          			villager.close()
          			bot.chat('trade is disabled')
          			break
			case trade.maxTradeuses - trade.tooluses < count:
          			villager.close()
          			bot.chat('cant trade that often')
          			break
        		case !hasResources(villager.window, trade, count):
          			villager.close()
          			bot.chat('dont have the resources to do that trade')
          			break
        		default:
          			bot.chat('starting to trade')
          			try {
            				await bot.trade(villager, index - 1, count)
            				bot.chat(`traded ${count} times`)
          			} catch (err) {
            				bot.chat('an error acured while tyring to trade')
           			 	console.log(err)
          			}
          			villager.close()
			}
		}
	}

	function hasResources (window, trade, count) {
		const first = enough(trade.firstInput, count)
		const second = !trade.hasSecondItem || enough(trade.secondaryInput, count)
		return first && second

		function enough (item, count) {
			return window.count(item.type, item.metadata) >= item.count * count
		}
	}
}

function stringifyTrades (trades) {
	return trades.map((trade) => {
		let text = stringifyItem(trade.firstInput)
		if (trade.secondaryInput) text += ` & ${stringifyItem(trade.secondaryInput)}`
		if (trade.disabled) text += ' x '; else text += ' » '
		text += stringifyItem(trade.output)
		return `(${trade.tooluses}/${trade.maxTradeuses}) ${text}`
  	})
}

function stringifyItem (item) {
	if (!item) return 'nothing'
	let text = `${item.count} ${item.displayName}`
	if (item.nbt && item.nbt.value) {
		const ench = item.nbt.value.ench
		const StoredEnchantments = item.nbt.value.StoredEnchantments
		const Potion = item.nbt.value.Potion
		const display = item.nbt.value.display

		if (Potion) text += ` of ${Potion.value.replace(/_/g, ' ').split(':')[1] || 'unknow type'}`
		if (display) text += ` named ${display.value.Name.value}`
		if (ench || StoredEnchantments) {
			text += ` enchanted with ${(ench || StoredEnchantments).value.value.map((e) => {
			const lvl = e.lvl.value
			const id = e.id.value
			return mcData.enchantments[id].displayName + ' ' + lvl
			}).join(' ')}`
		}
	}
	return text
}

bot.on("health", () => {
	if (bot.food === 20) bot.autoEat.disable()
	// Disable the plugin if the bot is at 20 food points
	else bot.autoEat.enable() // Else enable the plugin again
})

bot.on('onCorrelateAttack', function (attacker,victim,weapon) {
	if ((victim.displayName || victim.username).startsWith(botprefix)) {
		if ((attacker.displayName || attacker.username).startsWith(botprefix)) {

		} else {
			//bot.chat(`${(victim.displayName || victim.username)} is getting attacked by ${(attacker.displayName || attacker.username)}`)
			bot.pvp.attack(attacker)
		}
	}
	if ((attacker.displayName || attacker.username) === botowner && !(victim.displayName || victim.username).startsWith(botprefix)) {
		bot.pvp.attack(victim)
	}
});

function autototem() {
	setTimeout(function() {
		var ifhas = 0
		var items = bot.inventory.items()
		var arrayLength = items.length;
		for (var i = 0; i < arrayLength; i++) {
			var theitem = items[i]
			if (theitem.name === "totem_of_undying") {
				ifhas = 1
			}
		}
		if (ifhas === 0) {
			//bot.chat("/give @s totem_of_undying")
		}
		if (isAutototemEnabled) {
			const totemName = 'totem_of_undying'
			const totem = bot.inventory.items().find(item => item.name === totemName)

			if (totem && !bot.inventory.slots[45]) {
				try{ bot.equip(totem, 'off-hand') } catch (error) {}
			} else if (totem && bot.inventory.slots[45] && bot.inventory.slots[45].name !== totemName) {
				try { bot.equip(totem, 'off-hand') } catch (error) {}
			}
		}
		autototem()
	}, 500)
}
setTimeout(function() { autototem() }, 5000)

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

setTimeout(function() {
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
		if (!isEmpty(others) && isEmpty(friendly) && uselessvar3 >= 10) {
			var botpos = bot.entity.position
			//console.log(botpos)
			bot.chat(`botneedhelp ${botpos.x.toFixed()} ${botpos.y.toFixed()} ${botpos.z.toFixed()}`)
			uselessvar3 = 0
		} else if (!isEmpty(others) && isEmpty(friendly) && uselessvar === 30) {
			uselessvar3 = uselessvar3 + 1
			uselessvar = uselessvar + 1
			Object.entries(others2).forEach(([k,v]) => {
				try {
					var botpos = bot.entity.position
					var thevpos = bot.players[k].entity.position
					if (thevpos.x.toFixed() - botpos.x.toFixed() > 0) {
						if (thevpos.z.toFixed() - botpos.z.toFixed() > 0) {
							var posX = thevpos.x.toFixed() - botpos.x.toFixed()
							var posZ = thevpos.z.toFixed() - botpos.z.toFixed()
							console.log(`${k} : ${posX} ${posZ}`)
							if (posX < 7 && posZ < 7 && posX > -7 && posZ > -7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x - 4, botpos.y, botpos.z - 4, 1))
							}
						} else {
							var posX = thevpos.x.toFixed() - botpos.x.toFixed()
							var posZ = botpos.z.toFixed() - thevpos.z.toFixed()
							console.log(`${k} : ${posX} -${posZ}`)
							if (posX < 7 && posZ < 7 && posX > -7 && posZ > -7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x - 4, botpos.y, botpos.z + 4, 1))
							}
						}
					} else {
						if (thevpos.z.toFixed() - botpos.z.toFixed() > 0) {
							var posX = botpos.x.toFixed() - thevpos.x.toFixed()
							var posZ = thevpos.z.toFixed() - botpos.z.toFixed()
							console.log(`${k} : -${posX} ${posZ}`)
							if (posX < 7 && posZ < 7 && posX > -7 && posZ > -7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x + 4, botpos.y, botpos.z - 4, 1))
							}
						} else {
							var posX = botpos.x.toFixed() - thevpos.x.toFixed()
							var posZ = botpos.z.toFixed() - thevpos.z.toFixed()
							console.log(`${k} : -${posX} -${posZ}`)
							if (posX < 7 && posZ < 7 && posX > -7 && posZ > -7) {
								bot.pathfinder.stop()
								bot.pathfinder.setMovements(defaultMove)
								bot.pathfinder.setGoal(new GoalNear(botpos.x + 4, botpos.y, botpos.z + 4, 1))
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
}, 10000)

bot.on('chat', (username, message) => {
	if (username === bot.username) return
	if (username !== botowner) return
	// todo fix this
	const command = message.split(' ')
	switch (true) {
		case message === 'bot show villagers':
			showVillagers()
			break
		case message === 'bot show inventory':
			showInventory()
			break
		case /^show trades [0-9]+$/.test(message):
			showTrades(command[2])
			break
		case /^trade [0-9]+ [0-9]+( [0-9]+)?$/.test(message):
			trade(command[1], command[2], command[3])
			break
	}
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
		try {
			eval(thecode)
		} catch (error) {
			bot.chat(error.toString())
		}
	}

	if (message === "equiparmor") {
		bot.armorManager.equipAll()
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

	if (message === "bot autototem") {
		if (isAutototemEnabled) {
			bot.chat("disabled auto-totem")
			isAutototemEnabled = false
		} else {
			bot.chat("enabled auto-totem")
			isAutototemEnabled = true
		}
	}

	if (message === "bot autofish") {
		if (isAutoFishingEnabled) {
			bot.chat("disabled auto-fish")
			isAutoFishingEnabled = false
		} else {
			bot.chat("enabled auto-fish")
			isAutoFishingEnabled = true
		}
	}

	if (message.startsWith("bot attack ")) {
		try {
			bot.pvp.attack(bot.players[message.split("bot attack ")[1]].entity)
		} catch (error) {
			bot.chat("Could not find person")
		}
	}
	if (message === "line up") {
		const target = bot.players[username].entity
		if (!target) {
		  bot.chat("I don't see you !")
		  return
		}
		const { x: playerX, y: playerY, z: playerZ } = target.position

		bot.pathfinder.setMovements(defaultMove)
		bot.pathfinder.setGoal(new GoalNear(playerX + Number.parseInt(args[0].replace(botprefix, "")), playerY, playerZ, RANGE_GOAL))
	}
	if (message.startsWith("equipblock ")) {
		var blocktoequip = message.replace("equipblock ", "");
		bot.equip(mcData[itemsByName][blocktoequip].id, 'hand', (err) => {
			if (err) {
				bot.chat(`unable to equip ${blocktoequip}: ${err.message}`)
			} else {
				bot.chat(`equipped ${blocktoequip}`)
			}
		})
	}

	if (message.startsWith("throwblock ")) {
		var args = message.split(" ");
		try {
			bot.toss(mcData[itemsByName][args[1]].id, null, args[2], (err) => {
				if (err) {
					bot.chat(`unable to throw ${blocktoequip}: ${err.message}`)
				} else {
					//bot.chat(`threw ${blocktoequip}`)
				}
			})
		} catch (error) {
			bot.chat("unable to find block / not enough arguments")
		}
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

	if (message.startsWith("bot mine ")) {
	    isMiningEnabled = true
		var blocktomine = message.replace("bot mine ", "")
		var theid = mcData[itemsByName][blocktomine].id
		trymine(theid)
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
