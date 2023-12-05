
#your_app/management/commands/create_initial_data.py
from django.core.management.base import BaseCommand 
from cardquest.models import PokemonCard, Trainer

class Command (BaseCommand):

    help ='Creates initial data for the application' # <-- description of the command
    def handle (self, *args, **kwargs):
        self.create_pokemon_cards() # <-- where logic is implemented
        self.create_trainers ()
    def create_pokemon_cards(self):
    # Create Pokemon Card instances
        card1 = PokemonCard(
            name="Pikachu", rarity="Rare", hp=60,
            card_type="Electric", attack="Thunder Shock",
            description="A mouse-like Pokemon that can generate electricity.",
            weakness="Ground", card_number=25, release_date="1999-01-09",
            evolution_stage="Basic", abilities="Static"
        )

        card2 = PokemonCard(
            name="Charizard", rarity="Rare", hp=120,
            card_type="Fire", attack="Flamethrower",
            description="Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally.",
            weakness="Water", card_number=6, release_date="1996-02-27",
            evolution_stage="Final", abilities="Blaze"
        )

        card3 = PokemonCard(
            name="Blastoise", rarity="Rare", hp=100,
            card_type="Water", attack="Hydro Pump",
            description="A brutal Pokemon with pressurized water jets on its shell. It is known for blasting water over a long distance.",
            weakness="Electric", card_number=9, release_date="1996-02-27",
            evolution_stage="Final", abilities="Torrent"
        )

        card4 = PokemonCard(
            name="Jolteon", rarity="Rare", hp=65,
            card_type="Electric", attack="Thunderbolt",
            description="The negatively charged ions generated in its fur create a constant sparking noise.",
            weakness="Ground", card_number=135, release_date="1996-02-27",
            evolution_stage="Final", abilities="Volt Absorb"
        )

        card5 = PokemonCard(
            name="Venusaur", rarity="Rare", hp=110,
            card_type="Grass", attack="Solar Beam",
            description="The flower on its back catches the sun's rays. The sunlight is then absorbed and used for energy.",
            weakness="Fire", card_number=3, release_date="1996-02-27",
            evolution_stage="Final", abilities="Overgrow"
        )

        card6 = PokemonCard(
            name="Alakazam", rarity="Rare", hp=55,
            card_type="Psychic", attack="Psychic",
            description="Its brain can outperform a supercomputer. Its intelligence quotient is said to be around 5,000.",
            weakness="Dark", card_number=65, release_date="1996-02-27",
            evolution_stage="Final", abilities="Synchronize"
        )

        card7 = PokemonCard(
            name="Gyarados", rarity="Rare", hp=95,
            card_type="Water", attack="Hyper Beam",
            description="Rarely seen in the wild. Huge and vicious, it is capable of destroying entire cities in a rage.",
            weakness="Electric", card_number=130, release_date="1996-02-27",
            evolution_stage="Final", abilities="Intimidate"
        )

        card8 = PokemonCard(
            name="Dragonite", rarity="Rare", hp=91,
            card_type="Dragon", attack="Dragon Claw",
            description="It is said to make its home somewhere in the sea. It guides crews of shipwrecks to shore.",
            weakness="Ice", card_number=149, release_date="1996-02-27",
            evolution_stage="Final", abilities="Multiscale"
        )

        card9 = PokemonCard(
            name="Machamp", rarity="Rare", hp=90,
            card_type="Fighting", attack="Cross Chop",
            description="One arm alone can move mountains. Using all four arms, this Pokemon fires off awesome punches.",
            weakness="Psychic", card_number=68, release_date="1996-02-27",
            evolution_stage="Final", abilities="Guts"
        )

        card10 = PokemonCard(
            name="Gengar", rarity="Rare", hp=60,
            card_type="Ghost", attack="Shadow Ball",
            description="It is said to emerge from darkness to steal the lives of those who become lost in mountains.",
            weakness="Dark", card_number=94, release_date="1996-02-27",
            evolution_stage="Final", abilities="Levitate"
        )

        pokemon_cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10]
        for card in pokemon_cards:
            card.save()
        self.stdout.write(self.style. SUCCESS (
            'Successfully created Pokemon cards.')) #<-- display success message
    def create_trainers(self):
        # Create Trainer instances
        trainer1 = Trainer(name="Red", birthdate="1990-03-15",
                        location="Pallet Town", email="red@pokemon.com")
        trainer2 = Trainer(name="Blue", birthdate="1988-06-22",
                        location="Pallet Town", email="blue@pokemon.com")
        trainer3 = Trainer(name="Cynthia", birthdate="1975-01-10",
                        location="Celestic Town", email="cynthia@sinnoh.com")
        trainer4 = Trainer(name="Ethan", birthdate="2000-12-12",
                        location="New Bark Town", email="ethan@johto.com")
        trainer5 = Trainer(name="Leaf", birthdate="1992-09-03",
                        location="Pallet Town", email="leaf@pokemon.com")
        trainer6 = Trainer(name="Lance", birthdate="1980-08-30",
                        location="Blackthorn City", email="lance@johto.com")
        trainer7 = Trainer(name="May", birthdate="1995-04-12",
                        location="Littleroot Town", email="may@hoenn.com")
        trainer8 = Trainer(name="N", birthdate="1993-11-21",
                        location="N's Castle", email="n@teamplasma.com")
        trainer9 = Trainer(name="Rosa", birthdate="1998-07-05",
                        location="Aspertia City", email="rosa@unova.com")
        trainer10 = Trainer(name="Guzma", birthdate="1997-02-24",
                            location="Po Town", email="guzma@teamskull.com")

        trainers = [trainer1, trainer2, trainer3, trainer4, trainer5,
                    trainer6, trainer7, trainer8, trainer9, trainer10]

        for trainer in trainers:
            trainer.save()

        self.stdout.write(self.style.SUCCESS('Successfully created trainers. '))
        print(f"Trainer record count: {Trainer.objects.count()}")

