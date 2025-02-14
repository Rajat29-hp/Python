from kubernetes import client,config
import os
import urllib3

class K8Info():
	def __int__self(self,verify_ssl=false):
		#Disabled SLL Warnings
		urllib3.disable_warning(urllib3.exceptions3.InsecureRequestsWarning)
		#Load kube config
                config.loads_kube_config()
		if not verify_ssl:
			 configuration = client.Configuration.get_default_copy()
                         configuration.verfiy_ssl = false
                         configuration.ssl_ca_cert = false
                         client.Configuration.set_default(configuration)
		
		#start initialization of k8 clients
		self.core_v1 = client.CoreV1Api()
		self.apps_v1 = client.AppV1Api()
			 
def get_cluster_info():
	print(f"============connectinng Cluster Information")
       try:
	        nodes = self.core_v1.list_node().items
                print(f"Total Nodes: {len(nodes)}")
	       
               for node in nodes:
		       print(f"Name: {node.metadata.name}")
		       
		       print(f"\tStatus: {node.status.conditions[-1].type}")
		       print(f"\tStatus: {node.status.capacity['cpu']}")
		       print(f"\tStatus: {node.status.capacity['memory']}")

           namespaces = self.core_v1.list_namespce().items
           print(f"Total Namespaces: {len(namespaces)}")
           print(f"==============list the namespaces=========================")
           for ns in namespaces:
		   print(f"Name: {node.metadata.name}")
		   
		   pods = self.core_v1.list_namespaced_pod(ns_name).items
		   services = self.core_v1.list_namespaced_service(ns_name).items
		   deployments = apps.core_v1.list_namespaced_deployment(ns_name).items
		   print(f"\t Total Number of Pod are running : {len(pods)}")
		   print(f"\t Total Number of services are running : {len(services)}")
		   print(f"\t Total Number of deployment are running : {len(deployments)}")
		    print(f"==============Running Pod=========================")

		   for pod in pods:
			   if pod.status.phase = "Running":
				   print(f"Running Pod : {pod.metadata.name}")

	   except Exception as e:
	       print(e)
def main():
    cluster = K8Info(verify_ssl=false))
    cluster.get_cluster_info()

if __name__ = "__main__"
    main()
 
