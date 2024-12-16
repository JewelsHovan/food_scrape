# food_cache.py
import json
from pathlib import Path

class FoodCache:
    def __init__(self, cache_dir="cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)

    def get_cached_data(self, food_id):
        """
        Attempts to retrieve cached food data for a given food_id.
        
        Args:
            food_id: The food ID to look up
            
        Returns:
            The cached data if it exists, None otherwise
        """
        cache_file = self.cache_dir / f"{food_id}.json"
        
        if cache_file.exists():
            print(f"Loading cached data for food ID: {food_id}")
            with open(cache_file, 'r') as f:
                return json.load(f)
        return None

    def save_to_cache(self, food_id, food_data):
        """
        Saves food data to the cache.
        
        Args:
            food_id: The food ID to save
            food_data: The food data to cache
        """
        cache_file = self.cache_dir / f"{food_id}.json"
        print(f"Saving data to cache: {cache_file}")
        
        with open(cache_file, 'w') as f:
            json.dump(food_data, f, indent=2)