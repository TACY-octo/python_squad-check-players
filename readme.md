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

Ce script génère un fichier de log nommé 'seed-squad.log'. 

Exemple d'output si le serveur n'est pas sur une map seed : 

```
2020-01-09 08:38:35,554 :: INFO :: ============== INFORMATION SERVER =================
2020-01-09 08:38:35,808 :: INFO :: Nombre de joueurs sur le serveur : 0
2020-01-09 08:38:36,006 :: INFO :: MAP en cours sur le serveur : Yehorivka v2
2020-01-09 08:38:36,210 :: INFO :: Le serveur est actuellement vide, redemarrage en cours pour une map SEED
```

Exemple d'output si le serveur n'est pas sur une map seed : 

```
2020-01-09 09:00:33,282 :: INFO :: ============== INFORMATION SERVER =================
2020-01-09 09:00:33,521 :: INFO :: Nombre de joueurs sur le serveur : 0
2020-01-09 09:00:33,736 :: INFO :: MAP en cours sur le serveur : Yehorivka Skirmish v2
2020-01-09 09:00:34,169 :: INFO :: Aucun reload seed est necessaire.
```


