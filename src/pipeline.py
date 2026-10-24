from config.settings import get_storage_path


def run_pipeline():
    storage = get_storage_path()
    print(f"Reading records from local storage: {storage}")
    return True
