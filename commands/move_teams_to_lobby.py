import random

from commands.base_command import BaseCommand
import settings

class MPTL(BaseCommand):
    def __init__(self):
        description = "Move teams back to lobby"
        params = None
        super().__init__(description, params)
        pass

    async def handle(self, params, message, client):

        await message.delete()
        lobby_object = client.get_channel(settings.Lobby)
        room1 = client.get_channel(settings.Team1)
        room2 = client.get_channel(settings.Team2)
        sender = message.author

        user_roles = sender.roles
        if settings.Bot_Commander not in user_roles:
            pass

        people_in_channel = room1.members
        people_in_channel.extend(room2.members)

        for member in people_in_channel:
            await member.move_to(lobby_object)


        pass


