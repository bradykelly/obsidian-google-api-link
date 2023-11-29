import json
import os.path
import string

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from op import get_secure_note_field, run_op_command
from google_auth import get_tasks_api_credentials
from config import default_max_list_size


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]
OP_VAULT = "Google API"
OP_ITEM = "Google Tasks API"


def main():
    """Shows basic usage of the Tasks API.
    Prints the title and ID of the first 10 task lists.
    """

    lists = get_task_lists()
    print("Task lists:")
    for list in lists:
        print(f"{list['title']}: ({list['etag']})")
        tasks = get_tasks(list["id"])
        for task in tasks:
            print(f"  {task['title']}: ({task['id']})")



def get_task_service():
    """ Get a Google Tasks API service object """

    creds = get_tasks_api_credentials()
    service = build("tasks", "v1", credentials=creds)
    return service


def get_task_lists(page_size=default_max_list_size, filter: string = None):
    """ Get a list of task lists """
    # TODO Use filter parameter

    service = get_task_service()
    results = service.tasklists().list(maxResults=page_size).execute()
    items = results.get("items", [])

    if not items:
        print("No task lists found.")
        return
    
    return items


def get_tasks(task_list_id, page_size=default_max_list_size):
    """ Get a list of tasks in a task list """

    service = get_task_service()
    results = service.tasks().list(tasklist=task_list_id, maxResults=page_size).execute()
    items = results.get("items", [])

    if not items:
        print("No tasks found.")
        return
    
    return items


if __name__ == "__main__":
    main()
