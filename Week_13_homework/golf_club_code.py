players = int(input('Enter how many players to add to file: '))

def stats_add():
        player_stats = open('golf.txt', 'a')
        
        player_name = input('Enter Name of player: ')
        player_score = input('Enter Score of player: ')

        player_stats.write('%s  %s\n' %(player_name, player_score))
        player_stats.close()

for i in range(players):
        stats_add()
