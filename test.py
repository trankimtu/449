import requests

# test get all data
def test_Get_All():


    resp = requests.get('http://127.0.0.1:5000/posts/all')
    print(resp.status_code)
    if resp.status_code == 200:

        print ('Get All Data works well!')
        obj = resp.json()
        length = len(obj)
        print(obj)
        print(f'The list has {length} items.')
    else:
        print ('Get All Data DOES NOT works well!')

        # raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    # for todo_item in resp.json():
    #     print('{} {}'.format(todo_item['id'], todo_item['summary']))

test_Get_All()