import csv

def save_to_file(players):
    file = open('players.csv', mode='w', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['name', 'overall', 'position', 'link'])
    for player in players:
        writer.writerow(player.values())
    return