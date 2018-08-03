import os
from slackclient import SlackClient

#SLACK_TOKEN = os.environ.get('xoxp-403592011893-403226331636-411825076390-5fe05bc62b53451bfc582b8d93da05d9')

SLACK_TOKEN = 'xoxp-403592011893-403226331636-411825076390-5fe05bc62b53451bfc582b8d93da05d9'

slack_client = SlackClient(SLACK_TOKEN)

def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None

if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for c in channels:
            print(c['name'] + " (" + c['id'] + ")")
    else:
        print("Unable to authenticate.")
