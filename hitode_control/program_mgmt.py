from unittest import result
from db_model.mysql import conn_mysqldb
from hitode_control.user_mgmt import User

class Program():
    
    def __init__(self, program_user_id, program_no, program_content):
        self.program_user_id = User.id
        self.program_no = program_no
        self.program_content = program_content

    @staticmethod
    def find_id(program_no):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT program_user_id FROM program_info WHERE PROGRAM_NO = '" + str(program_no) + "'"
        # print (sql)
        db_cursor.execute(sql)
        result = db_cursor.fetchone()
        result = int(result[0])
        if not result:
            return None
        return result

    @staticmethod
    def create(program_user_id, program_content):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "INSERT INTO program_info (PROGRAM_USER_ID, PROGRAM_CONTENT) VALUES ('%s', '%s')" % (str(program_user_id), str(program_content))
        created = db_cursor.execute(sql)
        mysql_db.commit()
        return created
    
    @staticmethod
    def delete(program_no):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "DELETE FROM program_info WHERE PROGRAM_NO = '" + str(program_no) + "'"
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted
    
    @staticmethod
    def update(program_no, program_content):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "UPDATE PROGRAM_INFO SET PROGRAM_CONTENT = '" + str(program_content) + "' WHERE PROGRAM_NO = '" + str(program_no) + "'"
        updated = db_cursor.execute(sql)
        mysql_db.commit()
        return updated
    
    @staticmethod
    def find_one(program_no):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM PROGRAM_INFO WHERE PROGRAM_NO = %s" % str(program_no)
        db_cursor.execute(sql)
        result = db_cursor.fetchone()
        result = result[0]
        if not result:
            return None
        return result
    
    @staticmethod
    def find_all():
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM PROGRAM_INFO"
        db_cursor.execute(sql)
        programs = db_cursor.fetchall()
        if not programs:
            return None
        return programs