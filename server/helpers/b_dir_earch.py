'''
    This Python module contains a method for the fuse-dot-wiki project.
    The method 'findTheWikiConnection' finds the articles that connect
        two given articles
'''


def findTheWikiConnection(db, source_id, target_id):
    '''
        This Python method contains an algorithm that will find 0, 1, or more
        paths of Wikipedia articles that link a source article and a
        target article.
    '''
    ####### ERROR CHECKING #######
    # Check if the id's given are valid Wikipedia articles
    # Check if the database connection can be established


    if source_id is None or target_id is None:
        return [] 

    ####### SETUP #######
    paths = []

    ####### 0 DEGREES OF SEPARATION #######
    if source_id == target_id:
        return "They're the same article!"

    ####### 1 DEGREE OF SEPARATION #######
    source_1 = db.find_outgoing([source_id])
    if target_id in source_1[source_id]:
        paths.append([source_id, target_id])
        return paths

    ####### 2 DEGREES OF SEPARATION #######
    target_1 = db.find_incoming([target_id])
    for article in source_1[source_id]:
        if article in target_1[target_id]:
            paths.append([source_id, article, target_id])
    if paths is not None:
        return paths

    ##### 3 DEGREES OF SEPARATION #####
    source_2 = db.find_outgoing(source_1)
    for k, v in source_2.item():
        for article in v:
            if article in target_1[target_id]:
                paths.append(source_id, k, article, target_id)
    if paths is not None:
        return paths


    ##### 4 DEGREES OF SEPARATION #####
    # Creates nodes of each outgoing link from each '1src' node
    # For each node created:
    #     if that node has an outgoing link that is any of the 1tgt' nodes:
    #         append to 'paths' a path of 0src---1src---crrnt---1tgt---0tgt
    # if 'paths' is non-empty:
    #     return 'paths'
#
 #   target_2 = []
  #  for article in target_1:
   #     target_2.append('ORM call that returns incoming links from each element in target_1')
#    for i in range(len(target_2)):
 #       for article in target_2[i]:
  #          for j in


    ##### 5 DEGREES OF SEPARATION #####
    # Create nodes of each incoming link to each '1tgt' node
    # For each node created:
    #     if that node has an incoming link that is any of the '2src' nodes:
    #         append to 'paths' a path of 0src---1src---2src---cnt---1tgt---0tgt
    # if 'paths' is non-empty:
    #     return 'paths'

    ##### 6 DEGREES OF SEPARATION #####
    # Creates nodes of each outgoing link from each '2src' node
    # For each node created:
    #     if that node has an outgoing link that is any of the '2tgt' nodes:
    #         append to 'paths' a path of 0sc--1sc--2sc--crrnt--2tg--1tg--0tg
    # if 'paths' is non-empty:
    #     return 'paths'
    # else:
    #     return 'path not found'
