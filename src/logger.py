from loguru import logger

# Configure logger
logger.add("logs.log", backtrace=True, diagnose=True)
