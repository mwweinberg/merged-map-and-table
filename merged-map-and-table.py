#python3

import pandas as pd
import numpy as np
import csv
import json
import time

#inputs: tempactinput.csv, temp_act_site_top.html, repoffinput.csv, rep_off_site_top.html, map_top.html, map_bottom.html
#temporary i/o: jsonholder.json
#outputs: index_TA_table.html, index_TA_table[DATE].html, index_RO_table.html, index_RO_table[DATE].html, index_map.html, index_map[DATE].html


##########################################################
#####tempt-act-html-table#################################
##########################################################
##input: tempactinput.csv, temp_act_site_top.html#########
##output: index_TA_table.html, index_TA_table[DATE].html##
##########################################################
def temp_act():


    #load the csv as the dataframe with only the columns you care about
    df_temp_act = pd.read_csv('tempactinput.csv', usecols = ['Organization Name (English)', 'Organization Name (Chinese)', 'Organization Origin', 'Chinese Partner Unit (English)', 'Chinese Partner Unit (Chinese)', 'Activity Name (English)', 'Activity Name (Chinese)', 'Activity Location (English)', 'Activity Location (Chinese)', 'Start Date', 'End Date'])


    #reorders the columns
    columnsTitles = ['Organization Name (English)', 'Organization Name (Chinese)', 'Organization Origin', 'Chinese Partner Unit (English)', 'Chinese Partner Unit (Chinese)', 'Activity Name (English)', 'Activity Name (Chinese)', 'Activity Location (English)', 'Activity Location (Chinese)', 'Start Date', 'End Date']
    df_temp_act = df_temp_act.reindex(columns=columnsTitles)

    #prevents truncation of field data
    pd.set_option('max_colwidth', -1)

    def temp_act_shuffle():
        #outputs html to a file
        #index = false is to avoid printing the index column
        new_table = df_temp_act.to_html(index = False, classes = ['tableizer-firstrow'], border = 0)

        #removes the formatting
        #changes the formatting for the table headers
        #I'm sure there is a more elegant way of doing this but I don't know it
        fixed_table_1 = new_table.strip('<table border="0" class="dataframe tableizer-firstrow">')
        fixed_table_1a = fixed_table_1.replace('<tr style="text-align: right;">', '<tr style="text-align: center;">')
        fixed_table_2 = fixed_table_1a.replace('<th>Organization Name (English)</th>', '<th style="width:10%">Organization Name (English)</th>')
        fixed_table_3 = fixed_table_2.replace('<th>Organization Name (Chinese)</th>', '<th style="width:10%">Organization Name (Chinese)</th>')
        fixed_table_4 = fixed_table_3.replace('<th>Organization Origin</th>', '<th style="width:10%">Organization Origin</th>')
        fixed_table_5 = fixed_table_4.replace('<th>Chinese Partner Unit (English)</th>', '<th style="width:10%">Chinese Partner Unit (English)</th>')
        fixed_table_6 = fixed_table_5.replace('<th>Chinese Partner Unit (Chinese)</th>', '<th style="width:10%">Chinese Partner Unit (Chinese)</th>')
        fixed_table_7 = fixed_table_6.replace('<th>Activity Name (English)</th>', '<th style="width:10%">Activity Name (English)</th>')
        fixed_table_8 = fixed_table_7.replace('<th>Activity Name (Chinese)</th>', '<th style="width:10%">Activity Name (Chinese)</th>')
        fixed_table_9 = fixed_table_8.replace('<th>Activity Location (English)</th>', '<th style="width:10%">Activity Location (English)</th>')
        fixed_table_10 = fixed_table_9.replace('<th>Activity Location (Chinese)</th>', '<th style="width:10%">Activity Location (Chinese)</th>')
        fixed_table_11 = fixed_table_10.replace('<th>Start Date</th>', '<th style="width:5%">Start Date</th>')
        fixed_table_12 = fixed_table_11.replace('<th>End Date</th>', '<th style="width:5%">End Date</th>')

        fixed_table = fixed_table_12
        return fixed_table

    temp_act_fixed_table = temp_act_shuffle()

    #This is the first part of the html page
    temp_act_top_half = open('static_inputs/temp_act_site_top.html', 'r')

    #this is the regular output
    temp_act_output_page = open('index_TA_table.html', 'w')

    #this creates the archive output
    timestamp = time.strftime("%Y%m%d")
    temp_act_output_page_archive_filename = "archive/index_TA_table" + timestamp + ".html"
    temp_act_archive_page = open(temp_act_output_page_archive_filename, 'w')

    #####for the regular page#######
    #writes the html to the new page
    for item in temp_act_top_half:
        temp_act_output_page.write(item)
        temp_act_archive_page.write(item)
    #writes the table
    for item in temp_act_fixed_table:
        temp_act_output_page.write(item)
        temp_act_archive_page.write(item)
    #closes out the page (this should be in the table but it isn't because I don't know why
    temp_act_output_page.write("table> <!–– add your tableizer data above this line––> </body> </html>")
    temp_act_archive_page.write("table> <!–– add your tableizer data above this line––> </body> </html>")

    temp_act_top_half.close()
    temp_act_output_page.close()
    temp_act_archive_page.close()

##########################################################
#####rep-off-html-table###################################
##########################################################
##input: repoffinput.csv, rep_off_site_top.html###########
##output: index_RO_table.html, index_RO_table[DATE].html##
##########################################################

def rep_off():

    #load the csv as the dataframe with only the columns you care about
    df_rep_off = pd.read_csv('repoffinput.csv', usecols = ['Organization Name (English)', 'Organization Name (Chinese)', 'Professional Supervisory Unit (English)', 'Professional Supervisory Unit (Chinese)', 'Organization Origin', 'Field of Work', 'Registration Location', 'Date of Registration', 'Permitted Area(s) of Operation'])


    #reorders the columns
    columnsTitles = ['Organization Name (English)', 'Organization Name (Chinese)', 'Professional Supervisory Unit (English)', 'Professional Supervisory Unit (Chinese)', 'Organization Origin', 'Field of Work', 'Registration Location', 'Date of Registration', 'Permitted Area(s) of Operation']
    df_rep_off = df_rep_off.reindex(columns=columnsTitles)

    #prevents truncation of field data
    pd.set_option('max_colwidth', -1)


    def rep_off_shuffle():
        #outputs html to a file
        #index = false is to avoid printing the index column
        new_table = df_rep_off.to_html(index = False, classes = ['tableizer-firstrow'], border = 0)

        #removes the formatting
        #changes the formatting for the table headers
        #I'm sure there is a more elegant way of doing this but I don't know it


        fixed_table_1 = new_table.strip('<table border="0" class="dataframe tableizer-firstrow">')
        fixed_table_1a = fixed_table_1.replace('<tr style="text-align: right;">', '<tr style="text-align: center;">')
        fixed_table_2 = fixed_table_1a.replace('<th>Organization Name (English)</th>', '<th style="width:10%">Organization Name (English)</th>')
        fixed_table_3 = fixed_table_2.replace('<th>Organization Name (Chinese)</th>', '<th style="width:10%">Organization Name (Chinese)</th>')
        fixed_table_4 = fixed_table_3.replace('<th>Professional Supervisory Unit (English)</th>', '<th style="width:10%">Professional Supervisory Unit (English)</th>')
        fixed_table_5 = fixed_table_4.replace('<th>Professional Supervisory Unit (Chinese)</th>', '<th style="width:5%">Professional Supervisory Unit (Chinese)</th>')
        fixed_table_6 = fixed_table_5.replace('<th>Organization Origin</th>', '<th style="width:5%">Organization Origin</th>')
        fixed_table_7 = fixed_table_6.replace('<th>Field of Work</th>', '<th style="width:10%">Field of Work</th>')
        fixed_table_8 = fixed_table_7.replace('<th>Registration Location</th>', '<th style="width:5%">Registration Location</th>')
        fixed_table_9 = fixed_table_8.replace('<th>Date of Registration</th>', '<th style="width:5%">Date of Registration</th>')
        fixed_table_10 = fixed_table_9.replace('<th>Permitted Area(s) of Operation</th>', '<th style="width:40%">Permitted Area(s) of Operation</th>')

        fixed_table = fixed_table_10
        return fixed_table

    rep_off_fixed_table = rep_off_shuffle()

    #This is the first part of the html page
    rep_off_top_half = open('static_inputs/rep_off_site_top.html', 'r')

    #this is the regular output
    rep_off_output_page = open('index_RO_table.html', 'w')

    #this creates the archive output
    timestamp = time.strftime("%Y%m%d")
    rep_off_output_page_archive_filename = "archive/index_RO_table" + timestamp + ".html"
    rep_off_archive_page = open(rep_off_output_page_archive_filename, 'w')


    #writes the html to the new page
    for item in rep_off_top_half:
        rep_off_output_page.write(item)
        rep_off_archive_page.write(item)
    #writes the table
    for item in rep_off_fixed_table:
        rep_off_output_page.write(item)
        rep_off_archive_page.write(item)
    #closes out the page (this should be in the table but it isn't because I don't know why
    rep_off_output_page.write("table> <!–– add your tableizer data above this line––> </body> </html>")
    rep_off_archive_page.write("table> <!–– add your tableizer data above this line––> </body> </html>")

    rep_off_top_half.close()
    rep_off_output_page.close()
    rep_off_archive_page.close()

##########################################################
#####csv2mapjson###################################
##########################################################
##input: repoffinput.csv, map_top.html, map_bottom.html###########
##temporary i/o: jsonholder.json
##output: index_map.html, index_map[DATE].html##
##########################################################

def rep_map():

    #turns the csv into a list of lists [[x, y, z,], [a, b, c]
    exampleFile = open('repoffinput.csv')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)


    #variable to hold the data we care about
    cleanData = []

    #removes header row
    del exampleData[0]

    #pull the data you care about into a new list. Each entry is a list in the list

    for row in exampleData:
        #this is the list of the elements for the individual entry
        subList = []

        #this goes through an plucks out the data that matters
        #breaks up the string value, turns it into numbers, and adds to list
        a,b = row[0].split(", ")
        locList = [float(a), float(b)]
        subList.append(locList)

        #clean up name and add
        if 'The' in row[4]:
            fullName = 'The ' + row[5]
        else:
            fullName = row[5]
        subList.append(fullName)

        #chinese name
        subList.append(row[6])
        #psu_en
        subList.append(row[7])
        #origin_loc
        subList.append(row[9])
        #sec
        subList.append(row[10])
        #regloc
        subList.append(row[12])
        #regdate
        subList.append(row[13])
        #actarea
        subList.append(row[14])
        #website_en
        subList.append(row[15])
        #website_ch
        subList.append(row[16])


        #once that list for the entry is created, it is added to cleanData
        cleanData.append(subList)


    #list to hold the list of dictionaries
    jsonList = []

    #creates the json
    for row in cleanData:
        #this is the dict for the entry
        subDict = {}

        subDict['geometry'] = {'type': 'Point', 'coordinates': row[0]}

        subDict['type'] = 'Feature'

        #this section only adds websites if they exist to the properties entry
        propertiesSubDict = {'orgname_en': row[1], 'orgname_ch': row[2], 'psu_en': row[3], 'originloc': row[4], 'sector': row[5], 'regloc': row[6], 'regdate': row[7], 'actarea': row[8]}

        if '.' in row[9]:
            propertiesSubDict['website_en'] = row[9]
        if '.' in row[10]:
            propertiesSubDict['website_ch'] = row[10]

        subDict['properties'] = propertiesSubDict

        #adds the now completed subDict to jsonList
        jsonList.append(subDict)

    #writes the json
    with open('static_inputs/jsonholder.json', 'w') as outfile:
        json.dump(jsonList, outfile)


    #This is the first part of the input html page
    map_top_half = open('static_inputs/map_top.html', 'r')
    #This re-inports the  json as a text file because . . . that's how it works
    map_middle = open('static_inputs/jsonholder.json', 'r')
    #This is the last part of the input html page
    map_bottom_half = open('static_inputs/map_bottom.html', 'r')

    #sets up the regular output
    map_output_page = open('index_map.html', 'w')
    ##sets up the archive output
    timestamp = time.strftime("%Y%m%d")
    map_output_page_archive_filename = "archive/index_map" + timestamp + ".html"
    map_archive_page = open(map_output_page_archive_filename, 'w')


    #writes the html to the new page
    for item in map_top_half:
        map_output_page.write(item)
        map_archive_page.write(item)
    #writes the json
    for item in map_middle:
        map_output_page.write(item)
        map_archive_page.write(item)
    #writes the end
    for item in map_bottom_half:
        map_output_page.write(item)
        map_archive_page.write(item)

    map_top_half.close()
    map_middle.close()
    map_bottom_half.close()
    map_output_page.close()
    map_archive_page.close()




temp_act()
rep_off()
rep_map()
