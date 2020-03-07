import requests

# test get all data
def test_Get_All():
    
    print()
    print('*'*50)
    print('get all'.upper())
    print('*'*50)
    print()

    resp = requests.get('http://127.0.0.1:5000/posts/all')
    
    if resp.status_code == 200:

        print ('Test Get All Data SUCCESS!')
        obj = resp.json()
        length = len(obj)
        print(f'The list has {length} Posts.\n')

        print("Posts: \n")
        for i in obj:
            print(i)
            print()

    else:
        print ('Get All Data DOES NOT work!')
        # raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    # for todo_item in resp.json():
    #     print('{} {}'.format(todo_item['id'], todo_item['summary']))

    print()


test_Get_All()

# ===================================

def test_Get_ID(PostID):
    print()
    print('*'*50)
    print(f'get Post at PostID = {PostID}')
    print('*'*50)
    print()

    URL = 'http://localhost:5000/posts/' + f'{PostID}'
    resp = requests.get(URL)
    
    if resp.status_code == 200:

        print (f'Test Get Data at index = {PostID} SUCCESS!')
        
        obj = resp.json()
        print(f'The list has 1 item.\n')

        print("Posts: \n")
        print(obj)

        print()
        return True
    else:
        print ('Get Data at index {PostID} DOES NOT work! or Data DOES NOT EXIST')


test_Get_ID(5)

# ===================================
# http://localhost:5000/posts/Community_3?n=3
def test_post_by_community(community, n):

    print()
    print('*'*50)
    print(f'Test {n} recent posts by the {community}')
    # print('get Post at PostID = '.upper() + f'{PostID}')
    print('*'*50)
    print()

# List the n most recent posts to a particular community
    URL = r"http://localhost:5000/posts/" + f'{community}?n={n}'
    # print(URL)


    resp = requests.get(URL)
    
    if resp.status_code == 200:

        print (f'Test {n} recent posts by the {community} SUCCESS')
        
        obj = resp.json()
        length = len(obj)
        print(f'The list has {length} Posts.\n')

        print("Posts: \n")
        for i in obj:
            print(i)
            print()

        print()
        return True
    else:
        print ('Get Data at index {PostID} DOES NOT work! or Data DOES NOT EXIST')

test_post_by_community('Community_2', 2)

# ===================================

def test_n_recent_post(n):

    print()
    print('*'*50)
    print(f'List the most {n} recent posts')
    # print('get Post at PostID = '.upper() + f'{PostID}')
    print('*'*50)
    print()


    # http://localhost:5000/posts?n=10

    URL = 'http://localhost:5000/posts?n=' + f'{n}'
    # print(URL)
    resp = requests.get(URL)
    
    if resp.status_code == 200:
                
        print (f'Test list of {n} recent posts SUCCESS!')
        obj = resp.json()
        length = len(obj)
        print(f'The list has {length} Posts.\n')

        print("Posts: \n")
        for i in obj:
            print(i)
            print()

    else:
        print ('Get Data at index {PostID} DOES NOT work! or Data DOES NOT EXIST')


test_n_recent_post(4)








# # ===================================

# print()
# print('*'*50)
# print('Create a Post')
# print('*'*50)
# print()

# from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get('http://localhost:5000/posts?n=1')

# try:
#     element = driver.find_element_by_name('_content')
#     print('found element')
# except Exception as e:
#     print('exception found', format(e))













# print('First start, my data has 9 records as 9 Posts')

# print(r'''

# Please go to post and create a new Post with data below:

# {
#     "Username": "User 10",
#     "PostTitle": "Post Title 10",
#     "Content": "Content 10",
#     "Community": "Community_1",
#     "URLResource": "www.URLResource10.com",
#     "PostID": 10
# }

# '''
# )

# if test_Get_ID(10):
#     print('Test add Post success, cause new post is in database\n')
    

# print()
# print('*'*50)
# print('Delete a Post')
# print('*'*50)
# print()

# print(
# '''
# After create a post, we have total 10 posts in database
# Go to this URL
# http://localhost:5000/posts/delete/10
# click on "DELETE"
# Then check all record again by go to this URL
# http://localhost:5000/posts/all
# you will see the post which PostID = 10 is deleted
# OR 
# '''
# )