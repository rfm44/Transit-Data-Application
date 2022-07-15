import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passord",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = "insert into mbta_buses (route_number, id, bearing, current_status,current_stop_sequence, direction_id,label,latitude,longitude,occupancy_status,speed,updated_at) values (%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['route_number'],mbtaDict['id'], mbtaDict['bearing'], mbtaDict['current_status'],mbtaDict['current_stop_sequence'],mbtaDict['direction'],mbtaDict['label'],mbtaDict['latitude'],mbtaDict['longitude'],mbtaDict['occupancy_status'],mbtaDict['speed'],mbtaDict['updated_at'])
        mycursor.execute(sql, val)

    mydb.commit()