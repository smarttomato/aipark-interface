import pymysql


class Mysql:
    def __init__(self, host, user, password, database, charset="utf8", port=3306):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
            )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def fetchone(self, sql):
        """
        单个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):
        """
        多个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self, sql):
        """
        执行
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except:
            print("fail")
            return False