``` Version : 0.1 ````

# Objectif 
Redémarrer le serveur si aucun joueur n'est présent et si le serveur n'est pas sur une map Skirmish (plus petite pour le seed). 

# Utilisation 

Ce script est exécuté dans un job cron.d. 

Les valeurs à renseigner sont : 
- url (obligatoire) : L'url de l'API du battlemetrics du serveur. (ex: https://api.battlemetrics.com/servers/4131310). 
- command (obligatoire) : La commande a utiliser pour redémarrer / relancer le serveur sur une map Skirmish. 
- loginfo (facultatif) : Permet de reglérer le niveau de logging du script. 

Commande à utiliser dans un fichier crond : 

```
python seed-squad.py --url https://api.battlemetrics.com/servers/4131310 --command 'echo redémarrage'   
```
