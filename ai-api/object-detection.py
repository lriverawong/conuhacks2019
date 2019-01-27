# written with Python 2.7

import argparse
import base64
# import picamera
import json
import glob
import os

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def findNewestFile():
    list_of_files = glob.glob('/home/hacker/*') # * means all
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file

def main():
    newest_file = findNewestFile
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
        print json.dumps(response, indent=4, sort_keys=True)	#Print it out and make it somewhat pretty.

if __name__ == '__main__':

    main()
