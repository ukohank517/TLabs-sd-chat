import MySQLdb

class MySQL:
    def _open(self):
        self.conn = MySQLdb.connect(user='root', passwd='Bu7mA9si', host='db', db='tlabs', charset='utf8')
        self.cur = self.conn.cursor()


    # injection対策のため、全部データ取って、サーバーで検索条件を実施
    # とりあえずリクエスト数多くないので。。
    def data_getter(self, sql):
        self._open()
        self.cur.execute(sql)
        return self.cur.fetchall()
