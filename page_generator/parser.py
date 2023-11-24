import re
import json

def clear_raw_data(data_json):
    del data_json['csrfmiddlewaretoken']
    del data_json['requestType']
    return data_json


def check_request_type(request):
    if 'POST' in request:
        request_type = 'POST'
    elif 'GET' in request:
        request_type = 'GET'
    elif 'PUT' in request:
        request_type = 'PUT'
    else:
        request_type = 'DELETE'
    return request_type

def create_new_json(matches, data_json):
    result = {}

    counter = 0
    for i in range(0, len(matches), 5):
        group = matches[i:i + 5]
        name = data_json[group[0]]
        endpoint = data_json[group[1]]
        request = data_json[group[2]]
        body = data_json[group[3]]
        answer = data_json[group[4]]
        result[counter] = {
            'request_type': check_request_type(group[0]),
            'request': request,
            'body': body,
            'answer': answer,
            'name': name,
            'endpoint': endpoint
        }
        counter += 1
    return result


def regular_data(data_json):
    data = str(data_json)

    pattern = r"(request\d+\-(?:POST|GET|PUT|DELETE)|body\d+\-(?:POST|GET|PUT|DELETE)|answer\d+\-(?:POST|GET|PUT|DELETE)|name\d+\-(?:POST|GET|PUT|DELETE)|endpoint\d+\-(?:POST|GET|PUT|DELETE))"
    matches = re.findall(pattern, data)

    return matches



def pars_raw_data(data_json):
    data = clear_raw_data(data_json)
    matches = regular_data(data)
    data = create_new_json(matches, data)
    return data