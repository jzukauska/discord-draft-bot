import random

from commands.base_command import BaseCommand
import settings

class MPTT(BaseCommand):
    def __init__(self):
        description = "Randomly assign players to a color and move them to a room"
        params = None
        super().__init__(description, params)
        pass

    async def handle(self, params, message, client):

        await message.delete()
        lobby_object =  client.get_channel(settings.Lobby)
        room1 =  client.get_channel(settings.Team1)
        room2 =  client.get_channel(settings.Team2)
        sender = message.author

        user_roles = sender.roles
        if settings.Bot_Commander not in user_roles:
            pass


        people_in_channel = lobby_object.members

        team_toggle = True
        team1 = []
        team2 = []

        random.shuffle(people_in_channel)

        for member in people_in_channel:
            if team_toggle is True:
                team1.append(member)
            else:
                team2.append(member)
            team_toggle = not team_toggle

        for member in team1:
            await member.move_to(room1)

        for member in team2:
            await member.move_to(room2)

        pass


