"""
Configuration module for Google Tasks integration
"""
import os
import json
from typing import Dict, Any

class Config:
    """Configuration manager for the application"""
    
    def __init__(self):
        self.credentials_file = os.getenv('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
        self.token_file = os.getenv('GOOGLE_TOKEN_FILE', 'token.json')
        self.scopes = ['https://www.googleapis.com/auth/tasks.readonly']
        
    def get_credentials_path(self) -> str:
        """Get the path to the Google credentials file"""
        return self.credentials_file
        
    def get_token_path(self) -> str:
        """Get the path to the token file"""
        return self.token_file
        
    def get_scopes(self) -> list:
        """Get the OAuth scopes required"""
        return self.scopes

# Global configuration instance
config = Config()