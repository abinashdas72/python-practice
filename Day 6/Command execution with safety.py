import logging, subprocess, platform
logging.basicConfig(filename="Day6_logfile.log",level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s" )

if platform.system() == "Windows":
    logging.debug("its Windows System")
    result=subprocess.run("dir",shell=True,capture_output=True, text=True)
    logging.info(result.stdout)
else:
    logging.debug("its Linux System")
    result=subprocess.run("df" "-h",shell=True,capture_output=True, text=True)
    logging.info(result.stdout)

if result.returncode == 0:
    logging.info("Success")
else:
    logging.error("error")