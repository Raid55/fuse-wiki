#!/usr/bin/env python3
'''
    This Python module contains a method for the fuse-dot-wiki project.

    The method 'findTheWikiConnection' finds the articles that connect
        two given articles
'''


def findTheWikiConnection(source_id, target_id, database):
    '''
        This Python method contains an algorithm that will find 0, 1, or more
        paths of Wikipedia articles that link a source article and a
        target article.
    '''
    ##### ERROR CHECKING #####
    # Check if the id's given are valid Wikipedia articles
    # Check if the database connection can be established

    # Create an array of arrays called 'paths'.
    # (Each inner array will contain strings that
    # represent the 'page_title'(s) of each page in the path)

    ##### 0 DEGREES OF SEPARATION #####
    # Check if 'source' and 'target' are the same article

    ##### 1 DEGREE OF SEPARATION #####
    # If an outgoing link from 'source' is the 'target' or
    # if an incoming link from 'target' is the 'source'
    #     Append to an inner array, two strings of 'source_title' and
    #     'page_title'
    

    ##### 2 DEGREES OF SEPARATION #####
    # Create nodes of each outgoing link from the 'source page'
    # For each node created:
    #     if that node has an outgoing link that is the 'taget':
    #         append to 'paths' a path of: source--current_node--target
    # if 'paths' is non-empty:
    #     return 'paths'

    ##### 3 DEGREES OF SEPARATION #####
    # Create nodes of each incoming link to the 'target page'
    # For each node created:
    #     if that node has an incoming link that is any of the nodes that are:
    #     1-degree from 'source':
    #         append to 'paths' a path of 0src---1src---crrnt---0tgt
    # if 'paths' is non-empty:
    #     return 'paths'

    ##### 4 DEGREES OF SEPARATION #####
    # Creates nodes of each outgoing link from each '1src' node
    # For each node created:
    #     if that node has an outgoing link that is any of the 1tgt' nodes:
    #         append to 'paths' a path of 0src---1src---crrnt---1tgt---0tgt
    # if 'paths' is non-empty:
    #     return 'paths'

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
