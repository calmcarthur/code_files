from socket import CAN_RAW_ERR_FILTER
import nba_api

# bron = 2544
threepointers = input('Three Pointers(/50):')
freethrows = input('Free Throws(/25):')
jumpers = input('Jumpers(/25):')

threepointers1 = int(threepointers)
freethrows1 = int(freethrows)
jumpers1 = int(jumpers)

playernum = input('Enter Player ID for comparison:')

print('Personal Stats:')
print('Three Pointers: ', threepointers1/50*100,'%')
print('FreeFree Throws: ', freethrows1/25*100,'%')
print('Jumpers:', jumpers1/25*100,'%')
print()
print('Lebron James Career Stats:')

from nba_api.stats.library.parameters import SeasonAll_Time
from nba_api.stats.static.players import _get_player_dict

from nba_api.stats.static import players 
player_dict = players.get_players()
bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]

from nba_api.stats.endpoints import playercareerstats

careetstats = playercareerstats.PlayerCareerStats(player_id= playernum)
careetstats.get_data_frames()
