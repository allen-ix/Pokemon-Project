class PokemonCard:
    def __init__(self, name, rarity, hp, card_type, attack, description, weaknesses, card_number, release_date, evolution_stage, abilities):
        self.name = name
        self.rarity = rarity
        self.hp = hp
        self.card_type = card_type
        self.attack = attack
        self.description = description
        self.weaknesses = weaknesses
        self.card_number = card_number
        self.release_date = release_date
        self.evolution_stage = evolution_stage
        self.abilities = abilities

    def show_info(self):
        print(
            f"Name: {self.name}\n"
            f"Rarity: {self.rarity}\n"
            f"HP: {self.hp}\n"
            f"Card Type: {', '.join(self.card_type)}\n"
            f"Attack: {self.attack}\n"
            f"Description: {self.description}\n"
            f"Weaknesses: {', '.join(map(str, self.weaknesses))}\n"
            f"Card Number: {self.card_number}\n"
            f"Release Date: {self.release_date}\n"
            f"Evolution Stage: {self.evolution_stage}\n"
            f"Special Abilities: {', '.join(self.abilities)}"
        )

class Trainer:
    def __init__(self, name, age, location, email):
        self.name = name
        self.age = age
        self.location = location
        self.email = email

    def show_info(self):
        print(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Location: {self.location}\n"
            f"Email: {self.email}"
        )

# Pokemon cards and assign them to variables
card1 = PokemonCard("Pikachu", "Common", 60, ["Electric"], "Thunder Shock", "A mouse-like pokemon that can generate electricity.", ["Ground"], 25, "01/09/1999", "Basic", ["Static"])
card2 = PokemonCard("Charizard", "Rare", 150, ["Fire", "Flying"], "Fire Blast", "A dragon-like pokemon that can breathe fire.", ["Water", "Electric", "Rock"], 6, "01/09/1999", "Stage 2", ["Blaze"])
card3 = PokemonCard("Mewtwo", "Rare", 130, ["Psychic"], "Psychic", "A genetically engineered pokemon that has powerful psychic abilities.", ["Dark, Bug, Ghost"], 10, "01/09/1999", "Basic", ["Pressure"])
card4 = PokemonCard("Bulbasaur", "Common", 50, ["Grass, Poison"] , "Vine Whip", "A plant-like pokemon that has a bulb on its back.", ["Fire, Ice, Flying, Psychic"], 44,  "01/09/1999", "Basic", ["Overgrow"])
card5 = PokemonCard("Squirtle", "Common", 40, ["Water"], "Bubble", "A turtle-like pokemon that can squirt water.", ["Electric, Grass"], 63,  "01/09/1999", "Basic", ["Torrent"])
card6 = PokemonCard("Eevee", "Common", 50, ["Normal"], "Tackle", "A fox-like pokemon that can evolve into different types.", ["Fighting"], 51, "16/06/1999", "Basic", ["Adaptability"])
card7 = PokemonCard("Snorlax", "Rare", 140, ["Normal"], "Body Slam", "A huge pokemon that likes to sleep and eat.", ["Fighting"], 27,  "16/06/1999", "Basic", ["Thick Fat"])
card8 = PokemonCard("Lugia", "Rare", 130, ["Psychic" , "Flying"], "Aeroblast", "A legendary pokemon that can control the wind.", ["Electric, Ice, Dark, Ghost"], 9,  "21/12/2000", "Basic", ["Pressure"])
card9 = PokemonCard("Ho-Oh", "Rare", 130, ["Fire" , "Flying"], "Sacred Fire", "A legendary pokemon that can resurrect the dead.", ["Water,Electric, Rock"], 7,  "21/09/2001", "Basic", ["Regenerator"])
card10 = PokemonCard("Celebi", "Rare", 70, ["Pyschic" , "Grass"], "Heal Bell", "A mythical pokemon that can travel through time.", ["Fire, Ice, Bug, Ghost, Dark, Flying"], 3,  "28/02/2002", "Basic", ["Natural Cure"])
card11 = PokemonCard("Gengar", "Rare", 60, ["Ghost" , "Poison"], "Shadow Punch", "A dark purple, bipedal Pokemon with a roundish body." , ["Ghost ,Dark , Ground, Psychic"] , 94,"06/07/2016" , "Final Form" , ["Cursed Body"])
card12 = PokemonCard("Gyarados", "Rare", 95, ["Water" , "Flying"], "Waterfall", "A piscine, draconic Pokemmon with a long serpentine body coverd in slightly overlapping scales" , ["Electric, Rock "] , 130,  "1996" , "Final Form" , ["Intimidate"])
card13 = PokemonCard("Mudkip", "Common", 50, ["Water"], "Watergun", "A small, ammphibious, quadrupedal Pokemon." , ["Electric, Grass "] , 258  , "08/12/2017" , "Basic" , ["Torrent"])
card14 = PokemonCard("Meowth", "Rare", 40, ["Normmal"], "Fake out", " A small, feline Pokemon with creamm0colored fur that turns brown at the tips of its hind paws and tail." , ["Fighting"]  , 52,  "06/07/2016" , "Basic" , ["Pickup"])
card15 = PokemonCard("Jigglypuf", "Rare", 115, ["Normmal" , "Fairy"], "Disarming Voice", "A pink pokemon with a spherical body" , ["Steel, Dark "]  ,39  , "28/05/1996" , "Basic" , ["Cute Charm"])
card16 = PokemonCard("Lucario", "Rare", 70, ["Fighting/Steel"], "Metal Claw", "A bipedal, canine-like Pokemon with predominantly blue and black fur" , ["Fire, Fighting, Ground "] , 448 , "05/16/2005" , "Final Form" , ["Inner Focus"])
card17 = PokemonCard("Wobbuffet", "Rare", 190, ["Pyschic"], "Destiny Bond", "A tall, cyan Pokemon with a soft body." , ["Bug, Ghost, Dark"] , 202 , "16/02/2017" , "Final Form" , ["Shadow Tag"])
card18 = PokemonCard("Darkrai", "Rare", 70, ["Dark"], "Dark Pulse", "A black, shadow-like Pokemon. It has a small head with a white fog-like ghostly plume billowing from its head covering one of its bright blue eyes" , ["Bug, Fairy, Fighting"] , 491 , "02/2007" , "Final Form" , ["Intimidate"])
card19 = PokemonCard("Totodile", "Common", 50, ["Water"], "Water Gun", "Is a bipedal, crocodilian Pokemon with well-developed jaws." , ["Electric, Grass "]  , 158 , "16/02/2017", "Basic" , ["Torrent"])
card20 = PokemonCard("Deoxys", "Rare", 50, ["Pyschic"], "Cosmic Power", "An alien-like, bipedal Pokemon that has four forms. Each focused on a different stat." , ["Bug, Ghost, Dark "] , 186, "17/06/2004" , "Normal Form" , ["Pressure"])


trainer1 = Trainer("Ash", 10, "Pallet Town", "ash@pokemon.com")
trainer2 = Trainer("Gary", 10, "Pallet Town", "gary@pokemon.com")
trainer3 = Trainer("Giovanni", 40, "Viridian City", "giovanni@teamrocket.com")
trainer4 = Trainer("Silver", 16, "Johto City", "silver@pokemon.com")
trainer5 = Trainer("Gold", 16, "Erika City", "Erika@pokemon.com")
trainer6 = Trainer("Steven", 31, "Ever Grande City", "stevenstone@pokemon.com")
trainer7 = Trainer("Roxanne", 18 , "Rustboro City" , "roxanne@pokemon.com" )
trainer8 = Trainer("Aaron" , 21 , "Sinoh Region" , "aaronelitefor@pokemon.com")
trainer9 = Trainer("Ronald", 20, "Buncag Grounds", "ronaldpogi@pokemon.com")
trainer10 = Trainer("Cedric" , 19 , "Bunkhose" , "cedric@pokemon.com")

pokemon_cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20]
trainers = [trainer1, trainer2, trainer3, trainer4, trainer5, trainer6, trainer7, trainer8, trainer9, trainer10]

print("Pokemon Cards:")
for card in pokemon_cards:
    card.show_info()
    print("\n" + "=" * 30 + "\n")

print("Trainers:")
for trainer in trainers:
    trainer.show_info()
    print("\n" + "=" * 30 + "\n")
