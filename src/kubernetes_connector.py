from kubernetes import config, client
import yaml

with open("kube_config.yaml", 'r') as stream:
    local_config = yaml.safe_load(stream)

def load_tls_cert():
    kube_config = client.Configuration()
    kube_config.host = "kubernetes_api_server_address"
    kube_config.ssl_ca_cert = "/path/to/ca.crt"
    kube_config.cert_file = local_config.get('data')['tls.crt']
    kube_config.key_file = local_config.get('data')['tls.key']

    return kube_config