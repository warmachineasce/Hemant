import asyncio
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, events, Button

api_id = 'your_api_id'
api_hash = 'your_api_hash'
session_string = 'your_session_string'
username1 = 'your_game_bot_username'

client = TelegramClient(StringSession(session_string), api_id, api_hash)

async def explore_and_battle():
    await client.start()

    while True:
        # Send "/explore" command to the game bot
        await client.send_message(username1, "/explore")

        # Wait for the game bot to reply with the challenge message and option
        @client.on(events.NewMessage(from_users=[username1]))
        async def handle_challenge(event):
            if "has challenged you!" in event.raw_text:
                character_name = event.raw_text.split()[0]
                print(f"Received challenge from {character_name}")

                # Simulate clicking the "Battle" button
                await event.reply("Simulating click on 'Battle' button")

                # Additional actions after clicking the "Battle" button
                await asyncio.sleep(1)  # Adjust sleep duration as needed

                # Continue with the rest of the script as needed

                # Simulate clicking the "Executioner_Blade" button
                message = await event.reply("Choose an option:",
                                            buttons=[[Button.inline("Battle", data="battle_option"),
                                                      Button.inline("Executioner_Blade", data="executioner_blade_option")]])

                # Continuously click the "Executioner_Blade" button until victory message is received
                while True:
                    await message.edit(buttons=[[Button.inline("Executioner_Blade", data="executioner_blade_option")]])
                    await asyncio.sleep(1)  # Adjust sleep duration as needed

                    # Check for the "You have defeated" message
                    messages = await client.get_messages(username1, limit=1)
                    if messages and "You have defeated" in messages[0].raw_text:
                        print("You have defeated an opponent")
                        break  # Break the loop if the victory message is received

                # Send "/explore" after victory
                await client.send_message(username1, "/explore")

        # Run the event loop until disconnected
        await client.run_until_disconnected()

# Run the script
asyncio.run(explore_and_battle())
                
