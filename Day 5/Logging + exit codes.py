import sys, logging
file = None
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

try:
    filename = input("Please enter the file name:")
    file=open(filename, 'r')
    data=file.read()

except FileNotFoundError as exc:
    logging.exception(f"File not found: {exc}")
    sys.exit(1)
except NameError as exc:
    logging.exception(f"File not found: {exc}")
    sys.exit(1)
else:
    logging.info(f"File opened successfully, data : {data}")
    sys.exit(0)
finally:
    if file:
        file.close()
        logging.info(f"File closed successfully")