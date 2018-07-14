# reasons
Discord bot to display unique image macros from Inspirobot.me <br />

## Requirments
Python 3.x and PIP
```
pip install requests
pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
```

## Installation
Head over to https://discordapp.com/developers/applications/me and create a new app. <br />
Click on "Create Bot User". <br />
Once done, you can get the secret bot token. <br />
In reason.py replace all <...> with appropriate information. <br />

To start bot, run:
```
python reasons.py
```
To add bot to server add your CLIENT_ID to this URL and visit in browser:  <br />
https://discordapp.com/oauth2/authorize?client_id=<YOUR_BOT_CLIENT_ID_GOES_HERE> <br />

## Usage
When bot is active in server, just type "$reason".
