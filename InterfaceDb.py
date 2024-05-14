import pyodbc 
import Pyro4
import os
import sqlite3

#Configure SQL Server Details
SQL_SERVER_NAME = "" #.../
SQL_SERVER_DB = "OUSTProject"

# Path to your SQL file and database file
SQL_FILE = 'OUSProject_database.sql'

#Set database interface Serving Details
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

            cursor = conn.cursor() #retunr cursor to scroll throguh data  
            cursor.execute(q, arg)
            return cursor#return cursor to scroll throguh data  
        except:
            return None

    #----- Exposed Methods that can be invoked

    def getScores(self, Student_ID):
        try:
            print("in Server2: Server1 -> interface to Database : Called getScores")
            scores = {}

            print("Attempting to Perform MSSQL Database lookup")
            #query database
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
        
    def getStudent(self,name,lastname,email):   
        try:
            print("in Server2: Server1 -> interface to Database : Called verifyStudent")
            scores = {}

            print("Attempting to Perform MSSQL Database lookup")
            #query database
            cursor = self.__sqlQuery('SELECT Student_ID FROM Student WHERE First_Name = ? AND Last_Name = ? AND Email = ? ', [name,lastname,email])

            student_id=cursor.fetchone()
            if student_id:
                print("from Server2: database interface -> Server 1 : Sending student id to server 1")
                return 1
            else:#student was not found
                return -1
        except:
            print("from Server2: database interface -> Server 1  : Sending Database Error")
            return None

def AcceptRMI():
    OUSTProjectdb=db()
    daemon=Pyro4.Daemon(port=SA1_PORT)                
    uri=daemon.register(OUSTProjectdb, "OUSTProject")


    print("-----------------------------")
    print(" Server2 - Interface ")
    print("-----------------------------")
    print() 
    print("Ready. Object uri =", uri)

    daemon.requestLoop()


if __name__ == '__main__':

    print("Insert the name of your MySQL Server ")
    print("example>> DESK")
    SQL_SERVER_NAME=input("Type it here>>: ")

    print()
    print("Loading database......")
    
    AcceptRMI()