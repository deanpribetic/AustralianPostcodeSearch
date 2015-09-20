import httplib
import urllib
import json

connection = httplib.HTTPSConnection('auspost.com.au', 443, timeout = 30)
headers = {AUTH-KEY-GOES-HERE}
suburb = raw_input('Enter a suburb: ')
urlSuburb = urllib.quote(suburb.upper())
urlString = '/api/postcode/search.json?q=' + urlSuburb
connection.request('GET', urlString, None, headers)

try:
	response = connection.getresponse()
	content = response.read()
	resultDict = json.loads(content)
	localitiesDict = resultDict.get('localities')
	localityList = localitiesDict.get('locality')

	postcodes = ''
	if isinstance(localityList,dict):
		postcodes = localityList.get('location')+ ', ' + localityList.get('state') + ': ' + str(localityList.get('postcode'))
	else:
		for item in localityList:
			postcodes = postcodes + item.get('location')+ ', ' + item.get('state') + ': ' + str(item.get('postcode')) + '\n'
	print(postcodes.strip())	

except httplib.HTTPException, e:
	print('Exception during request')
