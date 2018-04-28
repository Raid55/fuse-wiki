import os.path
import sqlite3
from helpers.b_dir_earch import findTheWikiConnection 


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
        res = self.__curr.execute(query.format(str(tuple(arr))))
        return {row[0]: row[1].split("|") for row in res}
        

    def find_incoming(self, arr):
        """
            Takes an array of ids and returns all incoming links
            for each elem
        """
        query = "SELECT id, incoming_links FROM links WHERE id IN {}"
        res = self.__curr.execute(query.format(str(tuple(arr))))
        return {row[0]: row[1].split("|") for row in res}

    

    def find_title(self, id):
        pass


    def find_titles(self, arr):
        cache = {}

    def test(self, source_id, target_id):
        return findTheWikiConnection(self, source_id, target_id)


    def close(self):
        self.__connection.close()
