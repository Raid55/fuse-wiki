import requests



def rmv_spaces(str):
    return str.replace(' ', '+')

def test_return(ret):
    """
        tests return and returns true or false
    """
    # test if status code is correct
    if ret.status_code != 200 or ret.status_code != 201:
        return False
    # test if json is correct
    try:
        rJson = ret.json()
    except:
        return False
    # else return true
    return True

def wiki_search_id(query):
    # base query link
    base_link = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=info&list=search&utf8=1&srsearch="
    # making requests
    ret = requests.get(base_link + rmv_spaces(query))
    # checking if returned correctly
    if test_return(ret) is False:
        return None
    # listening to api suggestion if any
    rJson = ret.json()
    if 'suggestion' in rJson['query']['searchinfo']:
        ret = requests.get(base_link + rmv_spaces(rJson['query']['searchinfo']['suggestion']))
        if test_return(ret) is False:
            return None
        else:
            rJson = ret.json()
    
    return rJson['query']['search'][0]['pageid']
    