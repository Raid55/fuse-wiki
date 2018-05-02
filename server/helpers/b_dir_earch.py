'''
    This Python module contains a method for the fuse-dot-wiki project.
    The method 'findTheWikiConnection' finds the articles that connect
        two given articles
'''
from time import time

def findMatches(array_1, array_2):
    return set(array_1).intersection(array_2)


def bi_dir_earch(db, source_id, target_id):
    '''
        This Python method contains an algorithm that will find 0, 1, or more
        paths of Wikipedia articles that link a source article and a
        target article. This is v2
    '''
    ##### ERROR CHECKING #####
    if source_id is None or target_id is None:
        return "Error: There was a non-existent source or target article"

    ##### ZERO DEGREES OF SEPARATION #####
    if source_id == target_id:
        return [source_id, target_id]

    ##### DECLARE PERSISTENT OBJECTS #####
    paths = []
    source_id = str(source_id)
    target_id = str(target_id)
    source_tree = {}
    target_tree = {}
    source_depth = 0
    target_depth = 0


    while len(paths) == 0 and (source_depth < 3 or target_depth < 3):
        if source_depth == target_depth:
            source_depth += 1

            if source_depth == 1:
                source_tree = db.find_outgoing([source_id])
                if target_id in source_tree[source_id]:
                    paths.append([source_id, target_id])

            if source_depth == 2:
                start = time()
                source_tree[source_id] = db.find_outgoing(source_tree[source_id])
                for src1, src2_arr in source_tree[source_id].items():                    
                    for match in findMatches(src2_arr, target_tree[target_id]):
                        paths.append([source_id, src1, match, target_id])
#                    for src2 in src2_arr:
 #                       if src2 in target_tree[target_id]:
  #                          paths.append([source_id, src1, src2, target_id])
                print("3rd: ", time() - start)
                
            if source_depth == 3:
                start = time()
                for key, value in source_tree[source_id].items():
                    source_tree[source_id][key] = db.find_outgoing(value)
                for src1, src2_dict in source_tree[source_id].items():
                    for src2, src3_arr in src2_dict.items():
                        for tgt1, tgt2_arr in target_tree[target_id].items():
                            for match in findMatches(src3_arr, tgt2_arr):
                                paths.append([source_id, src1, src2, match, tgt1, target_id])
                print("5th: ", time() - start)
                
        else:
            target_depth += 1

            if target_depth == 1:
                start = time()
                target_tree = db.find_incoming([target_id])
                for article in source_tree[source_id]:
                    if article in target_tree[target_id]:
                        paths.append([source_id, article, target_id])
                print("2th: ", time() - start)

            if target_depth == 2:
                start = time()
                target_tree[target_id] = db.find_incoming(target_tree[target_id])
                for tgt1, tgt2_arr in target_tree[target_id].items():
                    for src1, src2_arr in source_tree[source_id].items():
                        for match in findMatches(src2_arr, tgt2_arr):
                            paths.append([source_id, src1, match, tgt1, target_id])
                print("4th: ", time() - start)

            if target_depth == 3:
                start = time()
                for key, value in target_tree[target_id].items():
                    target_tree[target_id][key] = db.find_incoming(value)
                for tgt1, tgt2_dict in target_tree[target_id].items():
                    for tgt2, tgt3_arr in tgt2_dict.items():
                        for src1, src2_dict in source_tree[source_id].items():
                            for src2, src3_arr in src2_dict.items():
                                for match in findMatches(src3_arr, tgt3_arr):
                                    paths.append([source_id, src1, src2, match, tgt2, tgt1, target_id])
                print("6th: ", time() - start)

    return paths


