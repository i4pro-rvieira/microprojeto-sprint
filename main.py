#!/usr/bin/env python3
"""
Main application for Google Tasks integration and CSV export
"""
import argparse
import sys
import logging
from google_tasks import GoogleTasksClient
from csv_exporter import CSVExporter

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(description='Export Google Tasks to CSV')
    parser.add_argument(
        '--output', '-o',
        help='Output CSV filename (default: auto-generated with timestamp)',
        default=None
    )
    parser.add_argument(
        '--summary', '-s',
        action='store_true',
        help='Print tasks summary to console'
    )
    parser.add_argument(
        '--list-only',
        action='store_true',
        help='Only list available task lists without exporting'
    )
    
    args = parser.parse_args()
    
    # Initialize Google Tasks client
    client = GoogleTasksClient()
    
    print("🔑 Authenticating with Google Tasks...")
    if not client.authenticate():
        print("❌ Authentication failed. Please check your credentials.")
        sys.exit(1)
    
    print("✅ Authentication successful!")
    
    if args.list_only:
        # Just list available task lists
        task_lists = client.get_task_lists()
        if not task_lists:
            print("No task lists found.")
            return
        
        print(f"\nAvailable Task Lists ({len(task_lists)}):")
        print("-" * 40)
        for task_list in task_lists:
            print(f"📋 {task_list.get('title', 'Untitled')} (ID: {task_list['id']})")
        return
    
    # Fetch all tasks
    print("📋 Fetching tasks from Google Tasks...")
    tasks = client.get_all_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    print(f"✅ Found {len(tasks)} tasks")
    
    # Print summary if requested
    if args.summary:
        exporter = CSVExporter()
        exporter.print_tasks_summary(tasks)
    
    # Export to CSV
    print("💾 Exporting tasks to CSV...")
    exporter = CSVExporter()
    filename = exporter.export_tasks(tasks, args.output)
    print(f"✅ Tasks exported successfully to: {filename}")

if __name__ == '__main__':
    main()