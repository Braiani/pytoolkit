import ssl
import socket
from datetime import datetime
import argparse


class Certificates:
    def __init__(self, hostname):
        self.hostname = hostname

    def get_certificate_expiry_date(self):
        context = ssl.create_default_context()
        with socket.create_connection((self.hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                cert = ssock.getpeercert()
                expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                return expiry_date

    def check_certificate_expiry(self):
        expiry_date = self.get_certificate_expiry_date()
        current_date = datetime.now()
        days_to_expiry = (expiry_date - current_date).days
        return days_to_expiry
    
    def get_certificate_details(self):
        try:
            days_to_expiry = self.check_certificate_expiry()
            print(f"The certificate for {self.hostname} expires in {days_to_expiry} days.")
        except:
            print(f"Ocorreu um erro ao tentar recuperar informações do site: {self.hostname}")


if __name__ == '__main__':
    # get hostname from argument
    parser = argparse.ArgumentParser(description='Get certificate details')
    parser.add_argument('hostname', help='Hostname to get certificate details')

    args = parser.parse_args()
    hostname = args.hostname
    
    cert = Certificates(hostname)
    cert.get_certificate_details()