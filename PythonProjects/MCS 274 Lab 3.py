import matplotlib.pyplot as plt

import sqlite3

def example_table():
    #the data that will go in the table:
    table_data = [[1,2],[3,4],[5,6]]

    #names for the columns:
    column_labels = ["column1", "column2"]

    #for your table, you can just change table_data and column_labels -
    #you don't need to change the code below here

    #creates the figure and axes
    fig, ax = plt.subplots()

    #hide the axes, since we only want a table
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    #create the table
    table = ax.table(cellText = table_data, colLabels = column_labels, loc = 'center')

    #display the table
    fig.tight_layout()
    plt.show()

def example_bar_chart():
    #the x-values that will go into the chart
    x_values = ["first", "second", "third", "fourth"]

    #the corresponding y-values that will go in the chart
    y_values = [5,2,7,3]

    #labels
    x_label = "Label for x-axis"
    y_label = "Label for y-axis"
    chart_label = "Title for the chart"

    #for your chart, you can just change the values of x_values, y_values, x_label, y_label, chart_label,
    #you shouldn't need to change the code below here.
    
    #set the size of the figure
    #depending on your computer, you may need to adjust the figsize to get the chart to display nicely
    fig = plt.figure(figsize = (10,5))

    #position of labels on x-axis
    x_pos = [i for i, _ in enumerate(x_values)]

    #make the bar chart
    plt.bar(x_pos, y_values)

    #add labels
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(chart_label)

    #labels on x-axis
    plt.xticks(x_pos, x_values)

    #show the chart
    plt.show()

def parties():
    con = sqlite3.connect("election_modified.db")

    c = con.cursor()

    parties = c.execute("SELECT party_abbreviation, party_name FROM Parties")

    #the data that will go in the table:
    table_data = []

    for row in parties:
        table_data.append(row)

    #names for the columns:
    column_labels = ["Party Abbreviation", "Party Name"]

    #for your table, you can just change table_data and column_labels -
    #you don't need to change the code below here

    #creates the figure and axes
    fig, ax = plt.subplots()

    #hide the axes, since we only want a table
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    #create the table
    table = ax.table(cellText = table_data, colLabels = column_labels, loc = 'center')

    #display the table
    fig.tight_layout()
    plt.show()

    con.commit()

    con.close()

def senate_candidates():
    con = sqlite3.connect("election_modified.db")

    c = con.cursor()

    candidates = c.execute("SELECT DISTINCT candidate_name, party_abbreviation FROM candidates \
WHERE office_id IN \
(SELECT office_id FROM offices WHERE office_name= 'U.S. Senator')")

    #the data that will go in the table:
    table_data = []

    for row in candidates:
        table_data.append(row)

    #names for the columns:
    column_labels = ["Candidate", "Party Abbreviation"]

    #for your table, you can just change table_data and column_labels -
    #you don't need to change the code below here

    #creates the figure and axes
    fig, ax = plt.subplots()

    #hide the axes, since we only want a table
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    #create the table
    table = ax.table(cellText = table_data, colLabels = column_labels, loc = 'center')

    #display the table
    fig.tight_layout()
    plt.show()

    con.commit()

    con.close()

def votes_by_party():
    con = sqlite3.connect("election_modified.db")

    c = con.cursor()

    party_votes = c.execute("SELECT sum(results.votes), candidates.party_abbreviation \
FROM results INNER JOIN candidates ON results.candidate_id = candidates.candidate_id AND results.office_id = candidates.office_id \
GROUP BY candidates.party_abbreviation;")
    
    #the x-values that will go into the chart
    x_values = []
    y_values = []

    for row in party_votes:
        x_values.append(row[1])
        y_values.append(row[0])

    #labels
    x_label = "Party Abbreviation"
    y_label = "Total Votes"
    chart_label = "Votes by Party in Minnesota in the 2012 Election"

    #for your chart, you can just change the values of x_values, y_values, x_label, y_label, chart_label,
    #you shouldn't need to change the code below here.
    
    #set the size of the figure
    #depending on your computer, you may need to adjust the figsize to get the chart to display nicely
    fig = plt.figure(figsize = (10,5))

    #position of labels on x-axis
    x_pos = [i for i, _ in enumerate(x_values)]

    #make the bar chart
    plt.bar(x_pos, y_values)

    #add labels
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(chart_label)

    #labels on x-axis
    plt.xticks(x_pos, x_values)

    #show the chart
    plt.show()

    con.commit()

    con.close()



def senate_votes():
    con = sqlite3.connect("election_modified.db")

    c = con.cursor()

    candidates = c.execute("SELECT DISTINCT candidates.candidate_name, sum(results.votes) \
FROM results INNER JOIN candidates ON results.candidate_id = candidates.candidate_id AND results.office_id = candidates.office_id \
WHERE candidates.office_id IN \
(SELECT office_id FROM offices WHERE office_name= 'U.S. Senator') \
GROUP BY candidates.candidate_id, candidates.office_id ORDER BY candidates.candidate_name")
    
    #the x-values that will go into the chart
    x_values = []
    y_values = []

    for row in candidates:
        x_values.append(row[0])
        y_values.append(row[1])

    #labels
    x_label = "Senate_Candidates"
    y_label = "Total Votes"
    chart_label = "Votes for Minnesota U.S Senator 2012"

    #for your chart, you can just change the values of x_values, y_values, x_label, y_label, chart_label,
    #you shouldn't need to change the code below here.
    
    #set the size of the figure
    #depending on your computer, you may need to adjust the figsize to get the chart to display nicely
    fig = plt.figure(figsize = (10,5))

    #position of labels on x-axis
    x_pos = [i for i, _ in enumerate(x_values)]

    #make the bar chart
    plt.bar(x_pos, y_values)

    #add labels
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(chart_label)

    #labels on x-axis
    plt.xticks(x_pos, x_values)

    #show the chart
    plt.show()

    con.commit()

    con.close()

parties()
senate_candidates()
votes_by_party()
senate_votes()

'''
queries

SELECT party_abbreviation, party_name FROM Parties;

SELECT DISTINCT candidate_name, party_abbreviation FROM candidates
WHERE office_id IN
(SELECT office_id FROM offices WHERE office_name= 'U.S. Senator');

SELECT sum(results.votes), candidates.party_abbreviation
FROM results INNER JOIN candidates ON results.candidate_id = candidates.candidate_id AND results.office_id = candidates.office_id
GROUP BY candidates.party_abbreviation;

SELECT DISTINCT candidates.candidate_name, sum(results.votes) 
FROM results INNER JOIN candidates ON results.candidate_id = candidates.candidate_id AND results.office_id = candidates.office_id
WHERE candidates.office_id IN
(SELECT office_id FROM offices WHERE office_name= 'U.S. Senator')
GROUP BY candidates.candidate_id, candidates.office_id;
'''
