# Database connection and operations
import json
from typing import List, Optional

class Database:
    def __init__(self):
        self.items = {}
        self.users = {}
    
    def add_item(self, item_id: int, item_data: dict):
        """Add an item to the database"""
        self.items[item_id] = item_data
        return item_data
    
    def get_item(self, item_id: int):
        """Get an item by ID"""
        return self.items.get(item_id)
    
    def get_all_items(self):
        """Get all items"""
        return list(self.items.values())
    
    def update_item(self, item_id: int, item_data: dict):
        """Update an item"""
        if item_id in self.items:
            self.items[item_id].update(item_data)
            return self.items[item_id]
        return None
    
    def delete_item(self, item_id: int):
        """Delete an item"""
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False

# Initialize database instance
db = Database()
