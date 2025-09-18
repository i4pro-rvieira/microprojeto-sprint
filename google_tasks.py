"""
Google Tasks API integration module
"""
import os
import json
import logging
from typing import List, Dict, Any, Optional
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GoogleTasksClient:
    """Client for interacting with Google Tasks API"""
    
    def __init__(self):
        self.service = None
        self.credentials = None
        
    def authenticate(self) -> bool:
        """
        Authenticate with Google Tasks API
        Returns True if authentication successful, False otherwise
        """
        try:
            creds = None
            # Check if token file exists
            if os.path.exists(config.get_token_path()):
                creds = Credentials.from_authorized_user_file(
                    config.get_token_path(), config.get_scopes()
                )
            
            # If there are no (valid) credentials available, let the user log in
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    if not os.path.exists(config.get_credentials_path()):
                        logger.error(f"Credentials file not found: {config.get_credentials_path()}")
                        return False
                        
                    flow = InstalledAppFlow.from_client_secrets_file(
                        config.get_credentials_path(), config.get_scopes()
                    )
                    creds = flow.run_local_server(port=0)
                
                # Save the credentials for the next run
                with open(config.get_token_path(), 'w') as token:
                    token.write(creds.to_json())
            
            self.credentials = creds
            self.service = build('tasks', 'v1', credentials=creds)
            logger.info("Successfully authenticated with Google Tasks API")
            return True
            
        except Exception as e:
            logger.error(f"Authentication failed: {e}")
            return False
    
    def get_task_lists(self) -> List[Dict[str, Any]]:
        """
        Get all task lists from Google Tasks
        Returns list of task lists or empty list if error
        """
        if not self.service:
            logger.error("Not authenticated. Call authenticate() first.")
            return []
            
        try:
            results = self.service.tasklists().list().execute()
            task_lists = results.get('items', [])
            logger.info(f"Found {len(task_lists)} task lists")
            return task_lists
            
        except HttpError as e:
            logger.error(f"Error fetching task lists: {e}")
            return []
    
    def get_tasks(self, task_list_id: str) -> List[Dict[str, Any]]:
        """
        Get all tasks from a specific task list
        
        Args:
            task_list_id: ID of the task list
            
        Returns:
            List of tasks or empty list if error
        """
        if not self.service:
            logger.error("Not authenticated. Call authenticate() first.")
            return []
            
        try:
            results = self.service.tasks().list(tasklist=task_list_id).execute()
            tasks = results.get('items', [])
            logger.info(f"Found {len(tasks)} tasks in list {task_list_id}")
            return tasks
            
        except HttpError as e:
            logger.error(f"Error fetching tasks from list {task_list_id}: {e}")
            return []
    
    def get_all_tasks(self) -> List[Dict[str, Any]]:
        """
        Get all tasks from all task lists
        
        Returns:
            List of all tasks with task list information
        """
        all_tasks = []
        task_lists = self.get_task_lists()
        
        for task_list in task_lists:
            tasks = self.get_tasks(task_list['id'])
            for task in tasks:
                # Add task list information to each task
                task['taskListTitle'] = task_list.get('title', 'Unknown')
                task['taskListId'] = task_list['id']
                all_tasks.append(task)
        
        logger.info(f"Total tasks collected: {len(all_tasks)}")
        return all_tasks