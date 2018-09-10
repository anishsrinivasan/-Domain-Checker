
# importing the requests library 
import requests 
import datetime
text_file = open("domainnames.txt", "r")
writeFileName = "Available Domains - "+datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"
write_file = open(writeFileName,"w+")
write_file.write(writeFileName+' \n \n')
domains = text_file.read().splitlines()

# api-endpoint 
URL = "https://api.godaddy.com/v1/domains/available"
print('\n Available Domains \n');
for domain1 in domains:
    for domain2 in domains:
        if(domain1 != domain2):
            domain = domain1+domain2
            PARAMS = {'domain':domain+'.com','checkType':'FAST'}
            r = requests.get(url = URL, params = PARAMS, headers={"Authorization": "sso-key key:secretkey"}) 
            data = r.json()
            if(data["available"]):
               currency = str(data["price"])
                currency = currency[:-6]
                currency = int(currency)*72
                write_file.write(domain+'.com - Rs.'+str(currency)+' \n')
                print(domain+'.com - Rs.'+str(currency)+' \n')
write_file.close()
