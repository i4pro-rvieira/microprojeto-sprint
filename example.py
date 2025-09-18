#!/usr/bin/env python3
"""
Example script showing how to use Google Tasks CSV Exporter programmatically
"""
from google_tasks import GoogleTasksClient
from csv_exporter import CSVExporter

def example_usage():
    """Example of how to use the modules programmatically"""
    
    # Initialize the Google Tasks client
    client = GoogleTasksClient()
    
    # Authenticate with Google Tasks
    print("Authenticating with Google Tasks...")
    if not client.authenticate():
        print("Authentication failed!")
        return
    
    print("Authentication successful!")
    
    # Get all task lists
    print("\nFetching task lists...")
    task_lists = client.get_task_lists()
    print(f"Found {len(task_lists)} task lists:")
    for task_list in task_lists:
        print(f"  - {task_list.get('title', 'Untitled')}")
    
    # Get all tasks from all lists
    print("\nFetching all tasks...")
    all_tasks = client.get_all_tasks()
    print(f"Found {len(all_tasks)} total tasks")
    
    # Initialize CSV exporter
    exporter = CSVExporter()
    
    # Show tasks summary
    print("\n" + "="*50)
    print("TASKS SUMMARY")
    print("="*50)
    exporter.print_tasks_summary(all_tasks)
    
    # Export to CSV
    print("\nExporting to CSV...")
    filename = exporter.export_tasks(all_tasks, "my_tasks_example.csv")
    print(f"Tasks exported to: {filename}")
    
    # Example: Get tasks from specific list only
    if task_lists:
        first_list = task_lists[0]
        print(f"\nExample: Getting tasks only from '{first_list.get('title', 'Untitled')}'...")
        specific_tasks = client.get_tasks(first_list['id'])
        print(f"Found {len(specific_tasks)} tasks in this list")
        
        # Export specific list to separate CSV
        if specific_tasks:
            specific_filename = f"tasks_{first_list.get('title', 'list').replace(' ', '_')}.csv"
            exporter.export_tasks(specific_tasks, specific_filename)
            print(f"Specific list exported to: {specific_filename}")

if __name__ == '__main__':
    example_usage()