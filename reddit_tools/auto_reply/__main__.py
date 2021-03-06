import click
import time
from reddit_tools.utils import get_client
import random
import itertools
import string


@click.command()
@click.argument('reply-user')
@click.argument('reply-content')
def auto_reply(reply_user, reply_content):
    reply_content = reply_content.split(':') * 9999

    while True:
        for comment in get_client().inbox.unread():
            if str(comment.author) == str(reply_user):
                reply = reply_content.pop()

                print('\tFound comment, replying.')
                print(f'\tUsing reply "{reply}"')

                comment.reply(reply)
                comment.mark_read()
                if 5 == random.choice(range(0,10,1)):
                    comment.downvote()
        time.sleep(10)


def main():
    auto_reply()
