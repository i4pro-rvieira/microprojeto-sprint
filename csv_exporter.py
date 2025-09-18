"""
CSV export functionality for Google Tasks
"""
import csv
import logging
from typing import List, Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)

class CSVExporter:
    """Handles exporting tasks to CSV format"""
    
    def __init__(self):
        self.default_fields = [
            'title',
            'notes',
            'status',
            'due',
            'completed',
            'updated',
            'taskListTitle',
            'id'
        ]
    
    def export_tasks(self, tasks: List[Dict[str, Any]], filename: str = None) -> str:
        """
        Export tasks to CSV file
        
        Args:
            tasks: List of task dictionaries
            filename: Output filename (optional, defaults to timestamp-based name)
            
        Returns:
            The filename of the created CSV file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"google_tasks_export_{timestamp}.csv"
        
        if not tasks:
            logger.warning("No tasks to export")
            # Create empty CSV file with headers
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.default_fields)
                writer.writeheader()
            return filename
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                # Get all unique field names from tasks
                all_fields = set()
                for task in tasks:
                    all_fields.update(task.keys())
                
                # Prioritize default fields, then add any additional fields
                fieldnames = []
                for field in self.default_fields:
                    if field in all_fields:
                        fieldnames.append(field)
                        all_fields.remove(field)
                
                # Add remaining fields
                fieldnames.extend(sorted(all_fields))
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                # Write tasks
                for task in tasks:
                    # Clean up the task data for CSV export
                    cleaned_task = self._clean_task_data(task)
                    writer.writerow(cleaned_task)
                
                logger.info(f"Successfully exported {len(tasks)} tasks to {filename}")
                return filename
                
        except Exception as e:
            logger.error(f"Error exporting tasks to CSV: {e}")
            raise
    
    def _clean_task_data(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Clean and format task data for CSV export
        
        Args:
            task: Raw task dictionary from Google Tasks API
            
        Returns:
            Cleaned task dictionary suitable for CSV export
        """
        cleaned = {}
        
        for key, value in task.items():
            if value is None:
                cleaned[key] = ''
            elif isinstance(value, dict):
                # Convert nested dictionaries to string representation
                cleaned[key] = str(value)
            elif isinstance(value, list):
                # Convert lists to comma-separated string
                cleaned[key] = ', '.join(str(item) for item in value)
            else:
                cleaned[key] = str(value)
        
        # Format specific fields for better readability
        if 'due' in cleaned and cleaned['due']:
            try:
                # Convert RFC3339 timestamp to readable format
                dt = datetime.fromisoformat(cleaned['due'].replace('Z', '+00:00'))
                cleaned['due'] = dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                pass  # Keep original value if parsing fails
        
        if 'completed' in cleaned and cleaned['completed']:
            try:
                dt = datetime.fromisoformat(cleaned['completed'].replace('Z', '+00:00'))
                cleaned['completed'] = dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                pass
        
        if 'updated' in cleaned and cleaned['updated']:
            try:
                dt = datetime.fromisoformat(cleaned['updated'].replace('Z', '+00:00'))
                cleaned['updated'] = dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                pass
        
        return cleaned
    
    def print_tasks_summary(self, tasks: List[Dict[str, Any]]) -> None:
        """
        Print a summary of tasks to console
        
        Args:
            tasks: List of task dictionaries
        """
        if not tasks:
            print("No tasks found.")
            return
        
        print(f"\nTasks Summary ({len(tasks)} total tasks):")
        print("-" * 60)
        
        # Group by task list
        task_lists = {}
        for task in tasks:
            list_title = task.get('taskListTitle', 'Unknown')
            if list_title not in task_lists:
                task_lists[list_title] = []
            task_lists[list_title].append(task)
        
        for list_title, list_tasks in task_lists.items():
            print(f"\n📋 {list_title} ({len(list_tasks)} tasks)")
            for task in list_tasks:
                status_icon = "✅" if task.get('status') == 'completed' else "⭕"
                title = task.get('title', 'Untitled')
                due_date = task.get('due', '')
                if due_date:
                    try:
                        dt = datetime.fromisoformat(due_date.replace('Z', '+00:00'))
                        due_str = f" (Due: {dt.strftime('%Y-%m-%d')})"
                    except:
                        due_str = f" (Due: {due_date})"
                else:
                    due_str = ""
                
                print(f"  {status_icon} {title}{due_str}")
        
        print(f"\n{'='*60}")
        print(f"Total: {len(tasks)} tasks across {len(task_lists)} lists")