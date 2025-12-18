import logging
logging.basicConfig(filename="Day6_logfile.log",level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s" )
config = {
    "env": "prod",
    "enable_cleanup": True
}

logging.debug("Reading the given Dictionary for key 'enable cleanup'")

cleanup_flag= config["enable_cleanup"]

if cleanup_flag:
    logging.info("Cleanup enabled")
else:
    logging.info("Cleanup disabled")