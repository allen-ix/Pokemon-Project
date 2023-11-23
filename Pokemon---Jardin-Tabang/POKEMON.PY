class PokemonCard:
    def __init__(self, name, rarity, hp, card_type, attack, description, weaknesses, card_number, evolution_stage, abilities, release_date=None):
        self.name = name
        self.rarity = rarity
        self.hp = hp
        self.card_type = card_type
        self.attack = attack
        self.description = description
        self.weaknesses = weaknesses
        self.card_number = card_number
        self.evolution_stage = evolution_stage
        self.abilities = abilities
        self.release_date = release_date

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
card1 = PokemonCard("Pikachu", "Rare", 60, ["Electric"], "Thunder Shock", "A mouse-like pokemon that can generate electricity.", ["Ground"], 25, "Basic", ["Static"])
card2 = PokemonCard("Charmeleon", "Rare", 120, ["Fire"], "Flamethrower", "It has a barbaric nature. In battle, it whips its fiery tail around and slashes away with sharp claws.", ["Water"], 5, "Stage 2", ["Solar Power"])
card3 = PokemonCard("Mewtwo", "Uncommon", 150, ["Psychic"], "Psychic", "A genetically engineered pokemon that has powerful psychic abilities.", ["Dark"], 10,"Basic", ["Pressure"])
card4 = PokemonCard("Caterpie", "Common", 45, ["Grass"] , "Bug Bite", "For protection, it releases a horrible stench from the antenna on its head to drive away enemies.", ["Fire"], 44, "Basic", ["Shield Dust"])
card5 = PokemonCard("Squirtle", "Rare", 40, ["Water"], "Bubble", "A turtle-like pokemon that can squirt water.", ["Grass"], 63, "Basic", ["Torrent"])
card6 = PokemonCard("Eevee", "Rare", 50, ["Normal"], "Tackle", "A fox-like pokemon that can evolve into different types.", ["Fighting"], 51, "Basic", ["Adaptability"])
card7 = PokemonCard("Snorlax", "Uncommon", 140, ["Normal"], "Body Slam", "A huge pokemon that likes to sleep and eat.", ["Fighting"], 27, "Basic", ["Thick Fat"])
card8 = PokemonCard("Raikou", "Rare", 90, ["Electric"], "Thunder Fang", "Raikou embodies the speed of lightning. The roars of this Pokémon send shock waves shuddering through the air and shake the ground as if lightning bolts had come crashing down.", ["Ground"], 243, "Basic", ["Pressure"])
card9 = PokemonCard("Cryogonal", "Rare", 80, ["Ice"], "Aurora Beam", "Cryogonal appear during cold seasons. It is said that people and Pokémon who die on snowy mountains are reborn into these Pokémon.", ["Fire"], 615, "Basic", ["Levitate"])
card10 = PokemonCard("Pancham", "Uncommon", 67, ["Fighting"], "Circle Throw", "It chooses a Pangoro as its master and then imitates its masters actions. This is how it learns to battle and hunt for prey", ["Fairy"], 674,"Basic", ["Mold Breaker"])
card11 = PokemonCard("Entei", "Rare", 115, ["Fire"], "Flame Wheel", "Entei embodies the passion of magma. This Pokémon is thought to have been born in the eruption of a volcano. It sends up massive bursts of fire that utterly consume all that they touch." , ["Water"] , 244, "Basic" , ["Pressure"])
card12 = PokemonCard("Suicune", "Rare", 100, ["Water"], "Hydro Pump", "Suicune embodies the compassion of a pure spring of water. It runs across the land with gracefulness. This Pokémon has the power to purify dirty water." , ["Grass"] , 245 , "Final Form" , ["Pressure"])
card13 = PokemonCard("Mudkip", "Common", 50, ["Water"], "Watergun", "A small, ammphibious, quadrupedal Pokemon." , ["Electric"] , 258  , "Basic" , ["Torrent"])
card14 = PokemonCard("Meowth", "Rare", 40, ["Normmal"], "Fake out", " A small, feline Pokemon with creamm0colored fur that turns brown at the tips of its hind paws and tail." , ["Fighting"]  , 52, "Basic" , ["Pickup"])
card15 = PokemonCard("Jigglypuf", "Rare", 115, ["Normmal" , "Fairy"], "Disarming Voice", "A pink pokemon with a spherical body" , ["Steel, Dark "]  ,39 , "Basic" , ["Cute Charm"])
card16 = PokemonCard("Duskull", "Common", 20, ["Ghost"], "Payback", "If it finds bad children who won’t listen to their parents, it will spirit them away—or so it’s said." , ["Dark"] , 355, "Basic" , ["Levitate"])
card17 = PokemonCard("Wobbuffet", "Rare", 190, ["Pyschic"], "Destiny Bond", "A tall, cyan Pokemon with a soft body." , ["Bug, Ghost, Dark"] , 202  , "Final Form" , ["Shadow Tag"])
card18 = PokemonCard("Darkrai", "Rare", 70, ["Dark"], "Dark Pulse", "A black, shadow-like Pokemon. It has a small head with a white fog-like ghostly plume billowing from its head covering one of its bright blue eyes" , ["Bug, Fairy, Fighting"] , 491 , "Final Form" , ["Intimidate"])
card19 = PokemonCard("Totodile", "Common", 50, ["Water"], "Water Gun", "Is a bipedal, crocodilian Pokemon with well-developed jaws." , ["Electric, Grass "]  , 158, "Basic" , ["Torrent"])
card20 = PokemonCard("Deoxys", "Rare", 50, ["Pyschic"], "Cosmic Power", "An alien-like, bipedal Pokemon that has four forms. Each focused on a different stat." , ["Bug, Ghost, Dark "] , 186 , "Normal Form" , ["Pressure"])


trainer1 = Trainer("Ash", "May 22, 1987", "Pallet Town", "ash@pokemon.com")
trainer2 = Trainer("Gary", "April 6, 1984", "Pallet Town", "gary@pokemon.com")
trainer3 = Trainer("Giovanni", "August 1, 1983", "Viridian City", "giovanni@teamrocket.com")
trainer4 = Trainer("Silver", "December 24, 2007", "Johto City", "silver@pokemon.com")
trainer5 = Trainer("Gold", "July 21, 2007", "Erika City", "Erika@pokemon.com")
trainer6 = Trainer("Steven", "November 2, 1974", "Ever Grande City", "stevenstone@pokemon.com")
trainer7 = Trainer("Roxanne", "July 2, 2005" , "Rustboro City" , "roxanne@pokemon.com" )
trainer8 = Trainer("Aaron" , "October 6, 2002" , "Sinoh Region" , "aaronelitefor@pokemon.com")
trainer9 = Trainer("Ronald", "June 27, 2003", "Buncag Grounds", "ronaldpogi@pokemon.com")
trainer10 = Trainer("Cedric" , "June 2, 2004" , "Bunkhose" , "cedric@pokemon.com")

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
