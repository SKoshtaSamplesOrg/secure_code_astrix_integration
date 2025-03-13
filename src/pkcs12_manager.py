from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import pkcs12


# load PKCS#12 file
def load_pkcs12_cert(p12_filepath, password):
    try:
        with open(p12_filepath, "rb") as f:
            p12_data = f.read()
        private_key, cert, additional_certs = pkcs12.load_key_and_certificates(
            p12_data, password.encode('utf-8')
        )
        print(f"Private key: {private_key}, Cert: {cert}, Additional Details: {additional_certs}")
        if cert:
            return cert.public_bytes(serialization.Encoding.PEM)
        else:
            return None
    except Exception as e:
        print(f'Error loading PKCS12 cert: {e}')
        return None
