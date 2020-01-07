import json 
import urllib.request
import logging
from logging.handlers import RotatingFileHandler
import click
import os

class SquadServer():
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
        else: 
            exit(1)
    '''
        Get count player in game server
    ''' 
    def get_countplayer(self):
        self.get_stats() 
        self.server_countplayer = self.server_stats['data']['attributes']['players']
        return self.server_countplayer

    '''
        Get map 
    '''
    def get_map(self):
        return self.server_stats['data']['attributes']['details']['map']

    def reload_mapseed(self):
        
        # Use method for actualize player
        self.get_countplayer()
        logging.info('============== INFORMATION SERVER =================')
        logging.info('Nombre de joueurs sur le serveur : {0}'.format(self.get_countplayer()))
        logging.info('MAP en cours sur le serveur : {0}'.format(self.get_map()))

        # If the count is equal to 0 
        if self.server_countplayer == 0: 
            logging.info('Le serveur est actuellement vide, redémarrage en cours pour une map SEED')
            os.system(self.command_execute)
        # Else the count is not equal to 0 
        else:
            logging.info('Aucun reload seed est nécessaire.'.format(self.get_countplayer()))
    
@click.command()
@click.option('--url', prompt='L\'url battlemetric du server', help='Vous devez renseigner l\'url battlemetric du serveur')
@click.option('--command', prompt='Commande à exécuter',help='La commande à utiliser pour relancer le serveur sur une map seed.')
@click.option('--loglevel', help="Niveau de log pour le script --loglevel=INFO, --loglevel=DEBUG")
def main(url, command, loglevel):
    '''
        Configuraiton log. 
    '''
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    file_handler = RotatingFileHandler('squad_seedreload.log', 'a', 1000000, 1)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Instance server 
    server_exacted = SquadServer(url, command)

    # Checking players online in the server and reload with a map 'SEED' if the count equal 0. 
    server_exacted.reload_mapseed()

if __name__ == '__main__':
    main()
