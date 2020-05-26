import requests
import pytest

def test_object_name():
    objects = ['apple','bowtie','candle','door','envelope','fish', 'guitar','ice cream','lightning','moon','mountain','star','tent','toothbrush','wristwatch']
    response = requests.get('http://127.0.0.1:5000/api/object_name')
    assert response.text in objects

def test_object_name_with_param():
    payload = {'key1': 'value1', 'key2': 'value2'}
    objects = ['apple','bowtie','candle','door','envelope','fish', 'guitar','ice cream','lightning','moon','mountain','star','tent','toothbrush','wristwatch']
    response = requests.get('http://127.0.0.1:5000/api/object_name', params = payload)
    assert response.text in objects

def test_object_name_with_post():
    payload = {'key1': 'value1', 'key2': 'value2'}
    objects = ['apple','bowtie','candle','door','envelope','fish', 'guitar','ice cream','lightning','moon','mountain','star','tent','toothbrush','wristwatch']
    response = requests.post('http://127.0.0.1:5000/api/object_name', data = payload)
    assert response.status_code == 405

# store canvas success
# store canvas fail - array
# store canvas fail - image of different size
# mail drawing success
# mail drawing fail - email does not exist
# mail drawing fail - not an email
# store canvas another http method
