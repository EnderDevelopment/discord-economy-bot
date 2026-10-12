# Discord Economy Bot

A versatile Discord bot for economy, moderation, and earning commands.

## Features

- Economy commands like balance, deposit, withdraw, pay, leaderboard, and inventory
- Moderation commands like ban, unban, kick, warn, clear_warn, timeout, untimeout, say, purge, dm, cases, usernotes_add, usernotes_clear, usernotes_view, mass, lock, and unlock
- Earning commands like daily, weekly, work, beg, fish, mine, groom, trivia, and rob

## Requirements

- Python 3.8 or higher
- discord.py 2.0 or higher
- python-dotenv

## Installation

1. Clone the repository
2. Install the requirements with `pip install -r requirements.txt`
3. Create a `.env` file with your Discord bot token
4. Run the bot with `python bot.py`

## Usage

### Economy Commands

| Command | Description |
|---------|-------------|
| /balance | Check your balance |
| /deposit <amount> | Deposit money into your bank |
| /withdraw <amount> | Withdraw money from your bank |
| /pay <user> <amount> | Pay another user |
| /leaderboard | View the leaderboard |
| /inventory | View your inventory |

### Moderation Commands

| Command | Description |
|---------|-------------|
| /ban <user> [delete_days] [reason] | Ban a user from the server |
| /unban <user> | Unban a user from the server |
| /kick <user> [reason] | Kick a user from the server |
| /warn <user> [reason] | Warn a user |
| /clear_warn <user> | Clear a warning for a user |
| /timeout <user> <duration> <reason> | Timeout a user |
| /untimeout <user> | Remove timeout from a user |
| /say <message> | Make the bot say something |
| /purge <amount> | Purge messages from the channel |
| /dm <user> <message> | Send a DM to a user |
| /cases <user> | View moderation cases for a user |
| /usernotes_add <user> <note_type> | Add a user note |
| /usernotes_clear <user> | Clear user notes |
| /usernotes_view <user> | View user notes |
| /mass <action> <users> [reason] | Mass actions on users |
| /lock <channel> [reason] | Lock a channel |
| /unlock <channel> | Unlock a channel |

### Earning Commands

| Command | Description |
|---------|-------------|
| /daily | Claim your daily reward |
| /weekly | Claim your weekly reward |
| /work | Work for money |
| /beg | Beg for money |
| /fish | Go fishing |
| /mine | Go mining |
| /groom | Groom animals |
| /trivia | Play trivia |
| /rob <user> | Rob another user |

## Configuration

Create a `.env` file with your Discord bot token:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```

---

## Generated with EnderDevelopment

This plugin was generated in minutes with [EnderDevelopment](https://enderdevelopment.com) — the AI platform that turns your ideas into working Minecraft plugins, Discord bots and FiveM scripts.

**Want your own?** [Generate this project on EnderDevelopment](https://dash.enderdevelopment.com?utm_source=github&utm_medium=readme&utm_campaign=discord-economy-bot&utm_content=bottom) — describe it in one sentence and get the full source code.