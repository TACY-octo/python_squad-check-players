# Objectif 

Vérifier le nombre de personne connecter sur un serveur de jeux, relancer une map "SEED" si aucun joueur n'est connecté...

# Utilisation 

Ce script est exécuté dans un job cron.d. 

Les paramètres sont déjà renseignés dans le script. 

Pour les modifiers, changer les valeurs suivantes : 
``` 
battlemetric_url={{ l'url battlemetric du serveur }}
command={{ commande à exécuter sur le serveur d'où est lancé le script }}
```

Lancer le script mannuellement : 

```
python main.py
```
