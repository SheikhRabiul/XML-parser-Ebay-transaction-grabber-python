"""
Created on Sat Jun 24 00:54:13 2017
Purpose: Making an ebay transaction dataset [parsing xml response from ebay and saving it in to a csv file]
@author: Sheikh Rabiul Islam 
"""
from xml.dom.minidom import parse
from urllib.request import urlopen
import xml.dom.minidom
import csv

#Starting item id
ITEMID=322338421702
#number of item you want to fetch
ROWNEEDED = 500

#open a csv file for writing parsed data
response_data = open('response_data21702.csv','w')

#create an object for csv writer
csvwriter = csv.writer(response_data)

#write data header of the csv file
re_head = []
re_head.append('ItemID')
re_head.append('Location')
re_head.append('PaymentMethods')
re_head.append('CurrentPrice')
re_head.append('StartTime')
re_head.append('Country')
re_head.append('PrimaryCate41goryID')
re_head.append('PrimaryCategoryName')
re_head.append('Title')
csvwriter.writerow(re_head)



#generate row_needed number of reques, parse xml file and store parsed data in csv file
for i in range(ROWNEEDED):
    item_idd = ITEMID + i
    print(item_idd)
    url = "http://open.api.ebay.com/shopping?callname=GetSingleItem&version=517&appid=WillGree-f395-4f80-a4aa-9afd33b046ac&ItemID=" + str(item_idd) + "&responseencoding=XML&IncludeSelector=Details"
    http_response = urlopen(url)
    
    DOMTree = xml.dom.minidom.parse(http_response);
    response = DOMTree.documentElement
    
    #get all elements inside item tag in items
    items = response.getElementsByTagName('Item')
            
    for item in items:    
        re_data = []
        ItemID = item.getElementsByTagName('ItemID')[0]
        print ("Item found with ID: %s" % ItemID.childNodes[0].data)
        Location = item.getElementsByTagName('Location')[0]
        PaymentMethods = item.getElementsByTagName('PaymentMethods')[0]
        CurrentPrice = item.getElementsByTagName('CurrentPrice')[0]
        StartTime = item.getElementsByTagName('StartTime')[0]
        Country = item.getElementsByTagName('Country')[0]
        PrimaryCategoryID = item.getElementsByTagName('PrimaryCategoryID')[0]
        PrimaryCategoryName = item.getElementsByTagName('PrimaryCategoryName')[0]
        Title = item.getElementsByTagName('Title')[0]    
        
        #store parsed data in the re_data list
        re_data.append(ItemID.childNodes[0].data)
        #location name may be in different language, so utf-8 encode
        re_data.append((Location.childNodes[0].data).encode('utf-8'))
        re_data.append(PaymentMethods.childNodes[0].data)
        re_data.append(CurrentPrice.childNodes[0].data)
        re_data.append(StartTime.childNodes[0].data)
        re_data.append(Country.childNodes[0].data)
        re_data.append(PrimaryCategoryID.childNodes[0].data)
        re_data.append(PrimaryCategoryName.childNodes[0].data)
        re_data.append(Title.childNodes[0].data)
        
        #write a row in the csv file
        csvwriter.writerow(re_data)

#close the file handler
response_data.close()