import argparse
import os
import sys


def get_args():
	parser = argparse.ArgumentParser()

	parser.add_argument('-in', '--input',
		dest='input',
		help='Input path')

	return parser.parse_args()

def predict( dataset_list, input_dir):
    
    #TODO: Substituir pelo codigo do pesquisador
    answers = []
    cont = 0

    for img in dataset_list: #read image
        # image = imread(os.path.join(input_dir, str(img)))

        prediction = 0.123456
        res = 0  # (0 para falso e 1 para positivo)
        
        exam = {
            "exam_id":dataset_list[cont],
            "answer": int(res), 
            "predict": float(prediction)
        }
        answers.append(exam)
        cont+=1

    return answers


if __name__ == '__main__':
    args = get_args()
    predict(args.input)
