from util import DBConnUtil as DB
class temp(DB.DBConnUtil):

    def createtable(self):
        self.open()
        createstr=f'''create table first(
        id int primary key,
        name varchar(50) not null,
        city varchar(40) not null
        );
        '''
        self.stmt.execute(createstr)
        self.conn.commit()
        self.close()
temp1=temp()
temp1.createtable()
