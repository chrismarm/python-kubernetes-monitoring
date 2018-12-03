from kubernetes import client, config, watch
from google.auth import compute_engine
from google.cloud.container_v1 import ClusterManagerClient
from google.oauth2 import service_account
import os
import time
import threading

PROJECT_ID=os.environ.get('K8S_PROJECT', 'tonal-justice-216711')
ZONE=os.environ.get('K8S_ZONE', 'europe-west1-b')

def main():
    ''' Default credentials based on local kubeconfig to manage cluster through K8S client '''
    config.load_kube_config()
    k8s_api = KubernetesAPIClient(client.CoreV1Api())
    
    ''' Service account credentials (temporary) to connect to cluster through GCP client '''
    credentials = service_account.Credentials.from_service_account_file('./keys.json')
    gcp_api = GoogleCloudAPIClient(credentials)
    
    ''' We can extract information about all the K8S elements like pods, services, volumes... '''
    k8s_api.list_nodes()
    k8s_api.watchServices()    
    
    ''' TODO K8S extraction methods '''
        
    ''' And also GCP elements involved in cluster with the GCP client '''
    gcp_api.list_clusters()
    
    ''' TODO GCP extraction methods '''

class KubernetesAPIClient(object):
    def __init__(self, k8s_api):
        self.__k8sApi = k8s_api
        ns = os.environ.get("K8S_NAMESPACE")
        if ns is None:
            ns = "default"
        self._ns = ns
    
    def list_nodes(self):
        print("Listing nodes and their IPs:")
        nodes = self.__k8sApi.list_node(watch=False)
        for i in nodes.items:
            print("%s" % (i.spec.pod_cidr))
    
    def watchServices(self):
        w = watch.Watch()
        for event in w.stream(self.__k8sApi.list_namespaced_service, self._ns):
            ''' TODO specific processing depending on the event type'''
            if event['type'] == 'ADDED':
                pass
            elif event['type'] == 'MODIFIED':
                pass
            else:
                pass
            
    def services_callback():
        ''' TODO Print relevant info for service discovery '''
        pass
     
class GoogleCloudAPIClient(object):
    def __init__(self, credentials):
        self.__gcpClient = ClusterManagerClient(credentials=credentials)
        
    def list_clusters(self):
        clusters = cluster_manager_client.list_clusters(PROJECT_ID, ZONE)
        ''' TODO Print relevant info '''
        pass
                
if __name__ == '__main__':
    main()
       