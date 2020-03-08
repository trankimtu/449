import requests
import datetime
# ===================================

# test get all Posts

# ===================================

def case_Get_All():
    
    resp = requests.get('http://127.0.0.1:5000/posts/all')
    
    if resp.status_code == 200:
        obj = resp.json()
        return True, obj
    else:
        print ('Test Get All Posts is FAILURE! or Data DOES NOT EXIST')
        return False, -1

# ===================================

# test get Post by ID

# ===================================

def case_Get_ID(PostID):
   

    URL = 'http://localhost:5000/posts/' + f'{PostID}'
    resp = requests.get(URL)
    
    if resp.status_code == 200:
        obj = resp.json()
        return True, obj
    else:
        print (F'Test Get Data at index {PostID} is FAILURE or Data DOES NOT EXIST')
        return False, -1
    print()

# ===================================

# test get Post by community

# ===================================


# def test_post_by_community(community, n):

#     print()
#     print('*'*50)
#     print(f'Test {n} recent posts by the {community}')
#     print('*'*50)
#     print()
    
#     # http://localhost:5000/posts/Community_3?n=3
#     URL = r"http://localhost:5000/posts/" + f'{community}?n={n}'

#     resp = requests.get(URL)
    
#     if resp.status_code == 200:

        
#         obj = resp.json()
#         length = len(obj)
#         print(f'The list has {length} Posts.\n')

#         print("Posts: \n")
#         for i in obj:
#             print(i)
#             print()

#         print (f'Test {n} recent posts by the {community} SUCCESS')
#         return True
#     else:
#         print (F'Test {n} recent posts by the {community} IS FAILURE or Data DOES NOT EXIST')
#         return False
#     print()


def test_post_by_community(community, n):
    
    # http://localhost:5000/posts/Community_3?n=3

    URL = r"http://localhost:5000/posts/" + f'{community}?n={n}'

    resp = requests.get(URL)
    
    if resp.status_code == 200:

        obj = resp.json()
        return True, obj

    else:
        print (F'Test {n} recent posts by the {community} IS FAILURE or Data DOES NOT EXIST')
        return False, -1

# ===================================

# test get n Posts by times

# ===================================

def test_n_post_by_time(n):

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
                
        obj = resp.json()
        length = len(obj)
        print(f'The list has {length} Posts.\n')

        print("Posts: \n")
        for i in obj:
            print(i)
            print()

        print (f'Test list of {n} recent posts SUCCESS!')
        return True
    else:
        print ('Test Get Data at index {PostID} FAILURE or Data DOES NOT EXIST')
        return False

    print()


# ===================================

# test Post

# ===================================

def case_Post(**arg):

    # http://localhost:5000/posts?n=10

    URL = 'http://localhost:5000/posts'
    # print('arg = ', arg)

    resp = requests.post(URL, data = arg)

    # print('resp = ', resp)
    # print('resp.text = ', resp.text)
    # print('resp.status_code = ', resp.status_code)
    if resp.status_code == 201:
        return True, resp.text

    else:
        return False, -1
   
# ===================================

# test Delete by ID

# ===================================

def case_Delete(DelID):

    # http://localhost:5000/posts?n=10

    URL = r'http://localhost:5000/posts/delete/' + f'{DelID}'

    resp = requests.delete(URL)

    # print('resp = ', resp)
    # print('resp.text = ', resp.text)
    # print('resp.status_code = ', resp.status_code)


    if resp.status_code == 204:
        return True

    else:
        return False



# case_Get_Al()
# case_Get_ID(5)
# test_post_by_community('Community_2', 2)
# test_n_post_by_time(4)
# case_Post()
# case_Delete(10)




def main():
    myDB = [
        {
            "PostID": 1,
            "Username": "User 1",
            "PostTitle": "Post Title 1",
            "PostDate": "2020-03-07 08:45:50",
            "Content": "Content 1",
            "Community": "Community_1",
            "URLResource": "www.URLResource1.com"
        },
        {
            "PostID": 2,
            "Username": "User 2",
            "PostTitle": "Post Title 2",
            "PostDate": "2020-03-07 08:45:50",
            "Content": "Content 2",
            "Community": "Community_1",
            "URLResource": "www.URLResource2.com"
        },
        {
            "PostID": 3,
            "Username": "User 3",
            "PostTitle": "Post Title 3",
            "PostDate": "2020-03-07 08:45:50",
            "Content": "Content 3",
            "Community": "Community_1",
            "URLResource": "www.URLResource3.com"
        },
        {
            "PostID": 4,
            "Username": "User 4",
            "PostTitle": "Post Title 4",
            "PostDate": "2020-03-07 08:45:50",
            "Content": "Content 4",
            "Community": "Community_2",
            "URLResource": "www.URLResource4.com"
        },
        {
            "PostID": 5,
            "Username": "User 5",
            "PostTitle": "Post Title 5",
            "PostDate": "2020-03-07 08:45:50",
            "Content": "Content 5",
            "Community": "Community_2",
            "URLResource": "www.URLResource5.com"
        },
        {
            "PostID": 6,
            "Username": "User 6",
            "PostTitle": "Post Title 6",
            "PostDate": "2020-03-07 08:45:50",
            "Content": "Content 6",
            "Community": "Community_2",
            "URLResource": "www.URLResource6.com"
        },
        {
            "PostID": 7,
            "Username": "User 7",
            "PostTitle": "Post Title 7",
            "PostDate": "2020-03-07 08:45:50",
            "Content": "Content 7",
            "Community": "Community_3",
            "URLResource": "www.URLResource7.com"
        },
        {
            "PostID": 8,
            "Username": "User 8",
            "PostTitle": "Post Title 8",
            "PostDate": "2020-03-07 08:45:50",
            "Content": "Content 8",
            "Community": "Community_3",
            "URLResource": "www.URLResource8.com"
        },
        {
            "PostID": 9,
            "Username": "User 9",
            "PostTitle": "Post Title 9",
            "PostDate": "2020-03-07 08:45:50",
            "Content": "Content 9",
            "Community": "Community_3",
            "URLResource": "www.URLResource9.com"
        }
    ]

    # ============================================
    # 1. TEST GET ALL POST 
    # ============================================

    print()
    print('*'*50)
    print('1. Test get all post'.upper())
    print('*'*50)
    print()


    # Process the correct result from database
    print('Correct result from database:\n')
    print(f'Length = {len(myDB)}\n')
    print('Post:\n')
    for i in myDB:
        print(f'{i}\n')

    print('-'*10 + '\n') # ------------------------

    # Process result from the website
    isPassed, AllPost = case_Get_All()

    print('Result from test case\n')
    print(f'Length of test case = {len(AllPost)}\n')
    print('Post:\n')
    for i in AllPost:
        print(f'{i}\n')

    print('-'*10 + '\n') # ------------------------
    print('Test Result: \n'.upper())

    if isPassed and AllPost == myDB:
        print ('Test Get All Posts SUCCESS!\n')
        
    else:
        print('Test Get All Posts is FAILURE!')

    # ============================================
    # 2. TEST GET POST AT PostID
    # ============================================

    DelID = 5

    print()
    print('*'*50)
    print(f'2. Test get Post at PostID = {DelID}')
    print('*'*50)
    print()

    # Process the correct result from database
    Answer = []

    for i in myDB:
        if i['PostID'] == DelID:
            Answer.append(i)

    print('Correct result from database:\n')
    print(f'Length = {len(Answer)}\n')
    print('Post:\n')
    print(f'{Answer}\n')

    print('-'*10 + '\n') # ------------------------


    # Process result from the website
    isPassed, postByID = case_Get_ID(DelID)

    if isPassed and (postByID in myDB):
        
        length = 1
        print('Result from test case\n')
        print(f'Length = {length}\n')
        print('Post:\n')
        print(f'{postByID}\n')

        print('-'*10 + '\n') # ------------------------
        print('Test Result:\n'.upper())
        print ('Test Get Posts by ID is SUCCESS!\n')
    else:
        print(f'Test Posts at PostID = {DelID} is FAILURE!')

    # ============================================
    # 3. TEST GET n RECENT POST BY THE COMMUNITY
    # ============================================

    myCommunity = 'Community_2'
    n = 2

    print()
    print('*'*50)
    print(f'3. Test get {n} recent posts by the {myCommunity}')
    print('*'*50)
    print()

    # Process the correct result from database

    result=[]
    i = 0

    while i < len(myDB) and len(result) < n:
        if myDB[i]['Community'] == myCommunity:
            result.append(myDB[i])
            i += 1
        else:
            i += 1
    
    print('Correct result from database:\n')
    print(f'Length = {len(result)}\n')
    print('Post:\n')
    for i in result:
        print(f'{i}\n')
    
    
    print('-'*10 + '\n') # ------------------------


    # Process result from the website

    isPassed, nPostByCommunity = test_post_by_community(myCommunity, n)

    print('Result from test case\n')
    print(f'Length = {len(nPostByCommunity)}\n')
    print('Post:\n')
    for i in nPostByCommunity:
        print(f'{i}\n')

    print('-'*10 + '\n') # ------------------------

    print('Test Result: \n'.upper())
    if isPassed and (nPostByCommunity == result):
        print (f'Test Get {n} Posts by community = {myCommunity} is SUCCESS!\n')
    else:
        print(f'Test Posts at PostID = {testID} is FAILURE!')


    # ============================================
    # 4. TEST GET n POST BY TIME
    # ============================================

    print()
    print('*'*50)
    print(f'4. Test get {n} posts by time')
    print('*'*50)
    print()

    # Process the correct result from database

    n = 4
    print('Correct result from database:\n')
    print(f'Length = {len(result)}\n')
    print('Post:\n')

    print('-'*10 + '\n') # ------------------------
    # Process result from the website



    print('Result from test case\n')
    print(f'Length = {len(nPostByCommunity)}\n')
    print('Post:\n')

    print('-'*10 + '\n') # ------------------------

    print('Test Result: \n'.upper())

    # test_n_post_by_time(4)


    # ============================================
    # 5. TEST POST 
    # ============================================
    myJSON = {
        "Username"      : "User 100",
        "PostTitle"     : "Post Title 100",
        "Content"       : "Content 100",
        "Community"     : "Community 100",
        "URLResource"   : "www.URLResource100.com"
    }   

    print()
    print('*'*50)
    print(f'5. Test post'.upper())
    print('*'*50)
    print()

    # ----------------------------------------------
    # Process the correct result from database
    myDB_Before_Post = myDB

    print('All posts from database BEFORE add the Post:\n')
    print(f'Length = {len(myDB_Before_Post)}\n')
    print('Post:\n')
    for i in myDB_Before_Post:
        print(f'{i}\n')

    print('-'*10 + '\n') # ------------------------

    # Process result from the website

    isPassed1, addJSON = case_Post(**myJSON)
    isPassed2, retrievedJson = test_post_by_community(myJSON['Community'], 2)
    tempBool, myDB_After_Post = case_Get_All()

    # print(myJSON['Community'])
    # print('isPassed1 = ', isPassed1)
    # print('isPassed2 = ', isPassed2)
    # print('retrievedJson = ', retrievedJson)

    print('Result from test case\n')
    print('All posts from database AFTER add the Post:\n')
    print(f'Length = {len(myDB_After_Post)}\n')
    print('Post:\n')

    for i in myDB_After_Post:
        print(f'{i}\n')

    # delta = len(myDB_After_Post)-len(myDB_Before_Post)
    # if isPassed and delta == 1:
    #     print("good")
    # case_Post(**myJson)

    print('-'*10 + '\n') # ------------------------
        
    print('Test Result: \n'.upper())

    if isPassed1 and isPassed2 == True:
        print ('Test Posts is SUCCESSFUL!\n')
    else:
        print(f'Test Posts is FAILURE!')


    # ============================================
    # 6. TEST DELETE 
    # ============================================

    DelID = 10

    print()
    print('*'*50)
    print(f'4. Test delete posts by PostID = {DelID}')
    print('*'*50)
    print()
    # ----------------------------------------------

    # Process the correct result from database
    myDB_Before_Del = myDB_After_Post

    print('All posts from database BEFORE delete the Post:\n')
    print(f'Length = {len(myDB_Before_Del)}\n')
    print('Post:\n')
    for i in myDB_Before_Del:
        print(f'{i}\n')

    print('-'*10 + '\n') # ------------------------

    # Process result from the website
    isPassed1 = case_Delete(DelID)
    isPassed2, retrievedJson = case_Get_ID(DelID)
    tempBool, myDB_After_Del = case_Get_All()

    # print('isPassed1 = ', isPassed1)
    # print('isPassed2 = ', isPassed2)

    print('Result from test case\n')
    print('All posts from database AFTER delete the Post:\n')
    print(f'Length = {len(myDB_After_Del)}\n')
    print('Post:\n')

    for i in myDB_After_Del:
        print(f'{i}\n')


    print('-'*10 + '\n') # ------------------------
        
    print('Test Result: \n'.upper())

    if isPassed1 == True and isPassed2 == False:
        print ('Test Delete is SUCCESSFUL!\n')
    else:
        print(f'Test Delete is FAILURE!')










    # case_Delete(10)
    # ============================================
    # ============================================





    # test_post_by_community('Community_2', 2)
    # test_n_post_by_time(4)
    # case_Post()
    # case_Delete(10)

main()



# >>> now = datetime.datetime.now()
# >>> today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
# >>> now < today8am
# True
# >>> now == today8am
# False
# >>> now > today8am
# False
















