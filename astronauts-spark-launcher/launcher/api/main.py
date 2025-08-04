from fastapi import FastAPI
from .k8s import create_spark_job

app = FastAPI()

@app.post("/launch")
def launch_job():
    result = create_spark_job()
    return {
        "message": "Job Spark criado com sucesso",
        "job_name": result["job_name"],
        "status": result["status"]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/")
def root():
    return {"message": "FastAPI Spark Launcher", "version": "1.0.0"}