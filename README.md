# Discord Screenshot Bot

Type `!shot` in Discord and the bot posts a screenshot of your PC. Handy for checking in on AFK stuff.

## Setup

1. Install dependencies:
   ```
   pip install discord.py mss python-dotenv
   ```
2. In the [Discord Developer Portal](https://discord.com/developers/applications), create a New Application, then open the **Bot** tab:
   - Copy the bot token.
   - Enable **Message Content Intent**.
3. Under **OAuth2 → URL Generator**, pick scope `bot` and permissions **Send Messages**, **Attach Files**, and **Read Message History**. Open the generated URL and add the bot to your server.
4. Copy `.env.example` to `.env` next to `screenshot_bot.py` and fill it in:
   - `DISCORD_TOKEN`: your bot token.
   - `OWNER_ID`: your Discord user ID (Settings → Advanced → enable Developer Mode, then right-click yourself → Copy User ID).
5. Run it:
   ```
   python screenshot_bot.py
   ```

## Usage

| Command    | Result                                  |
|------------|-----------------------------------------|
| `!shot`    | Screenshot of all monitors              |
| `!shot 1`  | Just monitor 1 (`!shot 2` for the second) |

## Notes

- The bot only responds to the user ID in `OWNER_ID`. It can see your whole screen, so keep it in a private server or channel.
- It has to be running on the PC. Put it in a terminal window or start it at login with Task Scheduler.
- If the PC is asleep or the screen is locked, nothing useful will be captured.
- Slopped together.
