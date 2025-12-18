import os, logging
logging.basicConfig(filename="Day6_logfile.log",level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s" )

logging.debug("Day 6 - Environment driven behavior")

env_var=os.environ.get("env")

logging.debug(f"Day 6 - Environment driven behavior: {env_var} is fetched")

if not env_var:
    logging.info("Environment driven behavior is empty, setting default to dev")
    os.environ.setdefault("env", "dev")
    logging.debug(f"Day 6 - Environment driven behavior is set to dev, {os.environ.get('env')} is fetched")

logging.info(f"Running in {os.environ.get('env')}  environment")