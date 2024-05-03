import pyodbc 
import Pyro4

#Configure SQL Server Details
SQL_SERVER_NAME = "DESK" #.../
SQL_SERVER_DB = "OUSTProject"

#Set Server2 Serving Details
SA1_PORT = 51515

@Pyro4.expose
class db(object):
    #Perform Database Lookup
    def __sqlQuery(self, q, arg):
        try:
            conn = pyodbc.connect('Driver={SQL Server};'#any version of SQLserver
                                'Server='+SQL_SERVER_NAME+';'
                                'Database='+SQL_SERVER_DB+';'
                                'Trusted_Connection=yes;')

            cursor = conn.cursor()
            cursor.execute(q, arg)
            return cursor
        except:
            return None

    #----- Exposed Methods that can be invoked

    def getScores(self, Student_ID):
        try:
            print("in Server2: Server1 -> interface to Database : Called getScores")
            scores = {}


            print("Attempting to Perform MSSQL Database lookup")

            cursor = self.__sqlQuery('SELECT Unit_Code, Score FROM Unit WHERE Student_ID = ? ', [Student_ID])
            for score in cursor:
                #add the grades to the list
                scores[score[0]] = score[1]
            if scores:
                print("from Server2: database interface -> Server 1 : Sending Grades to server 1")
                return scores
            else:#student was not found
                return -1
        except:
            print("from Server2: database interface -> Server 1  : Sending Database Error")
            return None

#Accept RMI
OUSTProjectdb=db()
daemon=Pyro4.Daemon(port=SA1_PORT)                
uri=daemon.register(OUSTProjectdb, "OUSTProject")


print("-----------------------------")
print(" Server2 - Interface ")
print("-----------------------------")
print() 
print("Ready. Object uri =", uri)

daemon.requestLoop()