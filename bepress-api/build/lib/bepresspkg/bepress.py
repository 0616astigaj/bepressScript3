import requests
import csv
import json

pubYear = "2019"
limit = "1000"
type = "thesis"

url = 'https://content-out.bepress.com/v2/epublications.marquette.edu/query?document_type="' + type + '"&publication_year=' + pubYear + '&limit=' + limit

headers = {
    'async':'true',
    'Authorization': 'EOFeFwNE1ZtlGZXMHETLNqBIu2jrXYSTlaq8jXmem3M=',
    'Access-Control-Allow-Origin' : '*'
}

response = requests.get(url, headers=headers)

data = response.json()
cleanData = []
with open('cleanData.json', 'w') as json_file:
  for i in data["results"]:
    documentTypes = data["results"][data["results"].index(i)]["document_type"]
    for j in documentTypes:
      if type == "thesis":
        if j == "thesis" or j == "Thesis" or j == "Theses" or j == "Thesis - Restricted" or j == "Theses - Restricted":
          cleanData.append(i)
          break
      elif type == "dissertation":
        if j == "dissertation" or j == "Dissertation" or j == "Dissertations" or j == "Dissertation - Restricted":
          cleanData.append(i)
          break
    

  json.dump(cleanData, json_file)

#with open('dirtydata.json', 'w') as json_file:
  #json.dump(data, json_file)