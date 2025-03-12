from OpenSSL import crypto
import configparser


config = configparser.ConfigParser()
config.read('pkcs12_config.ini')

# load PKCS#12 file
with open("cert.p12", "rb") as f:
    p12_data = f.read()

password = config.get('dev', 'pkcs12_password')
p12 = crypto.load_pkcs12(p12_data, password.encode('utf-8'))

private_key = p12.get_privatekey()
cert = p12.get_certificate()
ca_cert = p12.get_ca_certificates()

