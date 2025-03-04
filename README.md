# Ru-Translit Telegram Bot

This is a Telegram bot that transliterates Latin characters to Cyrillic and fixes typos in Russian text.

[Try it out](https://t.me/rutranslit_bot?start=source=github)

## Features

- Transliterate Latin characters to Cyrillic
- Fix common typos in Russian text using Yandex Speller
- Respond to `/start` command with a welcome message

## Requirements

- Python 3.9
- Docker
- Docker Compose

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/kkoemets/ru-translit_telegram_bot.git
    cd ru-translit_telegram_bot
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a .env file with your Telegram bot token by running the setup script:

   ```bash
    bash setup_env.sh
    ```

5. Run the bot:

    ```bash
    python bot.py
    ```

## Docker Setup

1. Build and run the Docker container:

    ```bash
    docker-compose up -d --build
    ```

## Usage

- Start a conversation with your bot on Telegram.
- Send a message with Russian words written in Latin characters.
- The bot will respond with the transliterated text in Cyrillic and fix any typos.

## License

This project is licensed under the MIT License.
