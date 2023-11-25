
# Twitch Bot Readme
## Introduction
This Python script serves as a Twitch bot using the twitchio library, designed to automate certain tasks in a Twitch channel. The bot monitors the streaming status of specified channels and periodically toggles emote-only mode based on the broadcaster's streaming status.

## Features
* **Stream Monitoring**: The bot checks the streaming status of specified channels.
* **Emote-Only Mode**: Toggles emote-only mode in the chat based on the broadcaster's streaming status.
* **Periodic Routine**: The Alive routine runs every hour to check the stream status.
## Prerequisites
**Python**: Ensure you have Python installed on your system.
**Twitch Account**: Create a Twitch account and register a new application on the Twitch Developer Portal. Obtain the client ID from the registered application.
## Installation
1) Clone the repository:
`git clone https://github.com/your-username/your-twitch-bot.git`
2) go to the folder: `cd your-twitch-bot`
3) Install the required packages:
`pip install -r requirements.txt`
4) open the script and replace the token variable with your Twitch OAuth token.
## Usage
1) Run the bot:
`python your_twitch_bot.py`
2) The bot will log in to Twitch and join the specified channels.
3) The **Alive** routine will periodically check the streaming status and toggle emote-only mode accordingly.
## Customization
* **Channels**: Update the initial_channels list in the Bot class to include the channels you want the bot to join initially.
* **Prefix**: Modify the prefix parameter in the Bot class to change the command prefix.
* **Routine** Interval: Adjust the `@routines.routine(hours=1)` decorator in the **Alive** method to change the interval at which the routine runs.
## Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License
This Twitch bot script is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
* Thanks to the developers of the twitchio library for providing an easy-to-use interface for Twitch integration.
* Special thanks to the Twitch community for inspiration and support.
## Disclaimer
This script is provided as-is without any warranty. Use it responsibly and ensure compliance with Twitch's terms of service and community guidelines.