import eel,sqlite3
import wx
e = "fail"
eel.init("web")

# Start the index.html file
eel.start("index.html", size=(300, 650), position=(0,0), block=False)




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

@eel.expose
def insertm(msg):
    print(msg)
    print("inseting main")
    insertMain(msg)
    return "ok"


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
@eel.expose
def getProduct(msg):
    print(msg)
    products=selectNames()
    products1d=[]
    for i in range (0,len(products)):
        products1d = unpackTuple(products1d,products[i])
    eel.returnNames(products)

    
@eel.expose
def getTourAudio(msg):
    print(msg)
    eel.getTourPath(selectAudio("Audio_dir ",msg))

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
@eel.expose

def getMarker(msg):
    print(msg)
    longlat=selectAudio("Loc_LAT,Loc_LON", msg)
    longlat =longlat[0]
    lat,long = longlat
    eel.returnMarker(lat,long)
while True:
    eel.sleep(2.0)  