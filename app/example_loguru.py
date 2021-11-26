from loguru import logger

# set file.log
## simple log
# logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 KB", compression="zip")

## extended log
logger.add("debug.json",
           format="{time} {level} {message}",
           level="DEBUG",
           rotation="10:00",
           compression="zip",
           serialize=True)

#basic usages
logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")


def div(a, b):
    return a / b
#decorator from logger
@logger.catch()
def main():
    div(10, 0)

main()