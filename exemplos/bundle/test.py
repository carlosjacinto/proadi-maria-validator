import os
import json
import sys
from datetime import datetime
from sys import argv, path
from predict import predict

start_time = datetime.now()
output_dir = "./output" # path for debug
input_dir = "./input" # path for debug
ID_SUBMISSION = "12345678"

def output_file(data):
    end_time = datetime.now()
    time = end_time - start_time
    time_format = {"overall_time_spent": time.seconds}

    data.update(time_format)

    return data

def input_read(input_dir):
    dataset = []

    filename=f"""{input_dir}/dataset_list.data"""

    with open(filename,'r') as file: 
        for exam in file:
            dataset.append(exam.strip())

    return dataset

def main():
    print("######START######", file=sys.stdout)
    output ={}
    message = {}
    try:
        print("Using input_dir: " + input_dir, file=sys.stderr)

        output = input_read(input_dir)
        
        output = predict(output , input_dir)

        message = {
            "id_submission": ID_SUBMISSION,
            "output_model": output
        }

        output = output_file(message)

        print("######OUTPUT######", file=sys.stdout)
        print(output, file=sys.stdout)

    except Exception as e:
        print('### ERROR - {} ###'.format(e), file=sys.stderr)
        message = {
            "body" : output,
            "error": {e}
        }
        print(message, file=sys.stderr)
  
if __name__ == "__main__":
    main()
