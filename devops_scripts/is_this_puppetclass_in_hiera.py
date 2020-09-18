import requests, warnings
from getpass import getpass

#global parameters
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)

def _get_hosts(foreman_login,foreman_password,puppet_class,envir='prod'):
    hosts = []
    for _class in puppet_class:
        base_url = 'https:///api/v2/hosts?search=environment+%3D+{}+and+class+%3D+{}'.format(envir,_class)
        foreman_reply = requests.get(base_url, auth=(foreman_login,foreman_password), params={'page': 1, 'per_page': 250}, verify=False)
        if foreman_reply.status_code == 200:
            foreman_json = foreman_reply.json()
            if len(foreman_json['results']) == 0:
                print('Error during the process ({})'.format(_class))
                exit
            else:
                for host in foreman_json['results']:
                    hosts.append(host['name'])
    return set(hosts)

def get_raw(host,envir='prod'):
    base_url='https:///hiera/{}/raw/master/hiera/fqdn'.format(envir)
    token = ''
    new_url = '{}/{}.yaml?private_token={}'.format(base_url,host,token)
    raw_data = requests.get(new_url, verify=False)
    return raw_data.text

if __name__ == "__main__":
    class_to_lookup = ['postgres_ingenico::pg95','psql_ingenico']
    scope = 'prod'
    login = ''
    print('Please enter the password (login: {}): '.format(login))
    password = getpass()
    counter = 0
    for host in _get_hosts(login,password,class_to_lookup,scope):
        for _class in class_to_lookup:
            if _class in get_raw(host,scope):
                counter += 1
                print('host ({}) has been detected! (fqdn: {}, class: {})'.format(counter,host,_class))
    if counter == 0:
        print('{} hosts found'.format(counter))
