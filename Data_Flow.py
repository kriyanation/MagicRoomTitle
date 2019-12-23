import sqlite3
import random

def get_Title():
    connection = sqlite3.connect("/home/ram/MagicRoom.db")
    cur = connection.cursor()
    sql = "select Lesson_Title from Magic_Science_Lessons where Lesson_ID = ?"
    cur.execute(sql, (4, ))
    text = cur.fetchone()[0]
    #print(text)
    connection.commit()
    return text

#get_Title()


def get_Quote():
    connection = sqlite3.connect("/home/ram/MagicRoom.db")
    cur = connection.cursor()
    sql = "select count(*) from Magic_Quotes"
    cur.execute(sql)
    rows = cur.fetchall()
    list_names = []
    for element in rows:
        list_names.append(element)
    connection.commit()


    for element in list_names:
        count = int(element[0])
   # print(str(count)+"count")
    q_text_number = random.randint(1,count)
    cur = connection.cursor()
    sql = "select * from Magic_Quotes where Theme_ID = ?"
    cur.execute(sql, (q_text_number,))
    rows = cur.fetchall()
    list_quote = []
    for element in rows:
        list_quote.append(element)
    connection.commit()

    for element in list_quote:
        quote = element[1]
    print(quote)
    connection.close()
    return quote


#get_Quote()
