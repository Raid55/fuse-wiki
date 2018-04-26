import requests



def rmv_spaces(str):
    return str.replace(' ', '+')

def test_return(ret):
    """
        tests return and returns true or false
    """
    # test if status code is correct
    if ret.status_code != 200 or != 201:
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

    # test if status code is correct
    if ret.status_code != 200 or != 201:
        return None
    # test if json is correct
    try:
        rJson = ret.json()
    except:
        return None

    if rJson
    