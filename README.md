# Tools for Reddit

## Setup
```Bash
virtualenv env -p python3.6 && source env/bin/activate
pip install -r requirements.txt
python setup.py install
```

## Creds
In the base directory, a file named `creds_file.json` needs to exist, with the following contents:
```json
{
  "client_id": "<client_id_from_reddit_app>",
  "client_secret": "<client_secret_from_reddit_app>",
  "password": "<account_password>",
  "user_agent": "<literally anything>",
  "username": "<account_username>"
}

```

## Commands

* `scrub_comments <REPLACEMENT_TEXT>`
* `auto_reply <USER_NAME> <REPLY>`

# Planned Commands

* `clone_user`
