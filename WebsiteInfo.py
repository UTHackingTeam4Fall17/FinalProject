class WebsiteInfo:

    def __init__(self, website_name, ip_address, service_mode, address_and_details, port):
        self.website_name = website_name
        self.ip_address = ip_address
        self.service_mode = service_mode
        self.address_and_details = address_and_details
        self.port = port

    def get_attack_info(self):
        return self.ip_address, self.service_mode, self.address_and_details, self.port


def get_all_websites():
    
