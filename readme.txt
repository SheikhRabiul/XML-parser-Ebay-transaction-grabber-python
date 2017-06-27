#ebay-xml-parser.py is the main file to parse the xml response.

#command to run the parser
python ebay-xml-parser.py 

#parsing may be interrrupted if any response contains unusual xml 
#pattern. So, re-run this file just changing the ITEMID variable #to the last successful one + 1.Successful/failed itemids are #printed on the secreen while execution.  


#command to merge multiple csv file in to one csv file
python csv_merge.py

#you may end up with multiple csv file as its takes time to get a dataset with lots of records and there may be some interruption. So I wrote above script to merge all individuals csv files in to a single output file. 

