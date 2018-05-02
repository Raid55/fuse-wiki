import os.path
import sqlite3
from helpers.b_dir_earch import bi_dir_earch


class Database:
    """
        DB connection
    """

    def __init__(self, DBArchive_path="./fuse.sqlite"):

        if not os.path.isfile(DBArchive_path):
            raise IOError('{} does not exist'.format(DBArchive_path))

        self.__connection = sqlite3.connect(DBArchive_path, check_same_thread=False)
        self.__curr = self.__connection.cursor()
        

    def find_outgoing(self, arr):
        """
            Takes an array of ids and returns all outgoing links
            for each elem
        """
        query = "SELECT id, outgoing_links FROM links WHERE id IN {}"
        # print(query)
        res = self.__curr.execute(query.format(str(tuple(arr)).replace(',)', ')')))
        return {str(row[0]): row[1].split("|") for row in res}
        

    def find_incoming(self, arr):
        """
            Takes an array of ids and returns all incoming links
            for each elem
        """
        query = "SELECT id, incoming_links FROM links WHERE id IN {}"
        # print(query)
        res = self.__curr.execute(query.format(str(tuple(arr)).replace(',)', ')')))
        return {str(row[0]): row[1].split("|") for row in res}


    def find_title(self, page_id):
        query = "SELECT title FROM pages WHERE id={}"
        print([row[0] for row in self.__curr.execute(query.format(page_id))][0])
        return [row[0] for row in self.__curr.execute(query.format(page_id))][0]

    def find_titles(self, arr):
        return [self.find_title(page_id) for page_id in arr]

    # //// bundled functions //////////////////////////////////////////

    def matrix_ids_to_titles(self, matrix):
        return [self.find_titles(row) for row in matrix]

    def findTheWikiConnection(self, source_id, target_id):
        resMatrix = bi_dir_earch(self, source_id, target_id)
        if (type(resMatrix) == str):
            return resMatrix
        
        return self.matrix_ids_to_titles(resMatrix)



    def close(self):
        self.__connection.close()
