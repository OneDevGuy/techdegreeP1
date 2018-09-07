import csv

has_xp = []
no_xp = []

def get_players(player_info):
    """ Takes a CSV file are parses each row to two list,
        then calls create_teams() to sort each player into teams """
    file = player_info

    with open(file, newline='') as csvfile:
        fieldnames = ['name', 'height', 'experience', 'guardians']
        reader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)
        rows = list(reader)
        for row in rows:
            if row['experience'] == 'NO':
                no_xp.append([row['name'], row['experience'], row['guardians']])
            elif row['experience'] == 'YES':
                has_xp.append([row['name'], row['experience'], row['guardians']])
            else:
                del row
        create_teams()


def create_teams():
    """ Takes the 2 lists from get_players() and
        spits them in to 3 teams and writes them
        to teams.txt """
    sharks = ''
    dragons = ''
    raptors = ''
    for player in has_xp[0:3] + no_xp[0:3]:
        sharks += ', '.join(player) + '\n'
    for player in has_xp[3:6] + no_xp[3:6]:
        dragons += ', '.join(player) + '\n'
    for player in has_xp[6:] + no_xp[6:]:
        raptors += ', '.join(player) + '\n'
    with open('teams.txt', 'w') as file:
        file.writelines('Sharks\n'+ sharks +'\n'
        + 'Dragons\n' + dragons + '\n' + 'Raptors\n' + raptors)



if __name__ == "__main__":
    get_players('soccer_players.csv')
