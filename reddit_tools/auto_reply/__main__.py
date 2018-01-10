import click
import time
from reddit_tools.utils import get_client
import random


@click.command()
@click.argument('reply-user')
@click.argument('reply-content')
def auto_reply(reply_user, reply_content):
    print('Using reply "{}"'.format(reply_content))

    while True:
        print('Searching recent comments for user "{}".'.format(reply_user))
        for comment in get_client().inbox.unread():
            if str(comment.author) == str(reply_user):
                print('\tFound comment, replying.')
                comment.reply(reply_content)
                comment.mark_read()
                if 5 == random.choice(range(0,10,1)):
                    comment.downvote()
        print('Sleeping for 10 seconds.')
        time.sleep(10)


def main():
    auto_reply()
