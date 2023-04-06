import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения из БД")
        return []

    def addPost(self, title, comment):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO post VALUES(NULL, ?, ?, ?)", (title, comment, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД:" + ' ' + str(e))

            return False

        return True

    def getPost(self, post_id):
        try:
            self.__cur.execute(f"SELECT title, comment FROM post WHERE id = {post_id}")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД:" + ' ' + str(e))
        return False

    def getPostAnonce(self):
        try:
            self.__cur.execute("SELECT id, title, comment FROM post ORDER BY time ASC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД:" + ' ' + str(e))
        return ["Ваш список пуст", "Напишите свое первое дело!"]

    def updatePost(self, post_id, title, comment):
        try:
            self.__cur.execute(f"UPDATE post SET title = ?, comment = ?  WHERE id = {post_id}", (title, comment))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка обновления статьи в БД:" + ' ' + str(e))
            return False

        return True

    def deletePost(self, post_id):
        try:
            self.__cur.execute(f"DELETE FROM post WHERE id = {post_id}")
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка удаления статьи из БД:" + ' ' + str(e))