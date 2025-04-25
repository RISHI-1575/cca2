import pandas as pd

def load_crop_data(file_path):
    """Load crop data from CSV."""
    return pd.read_csv(file_path)

def load_user_data(file_path):
    """Load user data from CSV."""
    return pd.read_csv(file_path)

def load_company_posts(file_path):
    """Load company crop requirement posts from CSV."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Crop", "Quantity", "Contact", "Location"])