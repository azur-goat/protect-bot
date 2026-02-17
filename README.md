# Ultimate Protection Bot 🔒

Version : 1.0.0\
Langage : Python 3.11+\
Librairie : discord.py 2.x

------------------------------------------------------------------------

## 💎 Description

Ultimate Protection Bot est un bot anti-nuke / sécurité totale pour
serveurs Discord.

Il protège contre :

-   Création / suppression / modification de salons
-   Création / suppression / modification de rôles
-   Bannissements et kicks non autorisés
-   Ajout ou suppression de bots
-   Emojis, stickers, webhooks et soundboard
-   Comptes récents suspects (anti-alt)
-   Patterns selfbot et spam
-   Token leaks
-   Modifications serveur (nom, icône, bannière)
-   Actions massives (anti-nuke)

Seul le OWNER_ID défini dans config.py peut effectuer des actions
internes.

------------------------------------------------------------------------

## 📁 Structure du projet

core/ → Modules centraux\
cogs/ → Protection événements\
security/ → Sécurité avancée\
database/ → Backups, logs, stockage crypté\
utils/ → Fonctions utilitaires\
main.py → Point d'entrée

------------------------------------------------------------------------

## ⚙️ Installation

1.  Installer les dépendances :

pip install -r requirements.txt

2.  Configurer config.py :

OWNER_ID = TON_ID_DISCORD\
TOKEN = TON_TOKEN

3.  Lancer le bot :

python main.py

------------------------------------------------------------------------

## 🛡️ Fonctionnalités

✔ Protection anti-nuke totale\
✔ Backup automatique complet\
✔ Restore automatique\
✔ Mode parano (freeze serveur)\
✔ Logs sécurité persistants\
✔ Chiffrement AES pour données sensibles\
✔ Système anti faux-positifs

------------------------------------------------------------------------

## 📌 Important

Le bot doit avoir la permission Administrateur. Ne partage jamais ton
token.
