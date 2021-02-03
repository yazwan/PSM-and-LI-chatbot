import mysql.connector

def DataUpdate(my_lastname,my_firstname,my_feedback): 
    mydb = mysql.connector.connect( 
        host="localhost",
        database="rasadatabase", 
        user="root",  
        passwd=""
    ) 

    mycursor = mydb.cursor() 
    sql='INSERT INTO feedback (LastName,FirstName,feedback) VALUES ("{0}","{1}", "{2}");'.format(my_lastname,my_firstname,my_feedback) 
    mycursor.execute(sql) 
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# if __name__ == "__main__":
#     DataUpdate("yazwan","saedon","your chatbot need im")