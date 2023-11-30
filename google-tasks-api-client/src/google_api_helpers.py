from typing import Any
import json, os

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

from security.op_cli import get_secure_note_field, run_op_command


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]
OP_VAULT = "Google API"
OP_ITEM = "Google Tasks API"


def get_tasks_api_credentials() -> Credentials:
    """ Get credentials for Google Tasks API from 1Password"""

    creds: Credentials = None
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
            secrets_json: str = get_secure_note_field(OP_VAULT, OP_ITEM, "desktop-credentials.json")
            client_config: Any = json.loads(secrets_json)
            flow: InstalledAppFlow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())

    return creds


def get_task_service():
    """ Get a Google Tasks API service object.

    This function retrieves the Google Tasks API service object by obtaining the necessary credentials
    and building the service using the tasks version 1.

    Returns:
        The Google Tasks API service object.
    """

    creds: Credentials = get_tasks_api_credentials()
    service: Any = build("tasks", "v1", credentials=creds)
    return service
