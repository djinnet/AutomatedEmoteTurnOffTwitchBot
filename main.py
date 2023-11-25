import requests
from twitchio.ext import commands, routines

token = ''


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=token, prefix='&', initial_channels=["", ""])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @routines.routine(hours=1)
    async def Alive(self, ctx: commands.Context):
        if ctx.author.is_mod:
            broadcaster = self.create_user(self.user_id, self.nick)
            isalive = checkIfUserIsStreaming(broadcaster.channel.name)
            emote_mode = False
            if isalive:
                print("/emoteonlyoff")
                emote_mode = False
            else:
                print("/emoteonly")
                emote_mode = True
            await broadcaster.update_chat_settings(token=token, moderator_id=self.user_id, emote_mode=emote_mode)


def checkIfUserIsStreaming(username):
    url = "https://gql.twitch.tv/gql"
    query = "query {\n  user(login: \"" + username + "\") {\n    stream {\n      id\n    }\n  }\n}"
    return True if requests.request("POST", url, json={"query": query, "variables": {}}, headers={"client-id": "kimne78kx3ncx6brgo4mv6wki5h1ko"}).json()["data"]["user"]["stream"] else False


if __name__ == '__main__':
    bot = Bot()
    bot.run()
