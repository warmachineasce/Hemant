import asyncio
import pyautogui
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, events

api_id = 'your_api_id'
api_hash = 'your_api_hash'
session_string = 'your_session_string'
username1 = 'your_game_bot_username'

client = TelegramClient(StringSession(session_string), api_id, api_hash)

# Replace these with the actual coordinates
battle_button_x_coordinate = 100
battle_button_y_coordinate = 200
executioner_blade_button_x_coordinate = 150
executioner_blade_button_y_coordinate = 250

async def explore_and_battle():
    await client.start()

    while True:
        # Send "/explore" command to the game bot
        await client.send_message(username1, "/explore")

        # Wait for 2 seconds
        await asyncio.sleep(2)

        # Simulate clicking the "Battle" button
        pyautogui.click(x=battle_button_x_coordinate, y=battle_button_y_coordinate)
        
        # Wait for 2 seconds before clicking "Executioner_Blade"
        await asyncio.sleep(2)

        # Continue clicking "Executioner_Blade" every 2 seconds until victory
        while True:
            # Simulate clicking the "Executioner_Blade" button
            pyautogui.click(x=executioner_blade_button_x_coordinate, y=executioner_blade_button_y_coordinate)
            print("Clicked Executioner_Blade button")

            # Wait for 2 seconds
            await asyncio.sleep(2)

            # Check for the "You have defeated" message
            messages = await client.get_messages(username1, limit=1)
            if messages and "You have defeated" in messages[0].raw_text:
                print("You have defeated an opponent")
                break  # Break the loop if the victory message is received

# Run the script
asyncio.run(explore_and_battle())

