from config import default_max_list_size
from google_api_helpers import get_task_service
from models.task_list import TaskList
from models.task_lists_result import TaskListsResult, TaskListsResultSchema


class TasksApiClient:
    """ A client for the Google Tasks API. """
 
    def get_task_lists(self, page_size: int=default_max_list_size, filter: str = None) -> TaskListsResult:
        """ Retrieves a list of task lists from the Google Tasks API.

        Args:
            page_size (int): The maximum number of task lists to retrieve. Defaults to default_max_list_size.
            filter (str): A filter to apply to the task list titles. Defaults to None.

        Returns:
            list: A list of task lists retrieved from the Google Tasks API.
        """

        # TODO Use filter parameter

        service = get_task_service()
        api_results = service.tasklists().list(maxResults=page_size).execute()
        items = api_results.get("items", [])
        result = TaskListsResultSchema().load(api_results)

        if len(result.items) == 0:
            print("No task lists found.")
            return
        
        return items
    
    def get_tasks(self, task_list_id, page_size=default_max_list_size) -> TaskList:
        """ Get a list of tasks in a task list """

        service = get_task_service()
        results = service.tasks().list(tasklist=task_list_id, maxResults=page_size).execute()
        items = results.get("items", [])

        if not items:
            print("No tasks found.")
            return
        
        return items    