from pathlib import Path
import os


def get_project_dir():
    return Path(__file__).parent.parent

def get_pid():
    return os.getpid()

def check_path(paths: list):
    for path in paths:
        if os.path.exists(path) is False:
            os.mkdir(path)

def target_url(domain, path):
    return f"{domain}/{path}"
