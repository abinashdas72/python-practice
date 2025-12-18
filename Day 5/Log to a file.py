import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logging.info("script started")
logging.error("sample error")
logging.info("script completed")
