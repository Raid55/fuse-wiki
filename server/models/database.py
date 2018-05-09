import os.path
import sqlite3
from helpers.b_dir_earch import bi_dir_earch
import json
from flask import current_app

class Database:
    """
        DB connection
    """

    def __init__(self, DBArchive_path="./fuse-db.sqlite", DBSearch_path="./fuse-searches.sqlite"):

        if not os.path.isfile(DBArchive_path):
            raise IOError('{} does not exist'.format(DBArchive_path))

        self.__db_connection = sqlite3.connect(DBArchive_path, check_same_thread=False)
        self.__db_curr = self.__db_connection.cursor()
        self.__srch_connection = sqlite3.connect(DBSearch_path, check_same_thread=False)
        self.__srch_curr = self.__srch_connection.cursor()
        

    def arr_to_qStr(self, arr):
        """ array to querry ready in statment string """
        return str(tuple(arr)).replace(',)', ')').replace('u', '')

    def find_outgoing(self, arr):
        """
            Takes an array of ids and returns all outgoing links
            for each elem
        """
        query = "SELECT id, outgoing_links FROM links WHERE id IN {}"
        # print(query.format(self.arr_to_str(arr)))
        res = self.__db_curr.execute(query.format(self.arr_to_qStr(arr)))
        return {str(row[0]): row[1].split("|") for row in res}
        

    def find_incoming(self, arr):
        """
            Takes an array of ids and returns all incoming links
            for each elem
        """
        query = "SELECT id, incoming_links FROM links WHERE id IN {}"
        # print(query.format(self.arr_to_str(arr)))
        res = self.__db_curr.execute(query.format(self.arr_to_qStr(arr)))
        return {str(row[0]): row[1].split("|") for row in res}


    def find_title(self, page_id):
        query = "SELECT title FROM pages WHERE id={}"
        return [row[0] for row in self.__db_curr.execute(query.format(page_id))][0]

    def find_titles(self, arr):
        return [self.find_title(page_id) for page_id in arr]

    def find_cached_searches(self, source_id, target_id):
        query = "SELECT search FROM searches WHERE source_id={} AND target_id={}"
        try:
            return json.loads([row[0] for row in self.__srch_curr.execute(query.format(source_id, target_id))][0])
        except:
            return None
    
    def save_search(self, source_id, target_id, resArr):
        query = "INSERT INTO searches VALUES (?, ?, ?)"
        try:
            self.__srch_curr.execute(query, (source_id, target_id, json.dumps(resArr)))
        except Exception as e:
            current_app.logger.error(e)
            return False
        self.__srch_connection.commit()
        return True

    # //// bundled functions //////////////////////////////////////////

    def matrix_ids_to_titles(self, matrix):
        return [self.find_titles(row) for row in matrix]

    def findTheWikiConnection(self, source_id, target_id):
        resMatrix = bi_dir_earch(self, source_id, target_id)
        if (type(resMatrix) == str):
            return resMatrix
        
        return self.matrix_ids_to_titles(resMatrix)


