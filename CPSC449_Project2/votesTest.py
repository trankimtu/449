import requests
import datetime

# ===================================
# test get all Votes
# ===================================
def case_Get_All():
    resp = requests.get('http://127.0.0.1:5000/api/v1/resources/votes/all')
    if resp.status_code == 200:
        obj = resp.json()
        return True, obj
    else:
        print ('Test Get_All is FAILURE! or Data DOES NOT EXIST')
        return False, -1

# ===================================
# test get Vote by ID, ex 1
# ===================================
def case_Get_Vote(id):  
    URL = 'http://127.0.0.1:5000/api/v1/resources/votebyid/' + f'{id}'
    resp = requests.get(URL)
    if resp.status_code == 200:
        obj = resp.json()
        return True, obj
    else:
        print (F'Test Get Vote at id: {id} is FAILURE or Data DOES NOT EXIST')
        return False, -1

# ===================================
# test get Vote by postID ex, 10, 11, 12
# ===================================
def case_Get_Vote_By_PostID(postID):
    URL = 'http://127.0.0.1:5000/api/v1/resources/votesbypostid/' + f'{postID}'
    resp = requests.get(URL)
    if resp.status_code == 200:
        obj = resp.json()
        return True, obj
    else:
        print (F'Test Get Vote by postID: {postID} is FAILURE or Data DOES NOT EXIST')
        return False, -1

# ===================================
# test get up_vote a post by postID, ex {"postID": 10}
# ===================================
def case_Get_Upvote_By_PostID(postID):
    URL = 'http://127.0.0.1:5000/api/v1/resources/upvote'
    # resp = requests.get(URL)
    postid =  {"postID": postID}
    resp = requests.post(URL, json = postid)
    if resp.status_code == 200:
        obj = resp.json()
        return True, obj
    else:
        return False, -1

# ===================================
# test get down_vote a post by postID, ex {"postID": 11}
# ===================================
def case_Get_Downvote_By_PostID(postID):
    URL = 'http://127.0.0.1:5000/api/v1/resources/downvote'
    # resp = requests.get(URL)
    postid =  {"postID": postID}
    resp = requests.post(URL, json = postid)
    if resp.status_code == 200:
        obj = resp.json()
        return True, obj
    else:
        return False, -1

# ===================================
# test get top-n post score, ex 3
# ===================================
def case_Get_Top_n_Post_Score(n):
    print(f'Top {n} post score')
    URL = 'http://127.0.0.1:5000/api/v1/resources/toppostscore/' + f'{n}'
    resp = requests.get(URL)
    if resp.status_code == 200:
        obj = resp.json()
        print(f'The list has {len(obj)} Posts.')
        print("Posts: ")
        for i in obj:
            print(i)
    
        print (f'Test list of {n} recent posts SUCCESS!')
        return True, obj
    else:
        print (F'Test Get {n} top post score is FAILURE or Data DOES NOT EXIST')
        return False, -1

# ===================================
# test List sorted by score, input list postID [10, 13, 14]
# ===================================
def case_List_Sorted_By_Score(listPostID):
    URL = 'http://127.0.0.1:5000/api/v1/resources/listsortedbyscore'
    listID = {"listID": listPostID}  
    resp = requests.post(URL, json = listID)
    if resp.status_code == 200:
        obj = resp.json()
        return True, obj
    else:
        return False, -1

def main():
    myDB = [
        {
            "voteID": 1,
            "postID": 10,
            "community": "funny",
            "upVoted": 1,
            "downVoted": 0
        },
        {
            "voteID": 2,
            "postID": 11,
            "community": "study",
            "upVoted": 0,
            "downVoted": 1
        },
        {
            "voteID": 3,
            "postID": 12,
            "community": "web back end",
            "upVoted": 0,
            "downVoted": 0
        },
        {
            "voteID": 4,
            "postID": 13,
            "community": "programming",
            "upVoted": 3,
            "downVoted": 0
        },
        {
            "voteID": 5,
            "postID": 14,
            "community": "programming",
            "upVoted": 0,
            "downVoted": 1
        }
    ]

    # ============================================
    # 1. TEST GET ALL POST 
    # ============================================
    print('*'*50)
    print('1. Test get all votes'.upper())
    print('*'*50)
    print('Correct result from raw database:')
    print(f'Length = {len(myDB)}')
    print('Post:')
    for i in myDB:
        print(f'{i}')

    # Process result from the website
    isPassed, allVotes = case_Get_All()

    print('\nResult from pugsql test case')
    print(f'Length of test case = {len(allVotes)}')
    print('Votes:')
    for i in allVotes:
        print(f'{i}')

    # print('-'*10 + '') # ------------------------
    if isPassed:
        print ('---> Test Get All Votes SUCCESS!')
        
    else:
        print('---> Test Get All Votes is FAILURE!')
    print()
    
    # ============================================
    # 2. TEST GET VOTE BY PostID
    # ============================================
    postID = 10
    print('*'*50)
    print(f'2. Test get Post at PostID = {postID}')
    print('*'*50)

    # Process the correct result from raw database
    Answer = []
    for i in myDB:
        if i['postID'] == postID:
            Answer.append(i)

    print('Result from raw database:')
    print(f'postID = {postID}')
    print(f'{Answer}')
    print('-'*10 + '') # ------------------------

    # Process result from the website
    isPassed, voteByPostID = case_Get_Vote_By_PostID(postID)
    if isPassed:        
        length = 1
        print('\nResult from pugsql test case')
        print(f'postID = {postID}')
        print(f'{voteByPostID}')
        print('-'*10 + '') # ------------------------
        print('Test Result:'.upper())
        print ('Test Get Vote by postID is SUCCESS!')
    else:
        print(f'Test Vote by postID = {postID} is FAILURE!')
    print()

    # ============================================
    # 3. TEST GET TOP n POST SCORE
    # ============================================
    n = 2
    print('*'*50)
    print(f'3. Test get top {n} post score')
    print('*'*50)

    # Process the correct result from raw database
    result=[]
    index=[]
    tempIndex=0
    largest=0
    i = 0
    while i < len(myDB) and len(result) < n:
        if(i not in index):
            temp = myDB[i]['upVoted'] - myDB[i]['downVoted']
            if (temp >= largest):
                largest = temp
                tempIndex = i
        if(i == len(myDB)):
            if(len(result) < n):
                result.append(myDB[i])
                index.append[i]
            i = -1
        i += 1
    
    print('Result from raw database:')
    print(f'Length = {len(result)}')
    print('Post:')
    for i in result:
        print(f'{i}') 
    print('-'*10 + '')

    # Process result from the website
    isPassed, nTopScore = case_Get_Top_n_Post_Score(n)
    print('\nResult from pugsql test case')
    print(f'Length = {len(nTopScore)}')
    print('Post:')
    for i in nTopScore:
        print(f'{i}')

    print('-'*10 + '') # ------------------------

    print('Test Result: '.upper())
    if isPassed:
        print (f'Test Get Top {n} post score is SUCCESS!')
    else:
        print(f'Test Get Top {n} post score is FAILURE!')
    print()

    # ============================================
    # 4. TEST UP VOTE A POST
    # ============================================
    print('Result from raw database:')
    postID = 13
    print('*'*50)
    print(f'4. Test Upvote a postID = {postID}')
    print('*'*50)
    for i in myDB:
        if i['postID'] == postID:
            i['upVoted'] += 1
            print('upVote updated:')
            print(f'{i}')
    print('-'*10 + '') # ------------------------

    # Process result from the website
    print('\nResult from pugsql test case')
    isPassed, upvoted = case_Get_Upvote_By_PostID(postID)
    if isPassed:
        print(f'upvote Updated: {upvoted}')
        print(f'Test upvote a post by postID {postID} is SUCCESS!')
        print('-'*10 + '') # ------------------------
    else:
        print(f'Test upvote a post by postID {postID} is FAILURE!')
    print()

    # ============================================
    # 5. TEST DOWN VOTE A POST BY POSTID
    # ============================================
   
    postID = 14
    print('*'*50)
    print(f'5. Test Downvote a postID = {postID}')
    print('*'*50)
    print('Result from raw database:')
    for i in myDB:
        if i['postID'] == postID:
            i['downVoted'] += 1
            print('downVote updated:')
            print(f'{i}')
    print()
    print('-'*10 + '') # ------------------------

    # Process result from the website
    print('\nResult from pugsql test case')
    isPassed, downvoted = case_Get_Downvote_By_PostID(postID)
    if isPassed:
        print(f'downVote Updated: {downvoted}')
        print(f'Test downvote a post by postID {postID} is SUCCESS!')
        print('-'*10 + '') # ------------------------
    else:
        print(f'Test downvote a post by postID {postID} is FAILURE!')
    print()

    # ============================================
    # 6. TEST GET LIST SORTED BY SCORE
    # ============================================
    listPostID = [10, 12, 14]
    print('*'*50)
    print(f'6. Test get list sorted by score = {listPostID}')
    print('*'*50)
    # print('Result from raw database:')
    # largest = 0
    # sortedList=[]
    # loop = 0
    # tempi =0
    # for j in listPostID:
    #     for i in myDB:       
    #         if i['postID'] == j and i['postID']:
    #             if i['upVoted'] - i['downVoted'] > largest:
    #                 largest = i['upVoted'] - i['downVoted']
    #                 tempi = i
    #                 sortedList.append(i)
    #             break
    # print('-'*10 + '') # ------------------------

    print('\nResult from pugsql test case')
    isPassed, listSorted = case_List_Sorted_By_Score(listPostID)
    if isPassed:
        print(f'Test get list sorted by {listPostID} is SUCCESS!')
        print('List sorted: ')
        for i in listSorted:
            print(i)
        print('-'*10 + '') # ------------------------
    else:
        print(f'Test get list sorted by {listPostID} is FAILURE!')

main()