import requests
from bs4 import BeautifulSoup
import time 
from time import sleep
import json
import os
import csv

def addr(a,b):
                    url="https://www.zaubacorp.com/company/{}/{}".format(a,b)   

                    headers = {
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                                    }

                    page2=requests.get(url,headers=headers)
                    soup2=BeautifulSoup(page2.text,'html.parser')
                    div_element=soup2.find_all("div",class_="col-lg-6 col-md-6 col-sm-12 col-xs-12")
                    div_element=str(div_element)
                    soup=BeautifulSoup(div_element,'html.parser')
                    address=[]
                    addr=soup.find_all('p')
                    for i in addr:
                            address.append(i.text)
                    data=(address[-1::])
                    data=str(data)
                    pin=None
                    words=data.split()
                    for i, word in enumerate(words):
                                if word.isdigit() and len(word) == 6:
                                    pin = word
                                    break
                    data=str(data)
                    pin=str(pin)    
                    return data,pin 

def compydata(a,b):
                    
                    url="https://www.zaubacorp.com/company/{}/{}".format(a,b)   

                    headers = {
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                                    }

                    page2=requests.get(url,headers=headers)
                    soup2=BeautifulSoup(page2.content,'html.parser')
                    td_tags = soup2.find_all('td')

                    # Extract text content within <p> tags inside <td> tags
                    result_data = []
                    for td_tag in td_tags:
                        p_tags = td_tag.find_all('p')
                        for p_tag in p_tags:
                            result_data.append(p_tag.get_text().strip())

                    # Print the extracted data
                    # print(result_data)

                    cinn=result_data.index("CIN")+1
                    cinno=result_data[cinn]
                    
                    company_name=result_data.index("Company Name")+1
                    companyname=result_data[company_name]   
                    
                    slug=str(companyname)
                    slug=slug.replace(" ","_")
                    slug=slug.lower()
                    
                    
                    company_status=result_data.index("Company Status")+1
                    companystatus=result_data[company_status]   
                    
                    
                    roc=result_data.index("RoC")+1
                    roc_state=result_data[roc]
                    
                    registration=result_data.index("Registration Number")+1
                    registrationno=result_data[registration]
                    
                    Company_caterg=result_data.index("Company Category")+1
                    company_category=result_data[Company_caterg]
                    
                    company_subcaterg=result_data.index("Company Sub Category")+1
                    company_subcategory=result_data[company_subcaterg]
                    
                    classofcompany=result_data.index("Class of Company")+1
                    classofcompany=result_data[classofcompany]
                    
                    Date_of_Incorporation=result_data.index("Date of Incorporation")+1
                    dateofincorporation=result_data[Date_of_Incorporation]
                    
                    ageofcompany=result_data.index("Age of Company")+1
                    ageofcompany=result_data[ageofcompany]
                    
                    numberofmembers=result_data.index("Number of Members")+1
                    numberofmembers=result_data[numberofmembers]
                    
                    authorizd_capital=result_data.index("Authorised Capital")+1
                    authorizdcapital=result_data[authorizd_capital]
                    authorizdcapital=authorizdcapital[1:]
                    
                    paidup_capital=result_data.index("Paid up capital")+1
                    paidupcapital=result_data[paidup_capital]
                    paidupcapital=paidupcapital[1:]
                    
                    address,pin=addr(a,b) 
                    address=address[2:-2]
                    
                    output=(companyname,companystatus,slug,address,pin,roc_state,dateofincorporation,ageofcompany,company_category,company_subcategory,classofcompany,cinno,registrationno,'Employment Details',numberofmembers,authorizdcapital,paidupcapital,'Email Address','Phone Number',"Website Link")
                    return output
                
