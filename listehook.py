#!/usr/bin/python
# -*- coding: utf-8 -*-
from webbot import Browser
import time
import os,sys
import threading
from threading import Thread
import random
import gc
from random import randint
from time import sleep
site = "http://" # buraya gezilecek siteyi giriniz
kelime = "kelime" #girilecek siteden bir kelime giriniz. dogru site olup olmadığı bu kelime ile kontrol edilecektir.
sayi = 10 #aynı anda kaç kişi siteye girsin. fazla sayıda işlem fazla cpu ve ram demektir. 
def main():
	while True:
		try:
			m1 = random.randint(20,500)
			m2 = random.randint(-200,700)
			m3 = random.randint(40,900)
			web = Browser(showWindow = False)
			web.set_page_load_timeout(60)
			web.go_to(site)
			if web.exists(kelime):
				sleep(random.randint(20,50))
				print("anasayfa")
				web.scrolly(m1) 
				web.scrolly(m2) 
				web.scrolly(m3)
				try:
					a = []
					a = web.find_elements(tag='a')
					sec = random.choice(a)
					sec.click()
					print(web.get_title())
					acik = web.get_total_tabs()
					if acik>1:
						web.switch_to_tab(2)
					sleep(random.randint(20,50))
					web.scrolly(m1) 
					web.scrolly(m2) 
					web.scrolly(m3)
					try:
						a = []
						a = web.find_elements(tag='a')
						sec = random.choice(a)
						sec.click()
						acik1 = web.get_total_tabs()
						if acik1>1:
							web.switch_to_tab(acik1)
						sleep(random.randint(20,50))
						print(web.get_title())
						web.scrolly(m1) 
						web.scrolly(m2) 
						web.scrolly(m3)
						try:
							a = []
							a = web.find_elements(tag='a')
							sec = random.choice(a)
							sec.click()
							acik2 = web.get_total_tabs()
							if acik2>1:
								web.switch_to_tab(acik2)
							sleep(random.randint(20,50))
							print(web.get_title())
							web.scrolly(m1) 
							web.scrolly(m2) 
							web.scrolly(m3)
							try:
								a = []
								a = web.find_elements(tag='a')
								sec = random.choice(a)
								sec.click()
								acik3 = web.get_total_tabs()
								if acik3>1:
									web.switch_to_tab(acik3)
								sleep(random.randint(20,50))
								print(web.get_title())
								web.scrolly(m1) 
								web.scrolly(m2) 
								web.scrolly(m3)
								try:
									a = []
									a = web.find_elements(tag='a')
									sec = random.choice(a)
									sec.click()
									acik4 = web.get_total_tabs()
									if acik4>1:
										web.switch_to_tab(acik4)
									sleep(random.randint(20,50))
									print(web.get_title())
									web.scrolly(m1) 
									web.scrolly(m2) 
									web.scrolly(m3)
									try:
										a = []
										a = web.find_elements(tag='a')
										sec = random.choice(a)
										sec.click()
										acik5 = web.get_total_tabs()
										if acik5>1:
											web.switch_to_tab(acik5)
										sleep(random.randint(20,50))
										print(web.get_title())
										web.scrolly(m1) 
										web.scrolly(m2) 
										web.scrolly(m3)
										try:
											a = []
											a = web.find_elements(tag='a')
											sec = random.choice(a)
											sec.click()
											acik6 = web.get_total_tabs()
											if acik6>1:
												web.switch_to_tab(acik6)
											sleep(random.randint(20,50))
											print(web.get_title())
											web.scrolly(m1) 
											web.scrolly(m2) 
											web.scrolly(m3)
											try:
												a = []
												a = web.find_elements(tag='a')
												sec = random.choice(a)
												sec.click()
												acik7 = web.get_total_tabs()
												if acik7>1:
													web.switch_to_tab(acik7)
												sleep(random.randint(20,50))
												print(web.get_title())
												web.scrolly(m1) 
												web.scrolly(m2) 
												web.scrolly(m3)
												web.quit()
											except:
												web.quit()
										except:
											web.quit()
									except:
										web.quit()
								except:
									web.quit()
							except:
								web.quit()
						except:
							web.quit()
					except:
						web.quit()	
				except:
					web.quit()	
			else:
				web.quit()
		except:
			web.quit()
if __name__ == '__main__':
    for t in range(sayi):
        t = threading.Thread(target=main)
        t.start()		
