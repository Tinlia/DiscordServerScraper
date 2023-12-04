# Discord Scraper

## Overview
This Discord Scraper is a Python script designed to retrieve messages from a specific Discord channel using Discord's API. The script requires an authorization key, a channel ID, and allows you to select the specific information you want to scrape from each message. The scraped data is then saved in a CSV file for further analysis.

## Files
1. **auth_key.txt**
   - This file should contain the Discord authorization key. To obtain the key, follow the instructions provided in the script under "Fetch User Auth ID."

2. **main.py**
   - The main Python script that performs the scraping. It uses the `requests` library to make API calls to Discord and retrieves messages from the specified channel. The selected message attributes are then saved in a CSV file named `output.csv`.

3. **output.csv**
   - This CSV file stores the scraped data. Each row represents a message, and the columns contain the selected attributes for each message.

## Instructions

### Step 1: Gather Authorization Key
1. Go to Discord in your web browser.
2. Enter a server text channel.
3. Open the developer panel by pressing `Ctrl + Shift + I`.
4. Go to the "Network" tab.
5. Start typing in the channel.
6. Locate 'typing' (Type: xhr) and click on it.
7. Under "Request Headers," copy the Authorization key.
8. Paste the key into the `auth_key.txt` file.

### Step 2: Configure Selected Attributes
1. Run the script using `python main.py`.
2. Follow the prompts to select the information you want to scrape from each message.
   - Type the desired information (e.g., username, content).
   - Type "all" to select all attributes or "done" to proceed.

```
Type information you would like to scrape (i.e., username)
    [+] id
    [-] channel_id
    [-] username
    [+] content
    [-] timestamp
    [+] tts
    [-] mention_everyone
    [-] mentions
    [-] attachments
    [-] embeds
    [-] pinned
    [+] type
    [•] All
    [•] *Done
>
```
3. The output will update to display your selections.

### Step 3: Enter Channel ID
1. Enter the desired channel ID from the Request URL (e.g., `https://discord.com/channels/<CHANNEL_ID>/>`).
2. Ensure the entered ID is a valid 18-digit number.

### Step 4: Run the Script
1. Save the changes and run the script.
2. The script will fetch messages from the specified channel using the provided authorization key.
3. The scraped data will be saved in the `output.csv` file.

### Notes
- Make sure the `auth_key.txt` file is properly configured.
- Review the selected attributes to ensure the desired information is being scraped.
- The CSV file will be created in the same directory as the script.

**Notice:** Be mindful of Discord's API usage policies and ensure compliance with their terms of service. Unauthorized scraping or misuse of the API may result in account suspension. Use this script responsibly and respect privacy and usage policies.
