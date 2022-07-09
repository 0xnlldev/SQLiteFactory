import sqlite3

class Factory:

    def connect(self, db_file_path):
        self.con = sqlite3.connect(f'{db_file_path}')
        self.cur = self.con.cursor()

    def save(self):
        self.con.commit()

    def close(self):
        try:
            self.cur.close()
            self.con.close()
        except:
            pass

    def tableCreate(self,table_name,tableContents):
        dbscript = f'CREATE TABLE IF NOT EXISTS {table_name} ('
        contents = ''
        tcount = len(tableContents)
        i = 1
        for content in tableContents:
            contents = contents + content
            if i < tcount:
                contents = contents + ','
            if i == tcount:
                contents = contents + ')'
                break
            i += 1

        dbscript = dbscript + contents
        self.cur.execute(dbscript)
        self.save()


    def addValues(self,table_name,values):
        dbscript = f'INSERT INTO {table_name} VALUES '
        contents = []
        i = 0
        contents.append('(')
        for content in values:
            if i < len(values):
                if i != 0:
                    contents.append("'")
                contents.append(content)
                if i != 0:
                    contents.append("'")
                if i != len(values)-1:
                    contents.append(',')
                i += 1
            elif i == len(values):
                if i != 0:
                    contents.append("'")
                contents.append(content)
                if i != 0:
                    contents.append("'")
                contents.append(')')
                i += 1
        contents.append(')')

        for content in contents:
            if type(content) == int or type(content) == float:
                dbscript += f'{content}'
            else:
                dbscript = dbscript + content

        self.cur.execute(dbscript)
        self.save()

    def getTable(self,table_name):
        table = self.cur.execute(f'SELECT * FROM {table_name}').fetchall()
        return table
                                            #                table_name     where
    def deleteData(self,table_name,where): # E.G: deleteValue('users', 'id = 3545')
        dbscript = f'DELETE FROM {table_name} WHERE {where}'
        self.cur.execute(dbscript)
        self.save()
