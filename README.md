# GKE cluster monitoring with Python clients [In Progress]

Both GCP Python client and Kubernetes Python clients are used to connect to a GKE project in order to retrieve information about clusters and be up to date about changes in them.

Previous to run the app, the following command needs to be run to give default privileges to our Kubernetes client:

```sh
$ gcloud auth application-default login
```

Additionally, a json with the temporary service account credentials for GCP client must be in the path of the project.

To be developed:

* Watches to receive events when happen in the cluster
* Extraction methods needs to be defined yet: extracted items, metrics, output, alarms, etc
