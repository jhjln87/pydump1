import random
import time
legendaryDrops = ["The Claw","Rolling Beasts","Sparked Runners","Energy Free Armor","Hollow Spectral Armor","Archimonde","Hardened Platinum Vest","Molten Platinum Vest","Fractured Heat Armor","Lightning Platinum Vest","Rusty Energy Armor","Superb Charge Engine","Advanced Teleporter","Double Teleporter","Platinum Grappling Hook","Flaming Grappling Hook","Shocking Grappling Hook","Mighty Protector","Platinum Plating","Platinum Fortress","UltraHot Protector","Heat Storage Unit","Plasma Fortress","Energy Storage Unit","SuperCharge Protector","Electric Fortress","Maximum Protector","Defence Matrix","Quad Core Booster","Overload Preventor","Combined Engine Unit","DustMaker","Greedy","Backstabber","Selfish Guardian","Solar Torch","FlameWave","Flame Spear","Murmur","Swoop","Backstabbing Guardian","Unreliable Guardian","Rail Gun","WindForge","Shockwave","Anguish","Perimiter Protector","Mercy","Purifier","Advanced Repulser","BloodWeep","Sweetie","Armor Annihilator","SeraphBlade","Dark Eagle","Ejection Blast","Malfunctioning Blaster","Disintegration","Last Resort Vulcan","Rock Polisher","Damaged Armor Annihilator","Abomination","Reckoning","Chaos Bringer","Sorrow","Crimson Rapture","Magma Blast","HeronMark","Explosive Retreat","TerrorBlade","Overcooking Oven","Shadow Wolf","Rusty Heat Blaster","Overcharged Rocket Battery","Hybrid Heat Cannon","Distance Controller","Misguided Rocket Battery","Basalt Polisher","Bunker Shell","Ash Creator","Unstable Power Cell","Evac Spark","BigDaddy","BrightRoar","BullDog","StormWeaver","Hybrid Energy Cannon","MortalBullet","Distance Generator","Piercing Fox","Lightning Cutter","Falcon","Desert Fury","Distance Shredder","Mighty Cannon","Lazy Falcon","Spartan Carnage","Cockpit Piercer","Burning Shower","Red Rain","Space Invader","Desert Snake","Flaming Scope","Iron Frenzy","Overheated Heat Bomb","Half Burnt Scope","Cockpit Burner","Party Crasher","Cockpit Electrocuter","Spinefall","Delerium","Lightning Scope","Valiant Sniper","Electrocuted Scope","Overloaded EMP"]
# 114 of legendary
epicDrops = ["Iron Boots","Grave Diggers","Massive Stone Feet","Dynamite Boots","Devouring Paws","Scorching Feet","Massive Lava Feet","Dynamic Stompers","Charged Walkers","Lightning Supporters","Recoil Stompers","Massive Shocker Feet","Battery Armor","Avenger","Brutality","Flame Battery Armor","Zarkares","Windigo","GrimReaper","Energy Battery Armor","Naga","Charge Engine","Heat Engine","Cooling Mass Booster","Energy Mass Booster","Energy Engine","Combined Storage Unit","Tonto","Void","Void","Hurlbat","Selfish Protector","Nemo","Clash","FireFly","HeatPoint","Backstabbing Protector","Torment","Face Shocker","Electrolyte","Snack","Unreliable Protector","Annihilation","Sacrifice Cannon","Nightfall","War Hammer","Terror Cry","BackBreaker","Rock Recoiler","Unrepaired Laser Cannon","DawnBlaze","Flaminator","Heat Bomb","Flaming Hammer","Magma Recoiler","Corrupt Light","Broken Devourer","Cracked Plasma Cannon","Basalt Dissolver","Viking Hammer","UltraBright","Lightning Recoiler","Obsolete Energy Cannon","Broken Blizzard Dissolver","Fractured Basalt Dissolver","Last Words","EMP","Blizzard Dissolver","Malice Beam","Hot Flash","Drunk Lightning","Reckless Beam","Night Eagle","Frantic Brute","Desolation","Supreme Cannon","Savagery","Frantic Flame","Vandal Rage","Frantic Lightning","Grim Cobra","Hysteria"]
# 81 of epic
rareDrops = ["Gumiho","Chimaera","Burning Boots","Metal Maniacs","Blue Madness","Red Wrath","Rapid Destruction","Cosmos","Crow","Saviour Resistance","Energy Protector","Heat Portector","Physical Protector","Iron Grappling Hook","Electric Grappling Hook"]
# 16 of rare
commonDrops = ["Fenrir","Ettin","Sith","Nightmare","Typhoon","Punisher","Sizzling Rollers","Copper Destroyers","Metal Piercer","Crazed Repeater","Headhunter","Boomwitch","Homage","Hungering Beam","FireStorm","Scalpel","Sikanda","Royal Launcher","Rocket Launcher","Jab","Basic Teleporter","Buzz","Striker","Heat Capsule Unit","Energy Capsule Unit","Energy Generator","Heat Generator","Iron Plating","Cooling Booster","Energy Booster"] 
# 30 of common
perks = ["Mexican Hat","St. Patrick Hat","Snow Balls","Pumpkin Torso","Tiny Mech","Giant Mech","Goat Perk","Unicorn Horn","Santa Hat"]
# 9 of perk

while True:
	answer = input("Do you want to open a box?")
	print("premiumBox")
	print("premiumPack")
	print("arenaR1")
	print("fortuneBox")
	print("silverBox")
	print("goldBox")
	print("perkBox")
	box = input("Which of these boxes do you want to open?")
	
	if answer == "yes" or answer == "Yes" or answer == "y":
			
		for x in range(0,4):
			time.sleep(0.5)
			print(".")

# premium box
		if box == "premiumBox":
			rarityPercentage = random.randint(0,99)
			rarity = 3
			if rarityPercentage >= 78:
				rarity = 4
			if rarity == 3:
				item = random.randint(0,80)
				print(epicDrops[item]," Epic")
			if rarity == 4:
				item = random.randint(0,113)
				print(legendaryDrops[item]," Legendary")
				
# premium pack	
		if box == "premiumPack":
			for x in range(0,5):
				rarityPercentage = random.randint(0,99)
				rarity = 3
				if rarityPercentage >= 78:
					rarity = 4
				if rarity == 3:
					item = random.randint(0,80)
					print(epicDrops[item]," Epic")
				if rarity == 4:
					item = random.randint(0,113)
					print(legendaryDrops[item]," Legendary")
					
# fortune box
		if box == "fortuneBox":
			for x in range(0,3):
				rarityPercentage = random.randint(0,99)
				rarity = 1
				if rarityPercentage >= 10:
					rarity = 2
				if rarityPercentage >= 65:
					rarity = 3
				if rarityPercentage >= 92:
					rarity = 4
				if rarity == 1:
					item = random.randint(0,29)
					print(commonDrops[item]," Common")
				if rarity == 2:
					item = random.randint(0,15)
					print(rareDrops[item]," Rare")
				if rarity == 3:
					item = random.randint(0,80)
					print(epicDrops[item]," Epic")
				if rarity == 4:
					item = random.randint(0,113)
					print(legendaryDrops[item]," Legendary")
					
# gold box
		if box == "goldBox":
			item = random.randint(0,113)
			print(legendaryDrops[item]," Legendary")
			
# silver box
		if box == "silverBox":
			for x in range(0,18):
				rarityPercentage = random.randint(0,99)
				rarity = 1
				if rarityPercentage >= 63:
					rarity = 2
				if rarity == 1:
					item = random.randint(0,29)
					print(commonDrops[item]," Common")
				if rarity == 2:
					item = random.randint(0,15)
					print(rareDrops[item]," Rare")
						
# perk box
		if box == "perkBox":
			item = random.randint(0,8)
			print(perks[item]," Common")
		
# arena rank one
		if box == "arenaR1":
			for x in range (0,5):
				rarityPercentage = random.randint(0,99)
				rarity = 3
				if rarityPercentage >= 55:
					rarity = 4
				if rarityPercentage >= 65:
					rarity = 5
				if rarityPercentage >= 87:
					rarity = 6
				if rarity == 3:
					item = random.randint(0,80)
					print(epicDrops[item]," Epic")
				if rarity == 4:
					item = random.randint(0,113)
					print(legendaryDrops[item]," Legendary")
				if rarity == 5:
					print("Epic Ascension Relic"," Epic")
				if rarity == 6:
					print("Legendary Ascension Relic"," Legendary")
				
	if answer == "no" or answer == "No" or answer == "n":
		print("Then why did you even play?")
		
	print(" ")