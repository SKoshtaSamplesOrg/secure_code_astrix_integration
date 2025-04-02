import kubernetes_connector as kube
import configparser

from src.db_connector import load_toml_config
from src.pkcs12_manager import load_pkcs12_cert

config = configparser.ConfigParser()
config.read('pkcs12_config.ini')

def kubernetes_example():
    creds = kube.load_tls_cert()

    print(f"Kube cert file value: {creds.cert_file}")
    print(f"Kube key file value: {creds.key_file}")

def pkcs12_example():
    p12_filepath = 'certs/certificate.p12'
    password = config.get('dev', 'pkcs12_password')

    cert_data = load_pkcs12_cert(p12_filepath, password)
    print(f"PKCS12 cert data: {cert_data}, password: {password}")

def toml_example():
    sf_config = load_toml_config()
    print(f"TOML data: {sf_config}")


def main():
    kubernetes_example()
    pkcs12_example()
    toml_example()

    print("Found it!")



if __name__ == "__main__":
    main()