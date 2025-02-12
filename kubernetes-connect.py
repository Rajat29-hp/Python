import os
import urllib3

class K8Info():
		def__inn__self(self,verify_ssl=false):
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