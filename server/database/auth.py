import pyodbc


SERVER = 'LAPTOP-A84E5O9M\SQLEXPRESS'
DATABASE = 'chat_database'
DRIVER = 'SQL Server Native Client 11.0'
conn = pyodbc.connect('Driver={'+DRIVER+'};Server='+SERVER+';Database='+DATABASE+';Trusted_Connection=yes;')


cursor = conn.cursor()
def login(username,password):
    cursor.execute("select username from chat_database.dbo.chat_User WHERE username = '"+username+"' and password ='"+password+"'")
    row = cursor.fetchall()
    if(row[0].username==username):
        return True
    return False

def register(username,password,mobilephone,email):
    cursor.execute("select username from chat_database.dbo.chat_User WHERE username = '"+username+"'")
    row = cursor.fetchall()
    if(row==0):
        return False
    cursor.execute("insert into chat_database.dbo.chat_User(username, password, mobilePhone,email) VALUES ('"+str(username)+"','"+str(password)+"','"+str(mobilephone)+"','"+str(email)+"')")
    cursor.commit()
    return True