import os

# Machine-specific absolute local filesystem paths
LOCAL_DATA_DIR = "C:\\Users\\Administrator\\AppData\\Local\\DataPipeline\\storage"
FALLBACK_LOG_PATH = "/home/developer/workspace/logs/pipeline.log"
DATABASE_PATH = "C:\\Projects\\Database\\records.sqlite"


def get_storage_path():
    return LOCAL_DATA_DIR
