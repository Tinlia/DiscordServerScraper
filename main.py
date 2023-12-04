import requests
import json
import csv
from pathlib import Path

def retrieve_msg(channel_id, auth_id):
    headers = {
        'authorization': auth_id
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers = headers)
    scrape = json.loads(r.text)
    print(str(scrape))
    # Specify the CSV file path
    csv_file_path = Path(__file__).parent / 'output.csv'
    with open(csv_file_path, 'w') as csvfile:
        # Initialize fieldnames
        fieldnames = [sel.title() for sel in selected]
        
        # Create a CSV writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header row
        writer.writeheader()
        
        # Write data rows
        for value in scrape:
            # ID
            ID = "ID: " + str(value['id'])
            # Channel ID
            Channel = "Channel: " + str(value['channel_id'])
            # Username
            Username = "Username: " + str(value['author']['username'] + "#" + value['author']['discriminator'])
            # Content
            Content = "Content: " + str(value['content'])
            # Timestamp
            Timestamp = "Timsetamp: " + str(value['timestamp'])
            # Tts
            Tts = "Tts: " + str(value['tts'])
            # @everyone
            Everyone = "Everyone: " + str(value['mention_everyone'])
            # Mentions
            Mentions = "Mentions: " + str(value['mentions'])
            # Attachments
            Atts = "Atts: " + str(value['attachments'])
            # Embeds
            Embeds = "Embeds: " + str(value['embeds'])
            # Pinned
            Pinned = "Pinned: " + str(value['pinned'])
            # Type (For Types, see https://discord.com/developers/docs/resources/channel#message-object-message-types)
            Type = "Type: " + str(value['type'])
            
            # List of types
            values = [ID, Channel, Username, Content, Timestamp, Tts, Everyone, Mentions, Atts, Embeds, Pinned, Type]
            
            post = {}
            for x in selected:
                post[x.title()] = values[types.index(x.lower())]
            # Write the fields to the CSV file
            writer.writerow(post)    
        
        print(f"Data written to {csv_file_path}")

selected = []
types = ['id', 'channel_id', 'username', 'content', 'timestamp', 
         'tts', 'mention_everyone', 'mentions', 'attachments', 
         'embeds', 'pinned', 'type']

# Gather Selected Values
while True:
    print("\n\n\n\n\n\nType information you would like to scrape (i.e., username)")
    
    # Changes Display for selected/unselected values
    for type in types:
        print("  [+] " + type if type in selected else "  [-] " + type)
    print("  [•] All")
    print("  [•] *Done")
    val = input(">")
    print("Value: " + val)
    
    # If done, move onto next step
    if val.lower() == "done":
        break
    # If all, select or deselect all
    elif val.lower() == "all":
        if selected == types:
            selected = []
        else:
            selected = types;
    # If not an option, invalidate entry
    elif not val in types:
        print("\nInvalid Entry")
    # If not already picked, add to selected
    elif not val.lower() in selected:
        selected.append(val.lower())
    # If already picked, remove from selected
    else:
        selected.pop(selected.index(val))

# Fetch Channel ID
while True:
    print("\n\n\n\n\n\n\nEnter desired channel ID from Request URL (i.e., https://discord.com/api/v9/channels/<CHANNEL_ID>/)")
    channel_id = input("> ")
    if channel_id.isdigit() and len(channel_id)==18:
        break
    else:
        print("Invalid Input.")

# Fetch User Auth ID
# To find this value:
    # Go to discord on your web browser
    # Enter a server text channel
    # Do ctrl+shift+i to open the dev panel
    # Go to the Network Tab
    # Start typing in the channel
    # locate 'typing' (Status: 204, Type: xhr) and click on it
    # Under "Request Headers" copy the Authorization key and paste into auth_key.txt
print("\n\n\n\n\n\n")
while True:
    print("\nEnter authorization key as a file")
    with open('auth_key.txt', 'r') as file:
        auth_id = file.read().strip()
    if auth_id == "" or auth_id == "<AUTH_KEY>":
        print("Error: Please ensure that auth_key.txt is properly configured")
    else:
        retrieve_msg(channel_id, auth_id)
        print("\n\n\n\n\n\n\n\n\n\tDone!\n\n\n")
        break;
