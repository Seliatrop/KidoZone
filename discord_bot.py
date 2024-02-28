import matplotlib.pyplot as plt
from datetime import datetime
import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def plot_points_with_time_and_image(carte_type, duree):
    # Obtenir l'heure actuelle
    current_time = datetime.now().strftime("%H:%M:%S")

    # Coordonnées des points
    y = [0.5, 1.90, 3.2]
    x = [5.8, 3.88, 3.25]

    # Valeurs associées à chaque point
    values = [f"{duree}"] * len(x)

    # Fixer la taille de la figure et les limites des axes
    plt.figure(figsize=(8, 6))  # Vous pouvez ajuster les valeurs (largeur, hauteur) selon vos besoins
    plt.xlim(0, 8)  # Ajustez ces valeurs selon vos besoins pour définir les limites en x
    plt.ylim(0, 4)  # Ajustez ces valeurs selon vos besoins pour définir les limites en y

    # Créer le graphique avec les points
    plt.scatter(x, y)

    # Ajouter du texte en dessous du graphique avec l'heure actuelle
    plt.text(2.5, 0, f"Heure actuelle: {current_time}", ha='center')

    # Ajouter du texte en bas de chaque point
    for i, value in enumerate(values):
        plt.text(x[i], y[i] - 0.1, value, ha='center')  # Ajustez le décalage y selon vos besoins

    # Ajouter une image en fond du graphique
    img = plt.imread('img.png')
    plt.imshow(img, extent=[0, 8, 0, 4], aspect='auto')

    # Configurer les axes et le titre
    plt.xlabel('Axe X')
    plt.ylabel('Axe Y')
    plt.title(f'Rizière - Carte {carte_type}')

    # Enregistrez le graphique au lieu de l'afficher directement
    plt.savefig('carte.png')

# Appeler la fonction pour afficher le graphique
# plot_points_with_time_and_image()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('?carte'):
        # Extraire le type de carte et la durée à partir du message
        _, carte_type, duree = message.content.split()

        # Appeler la fonction pour générer le graphique
        plot_points_with_time_and_image(carte_type, duree)

        # Envoyer le graphique généré sur le canal Discord
        await message.channel.send(file=discord.File('carte.png'))

# On récupère notre token discord dans l'env de Railway
bot_token = os.environ.get("DISCORD_BOT_TOKEN")

# Pour lancer le bot
client.run(bot_token)
