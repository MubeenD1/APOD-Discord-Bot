# APOD Discord Bot

This Discord bot retrieves NASA's Astronomy Picture of the Day (APOD) using the NASA API and sends it in the Discord channel when prompted.

## Features

- Fetch NASA's Astronomy Picture of the Day
- Option to include an explanation with the picture

## Setup

### Prerequisites

- Python 3.8 or higher
- Discord account and bot token
- NASA API key

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/nasa-apod-discord-bot.git
   cd nasa-apod-discord-bot
    ```

2. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Create a .env file in the root directory and add your Discord bot token and NASA API key:**
    ```text
    DISCORD_TOKEN=your-discord-token
    NASA_TOKEN=your-NASA-api-token
    ```
4. **Run the bot**
    ```sh
    python3 app.py
    ```
