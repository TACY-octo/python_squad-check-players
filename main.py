import json 
import urllib.request
import logging
import os

class SquadStats():
    '''
        Instance object
    '''
    def __init__(self, battlemetrics_url, command_execute):
        self.battlemetrics_url = battlemetrics_url
        self.command_execute = command_execute

    '''
        Get stats from Battlemetric API
    '''
    def get_stats(self):
        request = urllib.request.urlopen(self.battlemetrics_url)
        if(request.getcode()==200):
            response = request.read()
            self.server_stats = json.loads(response)
            return self.server_stats

    '''
        Get count player in game server
    ''' 
    def get_countplayer(self):
        self.get_stats() 
        self.server_countplayer = self.server_stats['data']['attributes']['players']
        return self.server_countplayer

    def reload_mapseed(self):
        
        # Use method for actualize player
        self.get_countplayer()

        # If the count is equal to 0 
        if self.server_countplayer == 0: 
            print('Le serveur est actuellement vide, redémarrage en cours pour une map SEED')
            os.system(self.command_execute)
        # Else the count is not equal to 0 
        else:
            print('Le serveur est plein : {0}'.format(self.get_countplayer()))
    
def main():
    # Instance server 
    server_exacted = SquadStats('https://api.battlemetrics.com/servers/4131310','echo "Bonjour !"')
    # Checking players online in the server and reload with a map 'SEED' if the count equal 0. 
    server_exacted.reload_mapseed()
    
main()
