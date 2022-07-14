#all imports
import eel,sqlite3
import wx
import gpsloc
e = "fail"
eel.init("web")

# Start the index.html file
eel.start("index.html", size=(300, 650), position=(0,0), block=False)



#SQL ststment to insert data to database
def insertMain(values): # create function to insert data
    with sqlite3.connect("AudioTour2.db") as db: # connect to the database
        print ("connected")
        try:
            cursor = db.cursor() # create cursor
            sql = "Insert into Main_tbl (Tourname, Audio_dir, Loc_LAT, Loc_LON) values (?,?,?,?)" # create SQL statement, using ? mark to paramatise this query, so you can pass any value into this function
            cursor.execute(sql,values)# execute the SQL statement and pass values
            db.commit() # save changes
        except Exception as e:
            print(e)
#eel function to pass though
@eel.expose
def insertm(msg):
    print(msg)
    print("inseting main")
    insertMain(msg)
    return "ok"

#get names for drop down
def selectNames():
 with sqlite3.connect("AudioTour2.db") as db: # connect to the database
        try:
            cursor = db.cursor() # create cursor
            cursor.execute("SELECT Tourname FROM Main_tbl;")
            products = cursor.fetchall()
            print(products)
            return products
        except Exception as e:
            print(e)
            return None
#Dynamic SQL statment for gathering data from table 
def selectAudio(select,tourname):
 with sqlite3.connect("AudioTour2.db") as db: # connect to the database
        try:
            cursor = db.cursor() # create cursor
            cursor.execute("SELECT " + select + " FROM Main_tbl WHERE Tourname='" + tourname +"' ;")
            products = cursor.fetchall()
            print(products)
            return products
        except Exception as e:
            print(e)
            return None

#tuple unpacking for dropdown
def unpackTuple(products1d,item):
    """based on 
https://wwww.geeksforgeeks.org/unpacking-a-tuple-in-python/
and
https://thispointer.com/python-how-to-unpack-list-tuple-or-dictionary-to-function-arguments-using/
and
https://www.javaexersise.com/python/python-convert-tuple-to-string.php
"""
    item1 = "".join(item)
    products1d.append(item1)
    return products1d
#unapcking data for dropdown
@eel.expose
def getProduct(msg):
    print(msg)
    products=selectNames()
    products1d=[]
    for i in range (0,len(products)):
        products1d = unpackTuple(products1d,products[i])
    eel.returnNames(products)

#function to return souce/path for audio tour
@eel.expose
def getTourAudio(msg):
    print(msg)
    eel.getTourPath(selectAudio("Audio_dir ",msg))
#function for uploading path
@eel.expose
def pythonFunction(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    print(path)
    return path
#function for returning guide marker location to javascipt though eels.
@eel.expose
def getMarker(msg):
    print(msg)
    longlat=selectAudio("Loc_LAT,Loc_LON", msg)
    longlat =longlat[0]
    lat,long = longlat
    eel.returnMarker(lat,long)
#function that gets user location data though gps
@eel.expose
def getUserloc():
    print("attahced")
    ulat,ulong = gpsloc.gps()
    print(ulat,)

    eel.returnUserloc(ulat,ulong)

while True:
    eel.sleep(2.0)  