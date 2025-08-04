FROM bitnami/spark:3.5.3

USER root

# Instala pip se não estiver disponível
RUN apt-get update && apt-get install -y python3-pip && rm -rf /var/lib/apt/lists/*

# Instala dependências Python para os jobs Spark
COPY spark-requirements.txt /tmp/spark-requirements.txt
RUN pip3 install -r /tmp/spark-requirements.txt

# Copia os scripts para o container Spark
COPY jobs /opt/spark/jobs

USER 1001 