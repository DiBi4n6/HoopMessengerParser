#HoopParser to parse data from Hoop Messenger

import csv
import sqlite3
import time
import os

DATA_HEADERS = ('User ID', 'Username', 'DisplayName','UserPhone','Country','PhotoURL','CreatedDatetime')
DATA_HEADERS2 = ('TIME', 'MESSAGE', 'USER NAME','DISPLAY NAME','MEMBERS OF CONVO')
SQL_QUERY = "SELECT user_id, user_username, user_display_name, user_phone, user_region, user_photo_url, datetime(user_created_at/1000, 'unixepoch', 'localtime') AS 'Decoded Date/Time' FROM User"
SQL_QUERY2 = "SELECT datetime(ConversationEvent.CONVERSATION_EVENT_CREATED_AT/1000, 'unixepoch', 'localtime'), ConversationEvent.CONVERSATION_EVENT_MESSAGE_DATA, User.USER_USERNAME, User.USER_DISPLAY_NAME, Conversation.CONVERSATION_USER_INFOS FROM ConversationEvent LEFT JOIN User ON User.USER_JID = ConversationEvent.CONVERSATION_EVENT_CREATED_BY_USER_JID LEFT JOIN Conversation ON Conversation.CONVERSATION_ID = ConversationEvent.CONVERSATION_EVENT_CONVERSATION_ID WHERE ConversationEvent.CONVERSATION_EVENT_LOCAL_TIMESTAMP IS NOT NULL"
print('')
print('HoopParser v1.1')
print('Created by: DiBi4n6')
print ("This script will parse User data and Messages")
print ("from a HOOP database!")
print('')

with open('HoopUserDataParser.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)

    # Write headers for User Data
    writer.writerow(DATA_HEADERS)


    # Connect to DB and create cursor
    db = sqlite3.connect("CollectionDatabase")
    cur = db.cursor()

    # Run SQL query for User data
    for row in cur.execute(SQL_QUERY):

        # Write row data
        writer.writerow(row)

with open('HoopMessageParser.csv','w') as csv_file:
    writer = csv.writer(csv_file)

    # Write headers for Messages
    writer.writerow(DATA_HEADERS2)

    for row in cur.execute(SQL_QUERY2):
        writer.writerow(row)


    # Close DB connection
    db.close()

time.sleep(3)
print("Finished!!")
print('')

os.system('pause')
