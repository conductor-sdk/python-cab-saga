from conductor.client.worker.worker_task import worker_task
from conductor.client.automator.task_handler import TaskHandler
from conductor.client.configuration.configuration import Configuration

@worker_task(task_definition_name='assign_driver')
def assign_driver(booking_id: str) -> object:
    return { 'driver_id': '7652' }

@worker_task(task_definition_name='cancel_driver_assignment')
def cancel_driver_assignment(booking_id: str) -> object:
    return { 'DRIVER_ASSIGNMENT_STATUS': 'CANCELLED' }

if __name__ == '__main__':
    api_config = Configuration()

    task_handler = TaskHandler(
        workers=[],
        configuration=api_config,
        scan_for_annotated_workers=True
    )
    task_handler.start_processes()
    task_handler.join_processes()