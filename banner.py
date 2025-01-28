from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Load player data
data_file = "player_data.csv"  # Update path to your CSV file
players = pd.read_csv(data_file)

# Load the banner template
template_path = "team_banner_template.jpg"  # Update path to your banner template
output_path = "team_banner_output.jpg"  # Path to save the final banner
match_title = "Week1 Line2"
address = "James Creek Tennis \n 3525 Melody Mizer Ln, Cumming, GA 30041 \n Feb 5th 1800 hrs"
team1 = "hyd"
team2 = "bengal"

# Define layout for players (example: 2x2 grid for 4 players)
photo_size = (150, 150)
photo_coords = [(30, 970), (30, 1210), (1230, 1010), (1260, 1240)]
name_coords = [(350, 1070), (350, 1280), (930, 1090), (960, 1280)]
match_coords = (590,350)
address_coords = (350,1420)
team1_coords = (270, 550)
team2_coords = (980, 550)
team_photo_size = (250, 250)
font_path = "arial.ttf"  # Path to a TTF font file
font_size = 40
match_font_size = 60
font = ImageFont.truetype(font_path, font_size)
match_font = ImageFont.truetype(font_path, match_font_size)
team1_photo_path = "photos/" + team1 + ".jpg"
team2_photo_path = "photos/" + team2 + ".jpg"

# Open the banner template
banner = Image.open(template_path)
draw = ImageDraw.Draw(banner)

# Iterate through the first 4 players and add them to the banner
for i, (_, row) in enumerate(players.iterrows()):
    if i >= 4:  # Stop after 4 players
        break
    
    name = row["name"]
    photo_path = row["photo_path"]

    # Add the player photo
    if os.path.exists(photo_path):
        player_photo = Image.open(photo_path).resize(photo_size)
        banner.paste(player_photo, photo_coords[i])
    else:
        print(f"Photo not found for {name}, skipping photo.")

    # Add the player name
    draw.text(name_coords[i], name, font=font, fill="black")
    draw.text(match_coords, match_title, font=match_font, fill="red")
    draw.text(address_coords, address, font=font, fill="green")
    team1_photo = Image.open(team1_photo_path).resize(team_photo_size)
    team2_photo = Image.open(team2_photo_path).resize(team_photo_size)
    banner.paste(team1_photo, team1_coords)
    banner.paste(team2_photo, team2_coords)

# Save the final banner
banner.save(output_path)
print(f"Saved team banner with 4 players at {output_path}")
