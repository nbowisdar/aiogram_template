from loguru import logger

# Configure logger
logger.add("app.log", backtrace=True, diagnose=True)
