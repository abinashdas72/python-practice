import logging, subprocess, platform
import os
import sys

logging.basicConfig(filename="Day6_logfile.log",level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s" )
logging.info("Script Started")

env_var=os.environ
logging.info(f"env variable is fetched to be: {env_var}")

if platform.system() == "Windows":
    logging.debug("its Windows System")
    result=subprocess.run("hostname",shell=True,capture_output=True, text=True)
    logging.info(result.stdout)
else:
    logging.debug("its Linux System")
    result=subprocess.run("hostname",shell=True,capture_output=True, text=True)
    logging.info(result.stdout)

if result.returncode == 0:
    logging.info("Success")
    sys.exit(0)
else:
    logging.error("error")
    sys.exit(1)