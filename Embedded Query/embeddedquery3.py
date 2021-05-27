from getpass import getpass
from mysql.connector import connect, Error
import plotly.express as px;
import pprint
try:


    check = "Select Political_Party.name as name,YEAR(Election.start_time) as st,Sum(Money_Spent)     from ( Political_Party INNER JOIN Member_Of ON Member_Of.Party_ID=Political_Party.id) INNER     JOIN Election ON Election.id = Member_Of.Election_id group by name,st ;"
    cnx = #connection info

    cursor = cnx.cursor()
    
    cursor.execute(check)
	
    result = cursor.fetchall();

    plot= [{"name":i[0],"YEAR":i[1],"wealth":i[2]} for i in result]
	
    
    fig = px.bar(plot,x="name", y="wealth",color="YEAR",title="Election spending, per election, per party.")   
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.show();
    cnx.commit();
except Error as e:
    print(e)

