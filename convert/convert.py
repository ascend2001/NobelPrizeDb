import json

# load data
data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))

PNp= open('PersonName.del','w')
ONp= open('OrgName.del','w')
nobelPrizes=open('NobelPrize.del','w')
affiliations=open('Affiliations.del','w')

PNp_array=[]
ONp_array=[]
nobelPrizes_array=[]
affiliations_array=[]


for laureate in data["laureates"]:

    id=laureate["id"]
    placeAndDate="\\N"
    city="\\N"
    country="\\N"
    date="\\N"
    givenName="\\N"
    famName="\\N"
    gender="\\N"

    if "gender" in laureate:
        gender=laureate["gender"]

    if "givenName" in laureate:
        givenName = laureate["givenName"]["en"]

    if "familyName" in laureate:
        famName = laureate["familyName"]["en"]
    if ("familyName" in laureate) or ("givenName" in laureate) or ("gender" in laureate):
        if "birth" in laureate:
            placeAndDate=laureate["birth"]
            if "date" in placeAndDate:
                date=placeAndDate["date"]
            if "place" in placeAndDate:
                if "city" in placeAndDate["place"]:
                    city=placeAndDate["place"]["city"]["en"]
                if "country" in placeAndDate["place"]:
                    country=placeAndDate["place"]["country"]["en"]
        PNp_value=id+","+"\""+givenName+"\""+","+"\""+famName+"\""+","+"\""+date+"\""+","+"\""+gender+"\""+","+"\""+city+"\""+","+"\""+country+"\""+'\n'
        if PNp_value not in PNp_array:
            PNp.write(PNp_value)
            PNp_array.append(PNp_value)

    placeAndDate="\\N"
    orgName="\\N"
    city="\\N"
    country="\\N"
    if "orgName" in laureate:
        orgName=laureate["orgName"]["en"]
        if "founded" in laureate:
            placeAndDate=laureate["founded"]
            if "date" in placeAndDate:
                date=placeAndDate["date"]
            if "place" in placeAndDate:
                if "city" in placeAndDate["place"]:
                    city=(placeAndDate["place"]["city"]["en"])
                if "country" in placeAndDate["place"]:
                    country=(placeAndDate["place"]["country"]["en"])
        ONp_value=id+","+"\""+orgName+"\""+","+"\""+date+"\""+","+"\""+city+"\""+","+"\""+country+"\""+'\n'
        if ONp_value not in ONp_array:
            ONp.write(ONp_value)
            ONp_array.append(ONp_value)


    if "nobelPrizes" in laureate:        
        for prize in laureate["nobelPrizes"]:
            awardYear="\\N"
            category="\\N"
            sortOrder="\\N"
            if "awardYear" in prize:
                awardYear=prize["awardYear"]
            if "category" in prize:
                category=prize["category"]["en"]
            if "sortOrder" in prize:
                sortOrder=prize["sortOrder"]
            if "affiliations" in prize:
                for affiliate in prize["affiliations"]:
                    affiliation_name="\\N"
                    affiliation_city="\\N"
                    affiliation_country="\\N"
                    if "city" in affiliate:
                        affiliation_city=affiliate["city"]["en"]
                    if "country" in affiliate:
                        affiliation_country=affiliate["country"]["en"]
                    if "name" in affiliate:
                        affiliation_name=affiliate["name"]["en"]
                    affiliations_value="\""+affiliation_name+"\""+","+"\""+affiliation_city+"\""+","+"\""+affiliation_country+"\""+","+"\""+awardYear+"\""+","+"\""+category+"\""+","+"\""+sortOrder+"\""+","+"\""+id+"\""+'\n'
                    if affiliations_value not in affiliations_array:
                        affiliations.write(affiliations_value)
                        affiliations_array.append(affiliations_value)
            nobelPrizes_value="\""+awardYear+"\""+","+"\""+category+"\""+","+"\""+sortOrder+"\""+","+id+'\n'
            if nobelPrizes_value not in nobelPrizes_array:
                nobelPrizes.write(nobelPrizes_value)
                nobelPrizes_array.append(nobelPrizes_value)


nobelPrizes.close()
affiliations.close()
PNp.close()
ONp.close()