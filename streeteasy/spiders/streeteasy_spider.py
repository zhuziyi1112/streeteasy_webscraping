# -*- coding: utf-8 -*-
from scrapy import Spider
from streeteasy.items import StreeteasyItem


class StreetesaySpider(Spider):
	name = 'streeteasy_spider'
	allowed_urls = ['https://streeteasy.com']
	start_urls = []
	handle_httpstatus_list = [403]

	for i in range(1,1649):
		start_urls.append('https://streeteasy.com/for-rent/nyc?page='+str(i))

	for i in range(1,1699):
		start_urls.append('https://streeteasy.com/for-sale/nyc?page='+str(i))

	def parse(self, response):
		# Find all the table rows
		# rows = response.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr')
		rows = response.xpath('//*[@class="left-two-thirds items item-rows listings u-overflow--unset jsListingsItems jsSearchResults"]/ul/li')
		#print(response.xpath('//*[@class="left-two-thirds items item-rows listings u-overflow--unset jsListingsItems jsSearchResults"]/ul/li/div/div[2]/div[1]/div/span/text()').extract_first())
		# The movie title could be of different styles so we need to provide all the possibilities.
		# patterns = ['./td[1]/i/a/text()', './td[1]/i/b/a/text()', './td[1]/i/span[2]//text()', './td[1]/i/b/span/text()']
		for row in rows[1:]:
	        # extract() will return a Python list, extract_first() will return the first element in the list
			# If you know the first element is what you want, you can use extract_first()
			# for pattern in patterns:
				# film = row.xpath(pattern).extract_first()
				# if film:
					# break
			# If the movie title is missing, then we just skip it.
			# if not film:
				# continue
			# Relative xpath for all the other columns

			# rows = response.xpath('//*[@class="left-two-thirds items item-rows listings u-overflow--unset js ListingsItems jsSearchResults"]/ul/li[1]/div/div[2]/div[1]/p/text()').extract_first()
			price = row.xpath('./div/div[2]/div[1]/div/span/text()').extract_first()
			bed = row.xpath('./div/div[2]/div[2]/div/div/div[1]/span/text()').extract_first()
			bath = row.xpath('./div/div[2]/div[2]/div/div/div[3]/span/text()').extract_first()
			listing = row.xpath('./div/div[2]/div[2]/p/text()').extract_first().replace("\n","").strip()
			

			Description = row.xpath('./div/div[2]/div[1]/p/text()').extract_first().replace("\n","").strip()
			print(Description)
			if 'in' in Description:
				RentalType = Description.split(' in ')[0]
				neighborhood = Description.split(' in ')[1]
			else:
				Description1 = row.xpath('./div/div[2]/div[1]/p[2]/text()').extract_first().replace("\n","").strip()
				RentalType = Description+" "+ Description1.split(' in ')[0]
				neighborhood = Description1.split(' in ')[1]
			
			fee = row.xpath('./div/div[2]/div[1]/div/div/span/text()').extract_first()
			if fee=="No Fee" or fee==None:
				fee=fee
			else:
				fee = row.xpath('./div/div[2]/div[1]/div/div[2]/span/text()').extract_first()
			size = row.xpath('./div/div[2]/div[2]/div/div/div[5]/span/text()').extract_first()
			if size==None:
				size=""
			else:
				size=size.replace("\n","").strip()

			#film = row.xpath('./td[1]//text()').extract_first()
			#year = int(row.xpath('./td[2]/a/text()').extract_first())
			# try:
			# 	awards = int(row.xpath('./td[3]/text()').extract_first())
			# except:
			# 	awards = row.xpath('./td[3]/text()').extract_first()
			# 	awards = int(re.findall('\d+',awards)[0])

			# nominations = int(row.xpath('./td[4]/text()').extract_first().strip())
			# is_bestpicture = bool(row.xpath('./@style').extract_first())

			# Initialize a new WikiItem instance for each movie.
			item = StreeteasyItem()
			item['price'] = price
			item['bed'] = bed
			item['bath'] = bath
			item['listing'] = listing
			item['RentalType'] = RentalType
			item['neighborhood'] = neighborhood
			item['fee'] = fee
			item['size'] = size
			yield item