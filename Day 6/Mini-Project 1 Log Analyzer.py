import logging, subprocess, platform
import os
import sys

logging.basicConfig(filename="Day6_Log_Analyzer_logfile.log",level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s" )
logging.debug("Script Started")
log_file="log.txt"
line_count = 0
info_count = 0
error_count = 0

try:
    with open(log_file,"r") as file:
        for line in file:
            line_count += 1
            if "INFO" in line:
                info_count += 1
            elif "ERROR" in line:
                error_count += 1
        logging.info(f"INFO Total lines: {line_count}")
        logging.info(f"INFO Total lines without any ERROR: {info_count}")
        logging.info(f"ERROR Total lines: {error_count}")
except FileNotFoundError:
    logging.exception("File Not Found")
    sys.exit(1)

else:
    if error_count > 0:
        logging.error("Application unhealthy")
        sys.exit(1)
    else:
        logging.info("Application healthy")
        sys.exit(0)

