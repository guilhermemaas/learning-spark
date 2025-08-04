import yaml
import datetime
from kubernetes import client, config

def create_spark_job():
    config.load_incluster_config()  # ou config.load_kube_config() para local
    
    # Carrega o template
    with open("manifests/spark-template.yaml") as f:
        spec = yaml.safe_load(f)
    
    # Cria nome único com timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    job_name = f"spark-astronauts-{timestamp}"
    spec['metadata']['name'] = job_name
    
    api = client.CustomObjectsApi()
    
    # Cria o novo job
    result = api.create_namespaced_custom_object(
        group="sparkoperator.k8s.io",
        version="v1beta2",
        namespace="default",
        plural="sparkapplications",
        body=spec
    )
    
    return {"job_name": job_name, "status": "created"}