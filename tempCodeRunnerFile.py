for filename in os.listdir('./Moderator'):
    if filename.endswith('.py'):
        client.load_extension(f'Moderator.{filename[:-3]}')

for filename in os.listdir('./AIchat'):
    if filename.endswith('.py'):
        client.load_extension(f'AIchat.{filename[:-3]}')