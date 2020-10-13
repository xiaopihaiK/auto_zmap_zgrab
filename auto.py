import time
import os

# port = [8083,8084,8085,7003,7004]

port = [8086,8087,8089,8091]

# port = [80]

all_filename = []

all_json = []

for i in port:
	filename = str(i)+'.txt'
	all_filename.append(filename)
	command = 'zmap -B 1000M -p '+str(i)+' -o '+str(i)+'.txt'
	# print command
	# print filename
	# print command
	os.system(command)

# time.sleep(10)

for i in all_filename:
	end_file_port = i.split('.')[0]
	end_file_port_json = end_file_port+'.json'
	all_json.append(end_file_port_json)
	command = '/usr/local/go/bin/src/github.com/zmap/zgrab2/zgrab2 http --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36" --max-size=1024 --timeout 2 --senders 1000 -f '+str(i)+' -o '+str(end_file_port)+'.json '+'-p '+str(end_file_port)
	print command
	os.system(str(command))
# print all_json

# os.system('zmap -B 1000M -p 8083 -o 8083.txt')

# time.sleep(10)


#os.system('zgrab http -p 7001 --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36" -f /root/7001.csv.txt -o 7001.json  --timeout 2 --senders 800')



# f = open('8083.txt','r')

# fp = open('8083_1.txt','a')

# for i in f.readlines():
# 	x = i.strip('\n')
# 	if 'time' in x:
# 		pass
# 	else:
# 		ip = x.split(',')[1]
# 		fp.write('%s\n'%str(ip))

# time.sleep(10)

# zgrab http -p 7001 
# --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36" 
# -f /root/7001.csv.txt -o 7001.json  --timeout 2 --senders 800
