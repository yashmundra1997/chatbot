from wit import Wit
import pymysql
from flask import Flask
from http.server import BaseHTTPRequestHandler,HTTPServer
import time
import psycopg2
import pytz
import datetime
from urllib.parse import unquote
access_token="RFXODTPVAHU625FDDOYNIF264AKMAU23"
client=Wit(access_token=access_token)
def get_hod(Branch):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from hod where branch=%(b)s",{'b':Branch})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
		else:
			x=result[0][0]+" "+result[0][1]
			return x
	except:
		return "no result found ask properly"
def get_chairman(group):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from members where branch=%(g)s and designation='Chairman'",{'g':group})
		result=cursor.fetchall()
		if len(result)==0:
			return "no result found ask properly"
		else:
			x=result[0][0]+" "+result[0][1]
			return x
			print("AITRBOT:",result[0][0],result[0][1])
	except:
		return "no result found ask properly"
def get_secretary(group):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from members where branch=%(g)s and designation='Secretary'",{'g':group})
		result=cursor.fetchall()
		if len(result)==0:
			return "no result found ask properly"
		else:
			x=result[0][0]+" "+result[0][1]
			return x
	except:
		return "no result found ask properly"
def get_info(firstName,lastName):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		if len(result)==0:
			return "no result found ask properly"
		else:
			cursor.execute("select designation,branch,gender from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
			mainResult=cursor.fetchall()
			if len(mainResult)==0:
				return "no result found ask properly"
			else:
				if mainResult[0][2]=='M':
					x="He is the "+mainResult[0][0]+" in "+mainResult[0][1]+" department."
					return x
				else: 
					x="She is the "+mainResult[0][0]+" in "+mainResult[0][1]+" department."
					return x
	except:
		return "no result found ask properly"
def get_professor(branch):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from associate_professor where branch=%(b)s",{'b':branch})
		result=cursor.fetchall()
		if len(result)==0:
			return "no result found ask properly"
		else:
			s=''
			for x in result:
				s=s+x[0]+x[1]+"\n"
			return s
				
	except:
		return "no result found ask properly"
def get_professor_by_gender(branch,gender):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		if gender=='male':
			cursor.execute("select firstName,lastName from associate_professor where branch=%(b)s and gender='M'",{'b':branch})
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else:
				s=''
				for x in result:
					s=s+x[0]+x[1]+"\n"
				return s
		elif gender=='female':
			cursor.execute("select firstName,lastName from associate_professor where branch=%(b)s and gender='F'",{'b':branch})
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else:
				s=''
				for x in result:
					s=s+x[0]+x[1]+"\n"
				return s	
	except:
		return "no result found ask properly"
def get_confirm_hod(firstName,lastName,type,branch):
	try:
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		cursor.execute("select designation,branch from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		mainResult=cursor.fetchall()
		if len(mainResult)==0:
			return "no result found ask properly"
		else:
			if mainResult[0][0]==type and mainResult[0][1]==branch:
				print("AITRBOT: Yes")
			else:
				print("AITRBOT: No")
	except:
		return "no result found ask properly"
def get_confirm_professor(firstName,lastName,type,branch):
	try:
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		cursor.execute("select designation,branch from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		mainResult=cursor.fetchall()
		if len(mainResult)==0:
			return "no result found ask properly"
		else:
			if mainResult[0][0]==type and mainResult[0][1]==branch:
				print("AITRBOT: Yes")
			else:
				print("AITRBOT: No")
	except:
		return "no result found ask properly"
def get_confirm_degree(firstName,lastName,type):
	try:
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		cursor.execute("select Qualification from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		mainResult=cursor.fetchall()
		mainResult=mainResult[0]
		s=''.join(mainResult)
		print(s)
		i=s.find(type)
		if i==-1:
			return "no result found ask properly"
		else:
			return "Yes"
	except:
		return "no result found ask properly"
def get_sports():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select name from sports")
		result=cursor.fetchall()
		if len(result)==0:
			return "no result found ask properly"
		else:
			r=''
			for x in result:
				r=r+x[0]+"\n"
			return r
	except:
		return "no result found ask properly"
def get_indoor_games():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select name from sports where type='Indoor'")
		result=cursor.fetchall()
		if len(result)==0:
			return "no result found ask properly"
			print("no result found ask properly")
		else:
			r={}
			for x in result:
				r.add(x[0])
			return r
	except:
		return "no result found ask properly"
def get_outdoor_games():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select name from sports where type='Outdoor'")
		result=cursor.fetchall()
		if len(result)==0:
			return "no result found ask properly"
			print("no result found ask properly")
		else:
			r={}
			for x in result:
				r.add(x[0])
			return r

	except:
		return "no result found ask properly"
def get_group_chairman(group):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from members where institutes=%(g)s and designation='Group Chairman'",{'g':group})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
			print("no result found ask properly")
		else:
			print("AITRBOT:",result[0][0],result[0][1])
	except:
		return "no result found ask properly"
def get_director(group):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from members where branch=%(g)s and designation='Director'",{'g':group})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
			print("no result found ask properly")
		else:
			s=result[0][0]+" "+result[0][1]
			print(s)
			return s
			print("AITRBOT:",result[0][0],result[0][1])
	except:
		return "no result found ask properly"
def get_group_director_cdc():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from members where designation='Group Director CDC'")
		result=cursor.fetchall()
		if len(result)==0:
			return "No result found ask Properly"
			print("no result found ask properly")
		else:	
			return result[0][0]+" "+result[0][1]
			print("AITRBOT:",result[0][0],result[0][1])
	except:
		return "no result found ask properly"
def get_confirm_gender(firstName,lastName,gender):
	try:
		db=pymysql.connect("localhost","root","mundra","chatbot")
		cursor=db.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		print(result)
		cursor.execute("select gender from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		mainResult=cursor.fetchall()
		if len(mainResult)==0:
			return "no result found ask properly"
			print("no result found ask properly")
		else:
			if mainResult[0][0]==gender:
				print("AITRBOT: Yes")
			else:
				print("AITRBOT: No")
	except:
		return "no result found ask properly"
def get_address():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select address from about_aitr")
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
			print("AITRBOT: Ask properly")
		else:
			x=result[0][0]
			return x
			print("AITRBOT :",result[0][0])
	except:
		return "no result found ask properly"
def get_contact_no():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select contact_no from about_aitr")
		result=cursor.fetchall()
		print(result[0][0])
		if len(result)==0:
			return "no result found ask properly"
			print("AITRBOT: Ask properly")
		else:
			print("else me gaya")
			s=result[0][0]
			print(s)
			return s
			print("AITRBOT :",result[0][0])
	except:
		return "no result found ask properly"
def get_affiliations():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select affiliations from about_aitr")
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
			print("AITRBOT: Ask properly")
		else:
			return result[0][0]
			print("AITRBOT :",result[0][0])
	except:
		return "no result found ask properly"
def get_timing_year(year):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select time from timing where year=%(y)s",{'y':year})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
			print("AITRBOT: Ask properly")
		else:
			x=result[0][0]
			return x
			print("AITRBOT :",result[0][0])
	except:
		return "no result found ask properly"
def get_timing_shift(year):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select time from timing where shift=%(y)s",{'y':year})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
			print("AITRBOT: Ask properly")
		else:
			x=result[0][0]
			return x
			print("AITRBOT :",result[0][0])
	except:
		return "no result found ask properly"
def give_facility(group):
	try:
		if group=='AITR':
			x="1.Well Equipped Laboratories."+"\n"+"2.Wi-Fi zone and Leased Line Internet."+"\n"+"3.E-Lrary with more than 16000 books and 52 National and International Journals."+"\n"+"4.On line lectures of National and International Experts through EDUSAT."+"\n"+"5.Training and Placement cell."+"\n"+"6. Technical and Soft Skill Training for campus selection."+"\n"+"7. Dell computers with 19 inch TFT-LCD monitors."+"\n"+"8. EMC academic alliance programme."+"\n"+"9. Research and consultancy Programme."+"\n"+"10. Energy Conservation Cell and Energy Audit for Industries."+"\n"+"11. Language Lab."+"\n"+"12. News Bulletin."+"\n"+"13. Faculty Development Programme on every Saturday."+"\n"+"14. MATLAB facility."
			return x
	except:
		return "no result found ask properly"
def get_info_acropolis(type):
	try:
		if type=='acropolis':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='about_us'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='canteen':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='canteen'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='vision':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='vision'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='mission':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='mission'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='vision and mission':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='v&m'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='GD room':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='gd room'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='laboratories':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='laboratories'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='mechanical workshop':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='mechanical workshop'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='sports':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='sports'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='classroom':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='classroom'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='hostel':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='hostel'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='ecell':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='ecell'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='training':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='training'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='CDC':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='CDC'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]
		elif type=='yhc':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='yhc'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]	
		elif type=='women cell':
			connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
			cursor=connection.cursor()
			cursor.execute("select content from info where information='women cell'")
			result=cursor.fetchall()
			if len(result)==0:
				return "no result found ask properly"
			else: 
				return result[0][0]		
	except:
		return "no result found ask properly"
def get_seats(branch):
	try:
		print(branch)
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select Intake,course_name from admission where specialization=%(b)s",{'b':branch})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
		else:
			for x in result:
				seats=x[0]
				course=x[1]
			return str(seats)+" in "+course
	except:
		return "no result found ask properly"
def get_eligibilty(branch):
	try:
		print(branch)
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select eligibility from admission where specialization=%(b)s",{'b':branch})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			print("AITRBOT: Ask properly")
			return "no result found ask properly"
		else:
			return result[0][0]
	except:
		return "no result found ask properly"
def get_library_timing():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select year,timing from library")
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			print("AITRBOT: Ask properly")
		else:
			return result[0][0]+"year:"+result[0][1]+"\n"+result[1][0]+"year:"+result[1][1]+"\n"+result[2][0]+"year:"+result[2][1]+"\n"+result[3][0]+"year:"+result[3][1]+"\n"
	except:
		return "no result found ask properly"
def get_timing_year_library(year):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select timing from library where year=%(y)s",{'y':year})
		result=cursor.fetchall()
		if len(result)==0:
			print("Ask properly")
		else:
			return result[0][0]
	except:
		return "no result found ask properly"
def get_timing():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select year,time from timing")
		result=cursor.fetchall()
		if len(result)==0:
			print("Ask properly")
		else:
			return result[0][0]+"year:"+result[0][1]+"\n"+result[1][0]+"year:"+result[1][1]+"\n"+result[2][0]+"year:"+result[2][1]+"\n"+result[3][0]+"year:"+result[3][1]+"\n"
	except:
		return "no result found ask properly"	
def get_list_hod():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName,branch from hod")
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			print("no result found ask properly")
		else:
			b=''
			for x in result:
				b=b+x[2]+": "+x[0]+" "+x[1]+"\n"
			return b
	except:
		return "no result found ask properly"
def get_list_management():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName,designation from members")
		result=cursor.fetchall()
		print("hi",result)
		if len(result)==0:
			print("no result found ask properly")
		else:
			b=''
			for x in result:
				b=b+x[2]+": "+x[0]+" "+x[1]+"\n"
			return b
	except:
		return "no result found ask properly"
def get_list_faculties():
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select firstName,lastName from associate_professor")
		result=cursor.fetchall()
		print("hi",result)
		if len(result)==0:
			print("no result found ask properly")
		else:
			b=''
			for x in result:
				b=b+x[0]+" "+x[1]+"\n"
			return b
	except:
		return "no result found ask properly"
def get_qualification(firstName,lastName):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select associatedTables from main where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		if len(result)==0:
			return "no result found ask properly"
		else:
			cursor.execute("select Qualification from "+result[0][0]+" where firstName=%(fn)s and lastName=%(ln)s",{'fn':firstName,'ln':lastName})
			mainResult=cursor.fetchall()
			if len(mainResult)==0:
				return "no result found ask properly"
			else:
				return mainResult[0][0]
	except:
		return "no result found ask properly"
def get_vision_department(branch):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select content from vision_department where branch=%(b)s",{'b':branch})
		result=cursor.fetchall()
		if len(result)==0:
			return "no result found ask properly"
		else:
			return result[0][0]
	except:
		return "no result found ask properly"
def get_mission_department(branch):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select content from mission_department where branch=%(b)s",{'b':branch})
		result=cursor.fetchall()
		if len(result)==0:
			return "no result found ask properly"
		else:
			return result[0][0]
	except:
		return "no result found ask properly"
def get_contact_people(firstName,lastName):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select contact_no from contact where firstName=%(fn)s and lastname=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
		else:
			return result[0][0]
	except:
		return "no result found ask properly"
def get_email(firstName,lastName):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select email from contact where firstName=%(fn)s and lastname=%(ln)s",{'fn':firstName,'ln':lastName})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
		else:
			return result[0][0]
	except:
		return "no result found ask properly"
def get_placement_year(y):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select sum(nos) from placement where year=%(fn)s",{'fn':y})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
		else:
			return str(result[0][0])
	except:
		return "no result found ask properly"
def get_placement_branch(b,y):
	try:
		print("go")
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select sum(nos) from placement where branch=%(bn)s and year=%(fn)s",{'bn':b,'fn':y})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
		else:
			r=str(result[0][0])+" students are placed of "+b+" branch."
			return r
	except:
		return "no result found ask properly"
def get_placement_company(y,c):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select sum(nos) from placement where year=%(fn)s and company_name=%(cn)s",{'fn':y,'cn':c})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
		else:
			return str(result[0][0])
	except:
		return "no result found ask properly"
def get_company_list(b):
	try:
		connection=psycopg2.connect(user='qkcbawmiqkysdd',password='35b198d914d171fc6b1e41079aeaa1753553666bb444a206228d1ae752deb8c6',host='ec2-107-22-253-158.compute-1.amazonaws.com',port='5432',database='dfq8opfmeh8l2t')
		cursor=connection.cursor()
		cursor.execute("select company_name from placement where branch=%(bn)s",{'bn':b})
		result=cursor.fetchall()
		print(result)
		if len(result)==0:
			return "no result found ask properly"
		else:
			b=''
			for x in result:
				b=b+x[0]+"\n"
			print(b)
			return b
			
	except:
		return "no result found ask properly"
def get_company():
	try:
		x="Zensar"+"\n"+"Yash Technologies"+"\n"+"L&T"+"\n"+"TCS"+"\n"+"Wipro"+"\n"+"Infosys"+"\n"+"Cognizant"+"\n"+"Persistent"+"\n"+"Capgemini"+"\n"+"many more......"
		return x
	except:
		return "no result found ask properly"
def formal_greeting():
	tz=pytz.timezone('Asia/Kolkata')
	currentDT=datetime.now(tz)
	x=currentDT.hour
	m=currentDT.minute
	if x>0 and x<=12:
		if m>0 and x==12:
			return "good afternoon"
		return "good morning"
	if x>12 and x<=17:
		if m>0 and x==17:
			return "good evening"
		return "good afternoon"
	else:
		return "good evening"
def process(message):
	print("hi")
	print(message)
	resp=client.message(message)
	print(resp)
	if "bye" in message:
		print("AITRBOT: bye")
	if not "intent" in resp['entities']:
		print("AITRBOT: I am confused ask properly")
	elif resp['entities']['intent'][0]['value']=='greetings':
		return resp['_text']+" How can i help you"
		print("AITRBOT: "+resp['_text']+" How can i help you")
	elif resp['entities']['intent'][0]['value']=='get_hod':
		if not "branch" in resp['entities']:
			return "no result found ask properly"
		else:
			branch=resp['entities']['branch'][0]['value']
			x=get_hod(branch)
			return x
	elif resp['entities']['intent'][0]['value']=='get_chairman':
		group=resp['entities']['group'][0]['value']
		x=get_chairman(group)
		return x
	elif resp['entities']['intent'][0]['value']=='get_secretary':
		group=resp['entities']['group'][0]['value']
		x=get_secretary(group)
		return x
	elif resp['entities']['intent'][0]['value']=='get_info':
		if not "firstName" in resp['entities']:
			return "please provide full name"
			print("AITRBOT: please provide full name")
		else:
			firstName=resp['entities']['firstName'][0]['value']
		if not "lastName" in resp['entities']:
			return "please provide full name"
			print("AITRBOT: please provide full name")
		else:
			lastName=resp['entities']['lastName'][0]['value']
		x=get_info(firstName,lastName)
		return x
	elif resp['entities']['intent'][0]['value']=='get_confirm_gender':
		firstName=resp['entities']['firstName'][0]['value']
		lastName=resp['entities']['lastName'][0]['value']
		gender=resp['entities']['gender'][0]['value']
		if gender=='male':
			get_confirm_gender(firstName,lastName,'M');
		if gender=='female':
			get_confirm_gender(firstName,lastName,'F');
	elif resp['entities']['intent'][0]['value']=='get_professor':
		branch=resp['entities']['branch'][0]['value']
		if not "gender" in resp['entities']:
			x=get_professor(branch)
			return x
		elif resp['entities']['gender'][0]['value']=='male' or resp['entities']['gender'][0]['value']=='female':
			print("hi")
			x=get_professor_by_gender(branch,resp['entities']['gender'][0]['value'])
			return x
	elif resp['entities']['intent'][0]['value']=='get_confirm':
		firstName=resp['entities']['firstName'][0]['value']
		lastName=resp['entities']['lastName'][0]['value']
		type=resp['entities']['type'][0]['value']
		if type=='HOD':
			branch=resp['entities']['branch'][0]['value']
			get_confirm_hod(firstName,lastName,type,branch)
		if type=='professor':
			branch=resp['entities']['branch'][0]['value']
			get_confirm_professor(firstName,lastName,type,branch)
		if type=='BE':
			get_confirm_degree(firstName,lastName,type)
	elif resp['entities']['intent'][0]['value']=='get_sports':
		x=get_sports()
		return x	
	elif resp['entities']['intent'][0]['value']=='get_indoor_games':
		x=get_indoor_games()
		return x	
	elif resp['entities']['intent'][0]['value']=='get_outdoor_games':
		x=get_outdoor_games()
		return x
	elif resp['entities']['intent'][0]['value']=='get_group_chairman':
		group=resp['entities']['group'][0]['value']
		x=get_group_chairman(group)
		return x
	elif resp['entities']['intent'][0]['value']=='get_director':
		group=resp['entities']['group'][0]['value']
		x=get_director(group)
		return x
	elif resp['entities']['intent'][0]['value']=='get_group_director_cdc':
		x=get_group_director_cdc()
		return x
	elif resp['entities']['intent'][0]['value']=='get_address':
		x=get_address()
		return x
	elif resp['entities']['intent'][0]['value']=='get_contact_no':
		x=get_contact_no()
		return x
	elif resp['entities']['intent'][0]['value']=='get_affiliations':
		x=get_affiliations()
		return x
	elif resp['entities']['intent'][0]['value']=='get_timing_year':
		year=resp['entities']['year'][0]['value']
		x=get_timing_year(year)
		return x
	elif resp['entities']['intent'][0]['value']=='get_timing_shift':
		year=resp['entities']['year'][0]['value']
		x=get_timing_shift(year)
		return x
	elif resp['entities']['intent'][0]['value']=='give_facility':
		group=resp['entities']['group'][0]['value']
		x=give_facility(group)
		return x
	elif resp['entities']['intent'][0]['value']=='get_info_acropolis':
		type=resp['entities']['type'][0]['value']
		x=get_info_acropolis(type)
		return x
	elif resp['entities']['intent'][0]['value']=='get_seats':
		branch=resp['entities']['branch'][0]['value']
		x=get_seats(branch)
		return x
	elif resp['entities']['intent'][0]['value']=='get_eligibility':
		branch=resp['entities']['branch'][0]['value']
		x=get_eligibilty(branch)
		return x
	elif resp['entities']['intent'][0]['value']=='get_timing_library':
		x=get_library_timing()
		return x
	elif resp['entities']['intent'][0]['value']=='get_timing_year_library':
		year=resp['entities']['year'][0]['value']
		x=get_timing_year_library(year)
		return x
	elif resp['entities']['intent'][0]['value']=='formal_greeting_question':
		return "I am fine"
	elif resp['entities']['intent'][0]['value']=='get_timing':
		x=get_timing()
		return x
	elif resp['entities']['intent'][0]['value']=='formal_greeting':
		return "hello"
	elif resp['entities']['intent'][0]['value']=='get_list_hod':
		x=get_list_hod()
		return x
	elif resp['entities']['intent'][0]['value']=='get_list_management':
		x=get_list_management()
		return x
	elif resp['entities']['intent'][0]['value']=='get_list_faculties':
		x=get_list_faculties()
		return x
	elif resp['entities']['intent'][0]['value']=='get_qualification':
		firstName=resp['entities']['firstName'][0]['value']
		lastName=resp['entities']['lastName'][0]['value']
		x=get_qualification(firstName,lastName)
		return x
	elif resp['entities']['intent'][0]['value']=='get_company':
		x=get_company()
		return x
	elif resp['entities']['intent'][0]['value']=='get_vision_department':
		branch=resp['entities']['branch'][0]['value']
		x=get_vision_department(branch)
		return x;
	elif resp['entities']['intent'][0]['value']=='get_mission_department':
		branch=resp['entities']['branch'][0]['value']
		x=get_mission_department(branch)
		print(x)
		return x;
	elif resp['entities']['intent'][0]['value']=='get_list_cells':
		x="1)CSI Student Branch"+"\n"+"2)Research & Consultancy"+"\n"+"3)Entrepreneurship Cell"+"\n"+"4)IIPC Industry Academia"+"\n"+"5)TSDC"+"\n"+"6)IPPC"+"\n"+"7)T&D"+"\n"+"8)Yavnika Hobby Club"+"\n"+"9)Women Cell"+"\n"+"10)NABL Accredited Civil Laboratory"
		return x
	elif resp['entities']['intent'][0]['value']=='get_contact_people':
		firstName=resp['entities']['firstName'][0]['value']
		lastName=resp['entities']['lastName'][0]['value']
		x=get_contact_people(firstName,lastName)
		return x
	elif resp['entities']['intent'][0]['value']=='get_placement_year':
		y=resp['entities']['year'][0]['value']
		x=get_placement_year(y)
		return x
	elif resp['entities']['intent'][0]['value']=='get_email':
		firstName=resp['entities']['firstName'][0]['value']
		lastName=resp['entities']['lastName'][0]['value']
		x=get_email(firstName,lastName)
		return x
	elif resp['entities']['intent'][0]['value']=='get_placement_company':
		y=resp['entities']['year'][0]['value']
		c=resp['entities']['company'][0]['value']
		x=get_placement_company(y,c)
		return x
	elif resp['entities']['intent'][0]['value']=='get_company_list':
		b=resp['entities']['branch'][0]['value']
		x=get_company_list(b)
		return x
	elif resp['entities']['intent'][0]['value']=='get_placement_branch':
		b=resp['entities']['branch'][0]['value']
		if not "year" in resp['entities']:
			y=2019
		else:
			y=resp['entities']['year'][0]['value']
		x=get_placement_branch(b,y)
		return x
	elif resp['entities']['intent'][0]['value']=='get_courses':
		return "BE in CS"+"\n"+"BE in ME"+"\n"+"BE in EC"+"\n"+"BE in IT"+"\n"+"BE in EC"
app = Flask(__name__)
@app.route('/',defaults={'path':''})
@app.route('/<path:path>')
def catch_all(path):
	print(path)
	if "bye" in path:
		return "bye bye"
	if "good bye" in path:
		return "bye bye"
	if "Good bye" in path:
		return "bye"
	if "good morning" in path:
		return "hello good afternoon"
	if "good evening" in path:
		return "hello afternoon"
	if "good afternoon" in path:
		return "hello good afternoon"
	if "good night" in path:
		return "hello good afternoon" 
	if "Good morning" in path:
		return "hello good afternoon"
	if "Good evening" in path:
		return "hello good afternoon"
	if "Good Afternoon" in path:
		return "hello good afternoon"
	if "Good night" in path:
		return "hello afternoon"
	if "Good Morning" in path:
		return "hello good afternoon"
	if "Good Evening" in path:
		return "hello good afternoon"
	if "Good Night" in path:
		return "hello good afternoon"
	if "Good afternoon" in path:
		return "hello good afternoon"
	else:
		x=process(path)
		print(x)
		print(x)
		return x

if __name__ == '__main__':
    app.run()		