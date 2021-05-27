from getpass import getpass
from mysql.connector import connect, Error
import plotly.express as px;
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pprint
try:


    check = "Select AVG(income)as average,AVG(income)-stddev(income) as lower_bound,AVG(income)+stddev(income) as upper_bound,MAX(Election.id) from person,Election;"
    cnx = #connection info

    cursor = cnx.cursor()
    
    cursor.execute(check)
    result = cursor.fetchall();
    avg = round(result[0][0])
    lower = round(result[0][1])
    upper = round(result[0][2])
    latest_election_id = result[0][3]
    second_query = f"""Select Constituency.name as NAME, CASE WHEN person.income BETWEEN 0 and {lower} THEN 'Lower class'
                                        WHEN person.income BETWEEN {lower} and {upper} THEN 'Middle class'
                                        WHEN person.income > {upper} THEN 'Upper class'
										END
                                        as income_bracket, Count(*) as total from ((  voter INNER JOIN 
										Constituency on voter.constituency_id = Constituency.id ) INNER JOIN person ON person.ID = voter.id ) INNER JOIN Voted_for ON Voted_for.voter_id = voter.id  
                                        where Voted_for.Election_ID=5 group by income_bracket,NAME  WITH ROLLUP ORDER BY NAME;"""
    cursor.execute(second_query);
    
    result = cursor.fetchall();
    total,upper,lower,middle = result[0][2],result[1][2],result[2][2],result[3][2]
    x_vals = list(set([i[0] for i  in result]));
    fig = make_subplots(rows=2,cols=1,subplot_titles = ["Voter turnout per constituency, for each income level","Cumulative voter turnout for each election"] );
    fig.add_trace(go.Bar(
    x = x_vals[:10],
    y =  [i[2] for i in result if i[1]=="Lower class" and i[0] != None][:10],
    name ="Lower class"),row=1,col=1)
    fig.add_trace(go.Bar(
    x = x_vals[:10],
    y =  [i[2] for i in result if i[1]=="Middle class" and i[0] != None][:10],
    name ="Middle class"),row=1,col=1) 
    fig.add_trace(go.Bar(
    x = x_vals[:10],
    y =  [i[2] for i in result if i[1]=="Upper class" and i[0] != None][:10],
    name ="Upper class"),row=1,col=1) 
    #fig.update_layout(barmode='group', xaxis_tickangle=-45)
    #fig.show()
    third_query = f""" Select Election.id,Election.start_time,COUNT(*) FROM Election INNER JOIN Voted_for on Voted_for.Election_ID=Election.id group by Election.id ORDER BY Election.id ; 
			"""
 
    cursor.execute(third_query);
    result = cursor.fetchall();

    fig2 =go.Bar(x = [i[1] for i in result],y = [i[2]for i in result],name = "Cumulative voter turnout")
    fig.append_trace(fig2,row=2,col=1);
    fig.update_xaxes(type="category",title_text = "election year", row=2, col=1)
    fig.update_yaxes(title_text = "voter turnout", row=2, col=1)
    fig.show();
    cnx.commit();
except Error as e:
    print(e)

