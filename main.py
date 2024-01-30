import requests
from bs4 import BeautifulSoup
import time 
from time import sleep
import json
import os
import csv
import re


import extract_filter
import name_cin


    
  
count=0
doption="1"
if doption=="1":
        filename="compny.txt" 
        f=open(filename,"r")
        file=f.readlines()  
        with open('Companydata_result3.csv', 'w+', encoding='utf-8', newline='') as f:
                                            writer=csv.writer(f)
                                            writer.writerow(["Company Name","Status","Slug","Address","state pincode","Roc","Date of Incorporation","Age of Company",'Category','Sub Category','Class of Company',"CIN",'Registration Number','Employment Details','Number of Member','Authorized Capital',"Paid up Capital",'Email Address','Phone Number',"Website Link"])
                                            
                                            for companyname in file:
                                                        b=companyname.upper()
                                                        propername=b.replace(" ","-")        
                                                        cin=name_cin.find_cin(companyname)
                                                        try:
                                                             output=extract_filter.compydata(propername,cin)
                                                        except:
                                                                continue
                                                        try:

                                            
                                                                writer.writerow(output)        
                                                        except:
                                                                pass
                                                        count+=1
                                                        print('Done ',count)
                                                        sleep(2)
                                                                               
