import json
import os.path

from op import get_secure_note_field, run_op_command

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]
OP_VAULT = "Google API"
OP_ITEM = "Google Tasks API"


def get_tasks_api_credentials():
    """ Get credentials for Google Tasks API """

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # TODO Store token in 1Password
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # TODO How to do this without human interaction?
            run_op_command(["op", "signin"])
            secrets_json = get_secure_note_field(OP_VAULT, OP_ITEM, "desktop-credentials.json")
            client_config = json.loads(secrets_json)
            flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())

    return creds