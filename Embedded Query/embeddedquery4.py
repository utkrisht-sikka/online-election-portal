from base64 import b64encode
import mysql.connector
from datetime import datetime
import time

def connectit():
  #connection info
    )
    return mydb

# https://www.mysqltutorial.org/python-mysql-blob/
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
#xxxxxxxxxxxxxxxxxx

def verification_official():

    connection=connectit()
    cursor=connection.cursor()
    cursor.execute("""use Election""")
    cursor.execute("select * from Unverified_User where V_official_id=20225")
    table=cursor.fetchall()

    count=0
    fname="verifdoc"

    if(len(table)==0):
        print("You currently have no users to verify.")
        return
    print("Unverified_id \t\t\t Verification_Document_Type")

    uvids=[]
    for i in table:
        write_file(i[2], fname+str(i[0])+".png")
        print(str(i[0])+"\t\t\t\t "+str(i[1]))
        uvids.append(i[0])
        count+=1

    print("Verification Documents can be viewed from current folder.")
    
    print("Enter Unverified_id of user to verify.")
    print("Enter 'end' to exit.")
    s=input()

    check1=False

    if(s=="end"):
        return
    else:
        try:
            if int(s) in uvids:
                check1=True
        except:
            print("Incorrect Input.")
            return

    if check1:
        print("Enter 'verify' to confirm verification of user with ID="+s)
        ss=input()
        if ss=="verify":

            cursor.execute("select Constituency_id from Verification_Official where id=20214")
            table=cursor.fetchall()

            contituencyid=0
            for t in table:
                for x in t:
                    constituencyid=x
                    break
                break

            cursor.execute("select * from Unverified_User where Unverified_id="+str(s))
            table=cursor.fetchall()
            x=table[0]

            # x=f"insert into Election.voter (id, constituency_id) VALUES ({x[0]},{constituencyid})"
            query="insert into Election.voter (id, constituency_id) VALUES (%s,%s)"
            inp=(x[0],constituencyid)
            # print(x)
            cursor.execute(query,inp)
            connection.commit()
            
            query = "Update Election.voter set Registration_Date = %s where id = %s"
            current_Date = datetime.now()
            formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S')
            inp = (formatted_date, x[0])
            cursor.execute(query, inp)
            connection.commit()

            # print(cursor.rowcount, "record inserted in 'voter'.")

            fil="verifdoc"+str(x[0])+".png"
            thedata = open(fil, 'rb').read()
            # print(fil)

            query="update Election.voter set document=%s where id=%s"
            inp=(thedata,x[0])
            cursor.execute(query,inp)
            connection.commit()

            cursor.execute("delete from Election.Unverified_User where Unverified_id= "+str(x[0]))
            # inp=(x[0])
            # cursor.execute(query,inp)
            connection.commit()

            cursor.close()
            connection.close()
            print("User verified.\nUser Data deleted from 'Unverified_User'.\nUser data added to 'Voter'.")

            return
        else:
            print("Unverified User with Unverified_id="+s+" not verified.")
            return
    else:
        print("You have entered incorrect Unverified_id.")
        return

verification_official()
