import requests



def rmv_spaces(str):
    return str.replace(' ', '+')

def test_return(ret):
    """
        tests return and returns true or false
    """
    # test if status code is correct
    # print(ret.status_code != 200)
    # print(ret.status_code != 201)
    if ret.status_code != 200 and ret.status_code != 201:
        # print("hete")
        return False
    # test if json is correct
    # print("2")
    try:
        rJson = ret.json()
    except:
        # print("4")
        return False
    # else return true
    # print('3')
    return True

def wiki_search_id(query):
    # base query link
    base_link = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=info&list=search&utf8=1&srsearch="
    # making requests
    ret = requests.get(base_link + rmv_spaces(query))
    print (base_link + rmv_spaces(query))
    # checking if returned correctly
    # print(type(ret.status_code))
    if test_return(ret) is False:
        return None
    # print("past")
    # listening to api suggestion if any
    rJson = ret.json()
    if 'suggestion' in rJson['query']['searchinfo']:
        ret = requests.get(base_link + rmv_spaces(rJson['query']['searchinfo']['suggestion']))
        if test_return(ret) is False:
            return None
        else:
            rJson = ret.json()
    
    return str(rJson['query']['search'][0]['pageid'])
    