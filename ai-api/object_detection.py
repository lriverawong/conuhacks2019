# written with Python 2.7

import argparse
import base64
# import picamera
import json
import glob
import os
import json
import sys

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
# from main_servo import *
from main_servo import classify_trash

# returns the filename of the most recently added file
def findNewestFile(image_path):
    images = image_path + "/*"
    list_of_files = glob.glob(images) # * means all
    latest_file = max(list_of_files, key=os.path.getctime)
    # print(latest_file)
    return str(latest_file)

# returns a list of all the items in a specific classification file
def readTextFile(path):
    text_file = open(path, "r")
    lines = text_file.read().split('\n')
    # print(lines)
    text_file.close()
    return lines

# returns the json_string of the API return statement, as a json dump (python string)
def getJson():
    newest_file = findNewestFile("/home/hacker/image-bank")
    # print(newest_file)
    """Run a label request on a single image"""

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open(newest_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 3
                }]
            }]
        })
        response = service_request.execute()
    # print(json.dumps(response, indent=4, sort_keys=True))	#Print it out and make it somewhat pretty.
    json_string = json.dumps(response)
    # convert the python dictionary above into a JSON string
    return json_string

# returns the individual word descriptions from the API
def readJson(json_data):
    # print(json_data)
    data = json.loads(json_data)
    # print(data["responses"][0]["labelAnnotations"][0]["description"])
    labels = data["responses"][0]["labelAnnotations"]
    # loop through the description and add into a list
    word_list = []
    for label in labels:
        split_label = label["description"].split() #split by any whitespace
        lowered_label = [x.lower() for x in split_label]
        for word in lowered_label:
            word_list.append(word.encode('ascii', 'ignore'))
    # print(word_list)
    return word_list

# returns the value corresponding to the corrrect bin
#   bluebin  --  0
#   greybin  --  1
#   greenbin --  2
#   garbage  --  3
def classification(descriptions):
    bluebin = readTextFile("/home/hacker/conuhacks2019/ai-api/bluebin")
    greybin = readTextFile("/home/hacker/conuhacks2019/ai-api/greybin")
    greenbin = readTextFile("/home/hacker/conuhacks2019/ai-api/greenbin")
    garbage = readTextFile("/home/hacker/conuhacks2019/ai-api/garbage")
    for word in descriptions:
        if (word in bluebin):
            print("This is a blue bin item!")
            f1 = open("/home/hacker/conuhacks2019/object-count/bluebin-count", "r+")
            count_var = f1.readlines()
            count_var = int(count_var[0])
            count_var += 1
            f1.close()
            f1 = open("/home/hacker/conuhacks2019/object-count/bluebin-count", "w")
            f1.write(int(count_var))
            f1.close()
            return 0
        elif (word in greybin):
            print("This is a grey bin item!")
            return 1
            f1 = open("/home/hacker/conuhacks2019/object-count/greybin-count", "r+")
            count_var = f1.readlines()
            count_var = int(count_var[0])
            count_var += 1
            f1.close()
            f1 = open("/home/hacker/conuhacks2019/object-count/greybin-count", "w")
            f1.write(int(count_var))
            f1.close()
        elif (word in greenbin):
            print("This is a green bin item!")
            return 2
            f1 = open("/home/hacker/conuhacks2019/object-count/greenbin-count", "r+")
            count_var = f1.readlines()
            count_var = int(count_var[0])
            count_var += 1
            f1.close()
            f1 = open("/home/hacker/conuhacks2019/object-count/greenbin-count", "w")
            f1.write(int(count_var))
            f1.close()
    # if for all items it didn't match a non-garbage, then the final thing returns garbage
    return 3
    print("Didn't match anything, therefore it is garbage.")
    f1 = open("/home/hacker/conuhacks2019/object-count/garbage-count", "r+")
    count_var = f1.readlines()
    count_var = int(count_var[0])
    count_var += 1
    f1.close()
    f1 = open("/home/hacker/conuhacks2019/object-count/garbage-count", "w")
    f1.write(int(count_var))
    f1.close()

def main():
    # get json data from latest photo addition
    json_data = getJson()
    # get the tokenized versions of the descriptions of object in the photo
    tokenized_descriptions = readJson(json_data)
    item_class = classification(tokenized_descriptions)
    # print(item_class)
    sys.path.append(os.path.abspath("/home/hacker/conuhacks2019/hardware"))
    classify_trash(item_class)
    
if __name__ == '__main__':

    main()
