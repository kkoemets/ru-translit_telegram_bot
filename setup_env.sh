#!/bin/bash

echo "Welcome to the Telegram Bot setup script!"
echo ""
read -p "Please enter your Telegram Bot Token: " TELEGRAM_BOT_TOKEN

cp .env_example .env
sed -i '' "s/your_telegram_bot_token_here/$TELEGRAM_BOT_TOKEN/" .env

echo ""
echo "Your .env file has been created successfully!"
