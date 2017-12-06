import requests

IP = '127.0.0.1'
PORT = '8080'
PATH = 'users'
QUERY_STRING = 'name={}'

def has_name(name):
    query = QUERY_STRING.format(name)
    path = 'http://{}:{}/{}?{}'.format(IP, PORT, PATH, query)
    resp = requests.head(path)
    return resp.status_code == 200

def main():
    print(has_name('arnav'))

if __name__ == '__main__':
    main()
