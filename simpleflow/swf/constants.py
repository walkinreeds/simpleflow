import os

MAX_DECISIONS = 100
MAX_OPEN_ACTIVITY_COUNT = int(os.getenv("SWF_MAX_OPEN_ACTIVITY_COUNT", 1000))
TRACEBACK_SIZE = 5
