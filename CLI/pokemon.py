import random
import csv
import argparse

pokemon_names = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Gengar", "Mewtwo",
    "Eevee", "Machop", "Gyarados", "Snorlax", "Vaporeon", "Machamp", "Dragonite",
    "Arcanine", "Lapras", "Alakazam", "Kangaskhan", "Rhydon", "Lugia", "Articuno",
    "Zapdos", "Moltres", "Raikou", "Entei", "Suicune", "Tyranitar", "Ho-Oh", "Celebi",
    "Sceptile", "Blaziken", "Swampert", "Gardevior", "Breloom", "Slaking", "Gardevoir",
    "Exploud", "Swalot", "Sharpedo", "Wailord", "Milotic", "Torterra", "Empoleon", "Infernape",
    "Staraptor", "Bibarel", "Kricketune", "Luxray", "Roselia"
]

def create_pokemon_csv(filename,num = 50):
    
    headers = ["name","level","power","is_legendary"]
    
    with open(filename,mode="w",newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers) # Write headers to the CSV file
        for _ in range(num) :
            name = random.choice(pokemon_names)
            level = random.randint(1,100)
            power = random.randint(1,100)
            is_legendary = random.choice([True, False])
            writer.writerow([name, level, power, is_legendary])
            
def get_legendary_pokemons(filename):
    with open(filename,"r",newline="") as file:
        reader = csv.DictReader(file)
        legendary_pokemons = [row for row in reader if row["is_legendary"]=="True"]
        return legendary_pokemons
    
def get_pokemon_detail(filename,pokemon_name):
    with open(filename,'r',newline='') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row['name'] == pokemon_name:
                return row

def delete_pokemon(filename, name):
    data = []
    with open(filename, mode="r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['name'] != name:
                data.append(row)
    
    with open(filename, mode="w", newline="") as csv_file:
        fieldnames = ["name", "level", "power", "is_legendary"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        
def main():
    parser = argparse.ArgumentParser(description="Pokemon data manager")
    parser.add_argument("--generate",metavar="FILENAME",type=str,help="generate pokemons using random and save it csv file")
    parser.add_argument("--legendary",metavar="FILENAME",type=str,help="Get all legendary pokemons")
    parser.add_argument("--detail",metavar=("FILENAME","NAME"),nargs=2,type=str)
    parser.add_argument('--delete',metavar=('FILENAME','NAME'),nargs=2,type=str,help='Delete one pokemon')
    args = parser.parse_args()
    print(args)
    if args.generate:
        create_pokemon_csv(args.generate)
        print(f' pokemons generated and saved in {args.generate}')
    if args.legendary:
        legendary_pokemon = get_legendary_pokemons(args.legendary)
        for row in legendary_pokemon:
            print(row)
    if args.detail:
        filename,detail=args.detail #unpack 
        details = get_pokemon_detail(filename,detail)
        if details:
            print(details)
        else: 
            print('no pokemon found')        
    if args.delete:
        filename, name = args.delete #unpack 
        delete_pokemon(filename, name)
        print(f"Deleted Pokémon '{name}' from {filename}")
    

if __name__ == "__main__":
    main()
        