#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json

KEWER_ENDPOINT = 'http://kewer.catenae.dev/api/tasks'


def launch_task(script_content, class_name):
    url = KEWER_ENDPOINT
    data = {'class': class_name, 'code': script_content}
    response = requests.post(url, data=json.dumps(data))
    return response.json()


if __name__ == "__main__":
    script_name = sys.argv[1]
    class_name = sys.argv[2]

    with open(script_name, 'r') as script_file:
        script_content = script_file.read()

    result = launch_task(script_content, class_name)
    print(json.dumps(result, indent=4, ensure_ascii=False))