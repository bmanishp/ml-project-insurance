from shutil import ExecError
from flask import Flask
from insurance.logger import logging
from insurance.exception import InsuranceException
import sys

app=Flask(__name__)

@app.route("/",methods=["POSt","GET"])
def index():
    try:
        raise Exception('custom error for testing purpose')
    except Exception as e:
        error=InsuranceException(e,sys)
        logging.info(error.error_message)
        logging.info("Testing Logging for the first time")
    return "Insurance Project"

if __name__ == "__main__":
    app.run(debug=True)
