import asyncio
import pyautogui
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, events

api_id = 'your_api_id'
api_hash = 'your_api_hash'
session_string = 'your_session_string'
username1 = 'your_game_bot_username'

client = TelegramClient(StringSession(session_string), api_id, api_hash)

# Replace these with actual coordinates
battle_button_x_coordinate = 100
battle_button_y_coordinate = 200
executioner_blade_button_x_coordinate = 150
executioner_blade_button_y_coordinate = 250

async def explore_and_battle():
    await client.start()

    while True:
        # Send "/explore" command to the game bot
        await client.send_message(username1, "/explore")

        # Wait for the game bot to reply with the challenge message
        event = await client.wait_event(events.NewMessage(from_users=[username1]))

        if "has challenged you!" in event.raw_text:
            character_name = event.raw_text.split()[0]
            print(f"Received challenge from {character_name}")

            # Check if the "Battle" button is present in the reply
            if "Battle" in event.raw_text:
                # Simulate clicking the "Battle" button
                pyautogui.click(x=battle_button_x_coordinate, y=battle_button_y_coordinate)
                
                # Continue with other actions as needed
                while True:
                    # Check for the "Executioner_Blade" button
                    if pyautogui.locateOnScreen('executioner_blade_button.png') is not None:
                        # Click the "Executioner_Blade" button
                        pyautogui.click(x=executioner_blade_button_x_coordinate, y=executioner_blade_button_y_coordinate)
                        print("Clicked Executioner_Blade button")
                        await asyncio.sleep(1)  # Adjust sleep duration as needed
                    else:
                        break  # Break the loop if the button is not found

                    # Check for the "You have defeated" message
                    messages = await client.get_messages(username1, limit=1)
                    if messages and f"You have defeated {character_name}" in messages[0].raw_text:
                        print(f"You have defeated {character_name}")
                        break  # Break the loop if the victory message is received

# Run the script
asyncio.run(explore_and_battle())

