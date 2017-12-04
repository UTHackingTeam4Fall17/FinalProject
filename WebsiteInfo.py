class WebsiteInfo:

    def __init__(self, website_name, ip_address, service_mode, address_and_details, port):
        self.website_name = website_name
        self.ip_address = ip_address
        self.service_mode = service_mode
        self.address_and_details = address_and_details
        self.port = port

    def get_attack_info(self):
        return self.ip_address, self.port, self.service_mode, self.address_and_details

    def __str__(self):
        return '{} -- {}:{} {}, {}'.format(self.website_name, self.ip_address, self.port, self.address_and_details, self.service_mode)

    def __repr__(self):
        return str(self)

from os import listdir
websites_dir = 'website_info/'
def get_all_websites():
    websites = {}

    files = listdir(websites_dir)
    for website_name in files:
        with open(websites_dir + website_name) as f:
            name = f.readline().rstrip()
            ip_addr = f.readline().rstrip()
            port = f.readline().rstrip()
            service_mode = f.readline().rstrip()
            address_and_details = f.readline().strip()
            
            websites[website_name] = WebsiteInfo(name, ip_addr, service_mode, address_and_details, port)

    return websites

if __name__ == '__main__':
    websites = get_all_websites()
    for k, v in websites.items():
        print(v)
