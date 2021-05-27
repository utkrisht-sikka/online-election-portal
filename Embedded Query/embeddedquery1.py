 
from base64 import b64encode
import mysql.connector
from datetime import date
 
  
# Create your views here.
def connectit():
  #connection info
    )
    return mydb

# https://www.mysqltutorial.org/python-mysql-blob/
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
#xxxxxxxxxxxxxxxxxx
        
def f_voter_view1():
    
    print("i1")
    connection=connectit()
    cursor=connection.cursor()
   
    cursor.execute("use Election")
    xxx="Tc8IFClQV0HQvXNnbtAD6PWCVOBI8p9SFXzC5hg0AJbaXArOAp3JaMaFBWeE8qPrSEIdDtflNZC9rxeAp7n1uJRRa7tSwRuI5D66"

    cursor.execute("select * from person where token=\""+xxx+"\"")  
    table=cursor.fetchall()
    id=table[0][0]
    cursor.execute("select * from Voted_for where Election_ID=6 and voter_id="+str(id));
    table=cursor.fetchall()
   
    print(table)
    if len(table)>0:
        cursor.execute("select FirstName, LastName from person where id="+str(table[0][1]))  
        table=cursor.fetchall()
        print("already voted")
        return 
    else:
        cursor.execute("""select person.FirstName,person.LastName,Political_Party.name,Political_Party.symbol,x.candid from person,Political_Party,Member_Of,
        (select Stands_From.id as candid from Constituency, voter,Stands_From
        where voter.id=1 and Constituency.id=voter.constituency_id and Stands_From.constituency_id=Constituency.id and Stands_From.election_id=5) as x
        where  x.candid=Member_Of.Candidate_id and Member_Of.Party_ID=Political_Party.id and x.candid=person.ID""")
        table=cursor.fetchall()
      
        print("i2")
        #print(table)
      
        cursor.close()
        connection.close()
        count=0
        filename="symbol"
        for i in table:
            write_file(i[3], filename+str(count)+".png")
            print(i[0]+" "+i[1]+" "+i[2]+" "+str(i[4]))
            count+=1
        # print("b2")
        # print(imgs)
        return


  
# creating a object 
f_voter_view1()
 
