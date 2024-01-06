import asyncio
import pyautogui
from telethon.sync import TelegramClient, events

api_id = '21124978'
api_hash = 'T47PWyCvxwJ5iZFSf3XFRw3QaGOILq2c'
session_string = '1BVtsOMgBuzMHr2PoXkLqH1EAKb3Il_bNri_WlPVKEi49UALTfMVwiZIBnRCkrK8CEiOzd9n-MyRkHvJ_p0z6QILYAk9FuGR5MGd0aBoYqZAzw7B0zknrHOE-1gZRC6jxbw07zGJPcmya2CMsRE3Gtjy5Y6wGF0rwfx8_hPkunPbLH98pSV8pvz3ZmK7ivvj0J1P3dVS_Ly0EnjdSVcGD3GImJUTIZmNTUYk3u8xbsTR95to2h73NdFfh-QMLuFGm4UhAZzc0unCg3B_IuoqDHqrx6v32Qx8yclyCq0Dg_8l7xrprYMDwhRtp23dl7BQxby_xUGMkhvFWgcWLsWU-ECOFX9kQMXQ='
username1 = '@Naruto_X_Boruto_Bot'

client = TelegramClient(StringSession(session_string), api_id, api_hash)

async def explore_and_battle():
    await client.start()

    while True:
        # Send "/explore" command to the game bot
        await client.send_message(username1, "/explore")

        # Wait for the game bot to reply with the challenge message
        @client.on(events.NewMessage(from_users=[username1]))
        async def handle_challenge(event):
            if "has challenged you!" in event.raw_text:
                character_name = event.raw_text.split()[0]
                print(f"Received challenge from {character_name}")

                # Simulate clicking the "Battle" button
                pyautogui.click(x=your_battle_button_x_coordinate, y=your_battle_button_y_coordinate)

                # Continuously click the "Executioner_Blade" button
                while True:
                    # Check for the "Executioner_Blade" button
                    if pyautogui.locateOnScreen('executioner_blade_button.png') is not None:
                        # Click the "Executioner_Blade" button
                        pyautogui.click(x=executioner_blade_button_x_coordinate, y=executioner_blade_button_y_coordinate)
                        print("Clicked Executioner_Blade button")
                        await asyncio.sleep(2)  # Adjust sleep duration as needed
                    else:
                        break  # Break the loop if the button is not found

                    # Check for the "You have defeated" message
                    messages = await client.get_messages(username1, limit=1)
                    if messages and f"You have defeated {character_name}" in messages[0].raw_text:
                        print(f"You have defeated {character_name}")
                        break  # Break the loop if the victory message is received

                # Stop the event handler after handling the battle
                client.remove_event_handler(handle_challenge)

        # Wait for the victory message
        await client.run_until_disconnected()

# Run the script
asyncio.run(explore_and_battle())
