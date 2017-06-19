import csv
import urllib2, requests
import   tempfile, subprocess, base64, time

print """

   _,gggggg,_                                           ,gg,                                   
 ,d8P""d8P"Y8b,                                        i8""8i                    I8            
,d8'   Y8   "8b,dP                                     `8,,8'                    I8            
d8'    `Ybaaad88P'                                      `Y88aaad8             88888888         
8P       `""""Y8                                         d8""""Y8,               I8            
8b            d8  gg,gggg,     ,ggg,    ,ggg,,ggg,      ,8P     8b   ,gggg,gg    I8     ,ggg,  
Y8,          ,8P  I8P"  "Yb   i8" "8i  ,8" "8P" "8,     dP      Y8  dP"  "Y8I    I8    i8" "8i 
`Y8,        ,8P'  I8'    ,8i  I8, ,8I  I8   8I   8I _ ,dP'      I8 i8'    ,8I   ,I8,   I8, ,8I 
 `Y8b,,__,,d8P'  ,I8 _  ,d8'  `YbadP' ,dP   8I   Yb,"888,,_____,dP,d8,   ,d8b, ,d88b,  `YbadP' 
   `"Y8888P"'    PI8 YY88888P888P"Y8888P'   8I   `Y8a8P"Y888888P" P"Y8888P"`Y888P""Y88888P"Y888
                  I8                                                                           
                  I8                                                                           
                  I8                                                                           
                  I8                                                                           
                  I8                                                                           
                  I8                                                                           


"""


url = 'http://www.vpngate.net/api/iphone/'

res = urllib2.urlopen(url)

cr = csv.reader(res)


country = raw_input("Enter a country : \n")

# List of the servers
servers_list = []

for row in cr:
    #print(row)

    
    server = []
    for an in row :
        
        if  country in an :
              
              server.append(row[0])
              server.append(row[1])
              server.append(row[5])
              #server.append(row[14])
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
        servers_list.append(server)


# List all of the servers and let the user chooses the server
#user = int(raw_input(">>>: "))
for server in servers_list :

   # List all servers for the user
   print server


# Ask the user to select a serevr
user_input = raw_input("Enter VPN IP address: \n")
for ip in servers_list :
    
    if user_input in ip :
        
        print 
        print "[+] VPN SELECTED ", ip
    else:
        pass



##winner = i[1]
###print winner
##
##_, path = tempfile.mkstemp()
##
##print path
##
##f = open(path, 'w')
##f.write(base64.b64decode(winner[-1]))
###f.write('\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf')
##f.close()
