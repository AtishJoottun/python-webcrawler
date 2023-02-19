from distutils.dir_util import copy_tree
import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
     if(page>0):
          url = WebUrl
          code = requests.get(url)
          plain = code.text
          s = BeautifulSoup(plain, "html.parser")
          for link in s.findAll():
               tet = link.get('title')
               tet_2 = link.get('href')
               print(tet)
               print(tet_2)
                
                


web(2,'https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031&ref_=nav_shopall_sbc_mobcomp_all_mobiles')
