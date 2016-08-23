from django.core.management.base import BaseCommand
from appRT.models import Post
from bs4 import BeautifulSoup
import requests
import json

class Command(BaseCommand):
	requires_model_validation = False
	can_import_settings = True
	
	def handle(self, *model_labels, **options):
		raw_data = requests.get("https://www.rottentomatoes.com/browse/opening") #dohvacanje html-a sa inicijalne stranice
		response_content = raw_data.content  
		soup = BeautifulSoup(response_content, 'html.parser')
		data_string=soup.find(id="jsonLdSchema").string #izdvajanje potrebnog sadrzaja
		data_json = json.loads(data_string)
		count=0
		for x in range(0, len(data_json['itemListElement'])):	
			raw_data_details = requests.get("https://www.rottentomatoes.com"+data_json['itemListElement'][x]['url']) #dohvat detalja filma sa njegove stranice
			response_content = raw_data_details.content 
			soup = BeautifulSoup(response_content, 'html.parser')
			data_string=soup.find(id="jsonLdSchema").string #izdvajanje potrebnog sadrzaja
			data_json_details = json.loads(data_string)
			
			
			def checkProdCompany(jsonContents): #Neki filmovi nemaju navedene sve informacije pa radim checkove 
				retValue = jsonContents['productionCompany']['name'] if "name" in jsonContents['productionCompany'] else "-"
				return retValue
			def checkDescription(jsonContents): 
				retValue = jsonContents['description'] if "description" in jsonContents else "-"
				return retValue
			def checkDirector(jsonContents):  #Nisam nasao bolje rjesenje za director i author koji su na nekim filmovima skroz prazni, a na nekima djelomicno
				if jsonContents['director']:
					retValue = jsonContents['director'][0]['name'] if "name" in jsonContents['director'][0] else "-"
					return retValue
				else: 
					return "-"
			def checkAuthor(jsonContents):
				if jsonContents['author']:
					retValue = jsonContents['author'][0]['name'] if "name" in jsonContents['author'][0] else "-"
					return retValue
				else: 
					return "-"
			def checkRating(jsonContents):
				retValue = jsonContents['aggregateRating']['ratingValue'] if "ratingValue" in jsonContents['aggregateRating'] else "-"
				return retValue


			
			b = Post(position=data_json['itemListElement'][x]['position'], name=data_json_details['name'], description=checkDescription(data_json_details), image=data_json_details['image']['url'], productionCompany=checkProdCompany(data_json_details), genre=data_json_details['genre'], director=checkDirector(data_json_details), author=checkAuthor(data_json_details), rating=checkRating(data_json_details))
			b.save() # spremi u bazu
			count += 1
			print "Importing movie %d/%d" % (count,len(data_json['itemListElement']))