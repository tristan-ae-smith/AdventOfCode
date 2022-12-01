from math import sqrt
# You are given three files with information
# about boats. File number one has hull form data, file number two has
# engine data, and file number three has type information about the
# ships. (Because CodePair doesn't support file access, we've included them as
# strings)You can determine the predicted speed of the ships by combining
# the hull form data and engine data.

# The boat’s velocity is given by the following equation.
# V=234.5 *(B/P)* SQRT(L)
# Where B is the Beam of the ship, L is the length at the water
# line, and P is the power of the ship’s power plant.

# Give me the five fastest battleships in ascending order.
# Give me the slowest ten cruisers in ascending order.

# Name,Power
fileEngine = '''South Carolina,16500
Michigan,16500
Delaware,25000
Utah,28000
Texas,28100
Mississippi,32000
California,29000
West Virginia,28900
Cleveland,100000
Atlanta,75000
Helena,100000
Honolulu,100000
Pheonix,100000
Boston,120000
Pittsburgh,120000'''

# Name,Length,Beam
fileHull = '''South Carolina,450,80.3
Michigan,450,80.3
Delaware,510,85.3
Utah,510,88.3
Texas,565,95.2
Nevada,583,95.2
Mississippi,624,97.5
California,600,114
West Virginia,624,114
Cleveland,610,66.4
Atlanta,541,53
Helena,608,61.5
Honolulu,608,61.7
Pheonix,608,61.7
Boston,673.5,70
Pittsburgh,673.5,71'''

# Name,Type
fileType = '''South Carolina,Battleship
Michigan,Battleship
Delaware,Battleship
Utah,Battleship
Texas,Battleship
Nevada,Battleship
California,Battleship
West Virginia,Battleship
Cleveland,Cruiser
Atlanta,Cruiser
Helena,Cruiser
Honolulu,Cruiser
Pheonix,Cruiser
Boston,Cruiser
Pittsburgh,Cruiser
Lexington,Carrier
Satatoga,Carrier
Yorktown,Carrier
Enterprise,Carrier
Hornet,Carrier
Franklin,Carrier'''

ships = {}
#read files into ships dict
for shipE in fileEngine.split('\n'):
    name, engine = shipE.split(',')
    ships[name] = {'engine': int(engine)}

for shipH in fileHull.split('\n'):
    name, length, beam = shipH.split(',')
    if name in ships:
        ships[name]['length'] = float(length)
        ships[name]['beam']= float(beam)
        
for shipT in fileType.split('\n'):
    name, sType = shipT.split(',')
    if name in ships:
        ships[name]['type'] = sType 



shipVels = {'Carrier': [], 'Battleship': [], 'Cruiser': []}
for name, ship in ships.items():
    # V=234.5 *(B/P)* SQRT(L)
    velocity = 234.5 * (ship['beam']/ship['engine']) * sqrt(ship['length'])
    if 'type' in ship:
        shipVels[ship['type']].append([name, velocity])
    
# print(ships)


# Give me the five fastest battleships in ascending order.
# Give me the slowest ten cruisers in ascending order.
shipVels['Battleship'].sort(key = lambda x : x[1])
shipVels['Cruiser'].sort(key = lambda x : x[1])

print(shipVels['Battleship'][-5:])
print(shipVels['Cruiser'][:10])

