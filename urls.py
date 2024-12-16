def get_autocomplete_url(search_term):
    """
    Generate the autocomplete API URL for a given search term.
    
    Args:
        search_term (str): The food term to search for
        
    Returns:
        str: The complete autocomplete URL
    """
    return f"https://api1.myfooddata.com/autocomplete/{search_term}"

def get_fooddata_url(food_id):
    """
    Generate the food data API URL for a given food ID.
    
    Args:
        food_id (str): The food ID to look up
        
    Returns:
        str: The complete food data URL
    """
    return f"https://api1.myfooddata.com/fooddata/{food_id}"

def get_nutrition_comparison_url(food_id):
    """
    Generate the nutrition comparison URL for a given food ID.
    
    Args:
        food_id (str): The food ID to compare
        
    Returns:
        str: The complete nutrition comparison URL
    """
    return f"https://api1.myfooddata.com/nutrition-comparison/{food_id}/100g/1"

def get_recipe_calculator_url(food_id):
    """
    Generate the recipe nutrition calculator URL for a given food ID.
    
    Args:
        food_id (str): The food ID for the recipe
        
    Returns:
        str: The complete recipe calculator URL
    """
    return f"https://api1.myfooddata.com/recipe-nutrition-calculator/{food_id}/100g/1"

def get_print_url(food_id):
    """
    Generate the nutrition label print URL for a given food ID.
    
    Args:
        food_id (str): The food ID for the nutrition label
        
    Returns:
        str: The complete print URL
    """
    return f"https://tools.myfooddata.com/print/{food_id}/100g/1"

# Base URLs that don't require parameters can be constants
FOODDATA_BASE_URL = "https://api1.myfooddata.com/fooddata/"

