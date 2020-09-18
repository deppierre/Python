#executer depuis icingamaster01fe.dc1.vl99.fr.its
#param /tmp/import_icinga svc-oracle-axis_stg_w4s

import sys, getopt, re
import requests, urllib3
import time, datetime

#global parameters
base_url = ''
user = 'root'
password = ''
nb_days = 2
urllib3.disable_warnings()

#function to get service for a host
def get_service(host):
	headers = { 'Accept':'application/json','X-HTTP-Method-Override':'GET' }
	url = base_url + '/objects/services?attrs=name&attrs=state&filter=host.name==%22{0}%22'.format(host)
	result = requests.get(url, headers=headers, auth=(user,password), verify=False)
	if result.status_code != 200 or result.json()['results'] == []:
		print('error: Icinga API, no data fetched')
		sys.exit()
	else: return result.json()

#collect hosts in the user file
arguments = sys.argv
try:
	scriptName, file_name = arguments
        try:
                with open(file_name) as input_file:
			hosts = dict(( host.strip().rstrip('\n'),[] ) for host in input_file.readlines() if re.search('(?:fr.its|ingenico.com|servicegroup)$',host.strip()))
			print('info: {0} hosts detected in the file ({1})'.format(len(hosts),file_name))
        except IOError:
                print('error: file unavailable ({0})'.format(file_name))
                sys.exit(2)
except ValueError:
	print('help: {0} /path/to/the/host/name/file'.format(arguments[0]))
        sys.exit(2)

#service collection (error state filtering)
[ hosts[host].append(service['attrs']['name']) for host in hosts for service in get_service(host)['results'] if service['attrs']['state'] == 2.0 ]

#user service decision
UserServiceIndex = check_ticket = None

#list unique (set) services
services = list( set( service for host in hosts for service in hosts[host] ))
exitIndex = len(services) + 1
if services:
	print('What service would you like to acknowledge? (1,2,...) :')
	for index, service in enumerate(services):
		print('\t{0}) {1}'.format(index + 1, service))
	print('\t{0}) exit'.format(exitIndex))

	#loop while user input not in the range
	while UserServiceIndex not in range(exitIndex + 1): 
		UserServiceIndex = raw_input('choice: ')
		if not UserServiceIndex: sys.exit()
		else: UserServiceIndex = int(UserServiceIndex)

	#exit option
	if UserServiceIndex == exitIndex: sys.exit()

	#get the service associated with the index
	UserService = services[UserServiceIndex - 1]
	UserHostsAffected = [ host for host in hosts for service in hosts[host] if UserService == service ]
else:
	print('warning: 0 service in error for these hosts')
	sys.exit(2)

#ticket number
while check_ticket is None:
	UserTicketNumber = raw_input('your ticket number (ex: SYS-1234): ')
	check_ticket = re.search(r'-[0-9]{4}$',UserTicketNumber)

#acknowledge recap + confirmation
print('\n' + '-' * 50)
UserConfirmation = raw_input('recap: you are about to acknowledge: \n\t- the service {0}, \n\t- for {1} server(s), \n\t- for {2} day(s), \nare you sure? (y/n) '.format(UserService, len(UserHostsAffected), nb_days ))
if UserConfirmation.lower() != 'y': sys.exit()

#acknowledge process
print('\n' + '-' * 50)
print('acknowledge process result:')
for host in hosts:
	if host in UserHostsAffected:
		end_date = ((datetime.date.today() + datetime.timedelta(days=nb_days)).timetuple())
		headers = { 'Accept':'application/json','X':'POST' }
		url = base_url + '/actions/acknowledge-problem?service={0}!{1}&author={2}&comment={3}&expiry={4}'.format(host,UserService,'mcs',UserTicketNumber.upper(),time.mktime(end_date))
		result = requests.post(url, headers=headers, auth=(user,password), verify=False)
		result_json = result.json()

		if result.status_code != 200 and result.json()['results'] == []: print('\t - error: host not acknowledged: {0}, details: {1}'.format(host, result.text))
		else: print('\t x success: host acknowledged: {0}'.format(host))
	else: print('\t - warning: host rejected: {0}'.format(host))

