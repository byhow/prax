import requests
from bs4 import BeautifulSoup 
url = 'https://tns4lpgmziiypnxxzel5ss5nyu0nftol.lambda-url.us-east-1.on.aws/challenge'
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

print(''.join([node.get('value') for node in soup.select('ul[data-tag*="75"] li[data-id^="98"] div[data-class*="35"] span.value')]))
