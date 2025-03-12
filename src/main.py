import kubernetes_connector as kube


def kubernetes_example():
    creds = kube.load_tls_cert()

    print(f"Kube cert file value: {creds.cert_file}")
    print(f"Kube key file value: {creds.key_file}")



def main():
    kubernetes_example()


    print("Found it!")



if __name__ == "__main__":
    main()