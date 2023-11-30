from models.task_list import TaskList
from models.task_lists_result import TaskListsResult
from tasks_api_client import TasksApiClient


def main():
    client: TasksApiClient = TasksApiClient()
    lists: TaskListsResult = client.get_task_lists()
    print("Task lists:")
    for list in lists:
        print(f"{list['title']}: ({list['etag']})")
        tasks: TaskList = client.get_tasks(list["id"])
        for task in tasks:
            print(f"\t{task['title']}: ({task['id']})")

if __name__ == "__main__":
    main()
