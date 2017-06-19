import csv
import urllib2, requests
import   tempfile, subprocess, base64, time

url = 'http://www.vpngate.net/api/iphone/'

res = urllib2.urlopen(url)

cr = csv.reader(res)



i = []
for row in cr:
    #print(row)

    
    server = []
    for an in row :
        
        if 'Japan' in an :
              
              server.append(row[0])
              server.append(row[1])
              server.append(row[5])
              server.append(row[14])
##            print "DDNS Hostname :" ,row[0]
##            print "IP Address : " ,row[1]
##            print "Score :" ,row[2]
##            print "Country: ", row[5]
##            print "Pings: ", row[4]
##            print "Speed: " , row[3]
##            print "VPN session: " ,row[7]
##            print "Total Users: ", row[9]
##            print "Logging Policy: ", row[11]
##            print "Owner: ", row[12]
##            print "CA ---------------------------"
##            print row[14]
##            print "-----------------------------END"
##            print "\n\n"
              #print server
    if server != []:
        i.append(server)



#print i[1] 

winner = i[1]
#print winner

_, path = tempfile.mkstemp()

print path

f = open(path, 'w')
f.write(base64.b64decode(winner[-1]))
#f.write('\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf')
f.close()
