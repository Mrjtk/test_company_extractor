import requests
from bs4 import BeautifulSoup
import time 
from time import sleep
import json
import os
import csv
import re

def find_cin(companyname):
                                url2=f"https://www.zaubacorp.com/companysearchresults/{companyname}"
                                headers = {
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                                    }

                                page2=requests.get(url2,headers=headers)
                                soup2=BeautifulSoup(page2.content,'html')
                                company_data2=(soup2.get_text())
                                f=open("search.txt",'w')
                                f.write(company_data2)
                                f.close()
                                f=open("search.txt",'r')
                                a=f.readlines()
                                longest_word = max(a, key=len)

                                a=''
                                cin=''
                                for i in longest_word:
                                    a+=i
                                    if "CINNameAddress" in a:
                                        cin+=i
                                        if len(cin)<=21:
                                            pass
                                        else:
                                            break
                                    else:
                                        pass
                                cin=cin[1:]
                                return cin

