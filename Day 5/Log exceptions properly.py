import logging
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
except NameError as exc:
    logging.exception(f"File not found: {exc}")

else:
    logging.info(f"File opened successfully, data : {data}")

finally:
    if file:
        file.close()
        logging.info(f"File closed successfully")