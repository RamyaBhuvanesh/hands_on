#logging_levels:
#1.debug
#2.info
#3.warning
#4.error
#5.critical

import logging
#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(Level=logging.ERROR) # defined a logger with level as error
#logging.warning("WARNING")
#logging.info("INFO") # has not printed
#logging.error("ERROR")
#logging.debug("DEBUG") # has not printed
#logging.critical("CRITICAL")
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(name)s : %(message)s',
                            datefmt='%a %m/%d/%y %I:%M:%A %p',
                            filename="ex1.log",
                            filemode="w",
                            level=logging.INFO)
logging.warning("WARNING")
logging.info("INFO") # has not printed
logging.error("ERROR")
logging.debug("DEBUG") # has not printed
logging.critical("CRITICAL")