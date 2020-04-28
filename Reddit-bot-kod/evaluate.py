import praw
import pandas as pd
import datetime as dt #only if you want to analyze the date created feature
import requests
import urllib.request
import time
import argparse
import json
import cv2
import numpy as np
from yolo.frontend import create_yolo
from yolo.backend.utils.box import draw_scaled_boxes
from yolo.backend.utils.annotation import parse_annotation
from yolo.backend.utils.eval.fscore import count_true_positives, calc_score
from pascal_voc_writer import Writer
from shutil import copyfile
import os
import yolo

DEFAULT_CONFIG_FILE = "dataSetKerras-master/config.json"
DEFAULT_WEIGHT_FILE = "model.h5"
DEFAULT_THRESHOLD = 0.3

argparser = argparse.ArgumentParser(
    description='Predict digits driver')

argparser.add_argument(
    '-c',
    '--conf',
    default='config.json',
    help='path to configuration file')

argparser.add_argument(
    '-t',
    '--threshold',
    default=DEFAULT_THRESHOLD,
    help='detection threshold')

argparser.add_argument(
    '-w',
    '--weights',
    default='model.h5',
    help='trained weight files')

argparser.add_argument(
    '-p',
    '--path',
    default='mapp',
    help='path to images')

# reddit account

reddit = praw.Reddit(user_agent='footballrecognizer',
                     client_id='_NosXdhPBALJKA', 
                     client_secret="eFh0UgpI-IwCGHIRb_1uNHYGWck",
                     username='footballrecognizer', 
                     password='qwerty12345')    

subreddit = reddit.subreddit('soccerbanners') # subreddit info

for submission in subreddit.stream.submissions():
    submissionURL = submission.url
    if "jpg" in submissionURL:
        postID = submission.id
        print(submissionURL)
        print(postID)
        urllib.request.urlretrieve(submissionURL, "mapp/test.jpeg")

        if __name__ == '__main__':
            # 1. extract arguments
            args = argparser.parse_args()
            with open(args.conf) as config_buffer:
                    config = json.loads(config_buffer.read())
            if config['train']['is_only_detect']:
                    labels = ['']
            else:
                    if config['model']['labels']:
                        labels = config['model']['labels']
                    else:
                        labels = get_object_labels(config['train']['train_annot_folder'])
            print(labels)

            # 2. create yolo instance & predict
            yolo = create_yolo(config['model']['architecture'],
                            labels,
                            config['model']['input_size'],
                            config['model']['anchors'])
            yolo.load_weights(args.weights)

            # 3. read image
            write_dname = "detected"
            if not os.path.exists(write_dname): os.makedirs(write_dname)

            for filename in os.listdir(args.path):
                img_path = os.path.join(args.path,filename)
                img_fname = filename
                image = cv2.imread(img_path)
                
                boxes, probs = yolo.predict(image, float(args.threshold))
                labels = np.argmax(probs, axis=1) if len(probs) > 0 else [] 

                # 4. save detection result
                image = draw_scaled_boxes(image, boxes, probs, labels)
                output_path = os.path.join(write_dname, os.path.split(img_fname)[-1])
                label_list = config['model']['labels']
                right_label = np.argmax(probs, axis=1) if len(probs) > 0 else [] 
                print("{}-boxes are detected. {} saved.".format(len(boxes), output_path))
                if len(probs) > 0:
                    cv2.imwrite(output_path, image)
                    probability = probs[0][0] * 100
                    submission.reply("The image contains a football with a certainty of " + probability + "%.") 
                    print("Kommenterat på reddit, etersom det finns en fotboll i bilden.")
                    print("Väntar nu 10 minuter för att kringgå reddits spamm filter.")
                    time.sleep(600)

os.remove("test.jpeg") # raderar bilden från datorn
print("Bild raderad.")

