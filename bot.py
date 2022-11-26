import slack

from decouple import config


OAUTH_TOKEN = config('OAUTH_TOKEN')

client = slack.WebClient(token=OAUTH_TOKEN)

client.chat_postMessage(channel='#test', text='Hello')