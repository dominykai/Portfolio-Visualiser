import os.path

BACKEND_ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
ASSETS_DIR = os.path.join(BACKEND_ROOT_DIR, "assets")

def get_file_from_assets(*args):
    """Return the absolute path of a file in the assets directory."""
    return os.path.join(ASSETS_DIR, *args)