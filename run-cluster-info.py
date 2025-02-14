from kubernetes-connect import K8Info

def main():
    mycluster = K8Info(verify_ssl=false)
    mycluster.get_cluster_info()

if __name__ = "__main__"
    main()
