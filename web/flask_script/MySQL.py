import MySQLdb

class MySQL:
    def _open(self):
        self.conn = MySQLdb.connect(user='root', passwd='Bu7mA9si', host='db', db='tlabs', charset='utf8')
        self.cur = self.conn.cursor()

    def data_inserter(self, sql, data):
        self._open()
        try:
            self.cur.execute(sql, data)
        except MySQLdb.Error as e:
            print('[ERROR] MySQLdb.Error: ', e)
            return False
        self.conn.commit()
        self.conn.close()

        return True

    # injection対策済
    def data_getter(self, sql, data):
        self._open()
        self.cur.execute(sql, data)
        return self.cur.fetchall()
