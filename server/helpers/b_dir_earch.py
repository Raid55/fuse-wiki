'''
    This Python module contains a method for the fuse-dot-wiki project.
    The method 'findTheWikiConnection' finds the articles that connect
        two given articles
'''


def bi_dir_earch(db, source_id, target_id):
    '''
        This Python method contains an algorithm that will find 0, 1, or more
        paths of Wikipedia articles that link a source article and a
        target article. This is v2
    '''
    ##### ERROR CHECKING #####
    if source_id is None or target_id is None:
        return "Error: There was a non-existent source or target article"

    ##### DECLARE PERSISTENT OBJECTS #####
    source_tree = "SQLite call"
    target_tree = "SQLite call"
    source_depth = 0
    target_depth = 0

    ##### ZERO DEGREES OF SEPARATION #####
    if source_id == target_id:
        return [source_id, target_id]

    ##### ONE DEGREE OF SEPARATION #####
    
