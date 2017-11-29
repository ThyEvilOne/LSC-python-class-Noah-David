errorInt = 1


def stats_add():
        player_stats = open('golf.txt', 'a')
        player_name = str(input('Enter Name of player: '))
        player_score = int(input('Enter Score of player: '))
        player_stats.write('%s  %s\n' %(player_name, player_score))
        player_stats.close()

while errorInt == 1:
        try:
                players = int(input('Enter how many players to add to file: '))

                for i in range(players):
                        stats_add()
                errorInt = 0
        except ValueError:
                print('Invalid data type. Name must be String and Score integer')
