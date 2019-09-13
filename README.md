# reasons
Discord bot to display unique image macros from Inspirobot.me <br />

## Dependencies

* python >= 3.6
* pip
    * requests >= 2.22.0
    * discord.py >= 1.2.3

## Installation
Head over to [Discord](https://discordapp.com/developers/applications/me "Discord") and create a new app. <br />
Record your *Client_ID*. On the left, click *Bot*, and then *Add Bot*. <br />
Once you are done setting up your bot, record the *Token*, *Client ID*, and *Client Secret*. <br />

In reasons.py replace all <...> with appropriate information. <br />

To start bot, run:
```
python reasons.py
```
To add bot to server add your CLIENT_ID to this URL and visit in browser:  <br />
"https://discordapp.com/oauth2/authorize?client_id=<YOUR_BOT_CLIENT_ID_GOES_HERE>&scope=bot" <br />

## Usage
When bot is active in server, just type "$inspire".
