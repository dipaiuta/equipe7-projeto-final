from dataproc import *
import os
from google.cloud import storage

ServiceAccount = r'C:\Users\quel-\OneDrive\Área de Trabalho\CURSOS\Curso - Python\Projeto_final\projeto-mineracao-soulcode-85d1cc17951f.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ServiceAccount

# Enviando os arquivos dos jobs para o bucket:
client = storage.Client()
bucket = client.get_bucket('soulcode-mineracao')
blob1 = bucket.blob('job1.py')
blob2 = bucket.blob('job2.py')
blob3 = bucket.blob('job3.py')
blob4 = bucket.blob('job4.py')

blob1.upload_from_filename(r'C:\Users\quel-\OneDrive\Área de Trabalho\CURSOS\Curso - Python\Projeto_final\Jobs\job1.py')
blob3.upload_from_filename(r'C:\Users\quel-\OneDrive\Área de Trabalho\CURSOS\Curso - Python\Projeto_final\Jobs\job3.py')
blob4.upload_from_filename(r'C:\Users\quel-\OneDrive\Área de Trabalho\CURSOS\Curso - Python\Projeto_final\Jobs\job4.py')

# Criando o cluster:
cluster_name = "teste-configuracao"
project_id = "projeto-mineracao-soulcode"
region = "us-east1" # Importante que seja a mesma região padrão do seu projeto
gcs_bucket = "soulcode-mineracao"

cluster = Dataproc(cluster_name, region, project_id)
cluster.cria_cluster()

# Enviando os jobs:
job1 = Job(region, project_id, gcs_bucket, 'job1.py', cluster_name)
job2 = Job(region, project_id, gcs_bucket, 'job2.py', cluster_name)
job3 = Job(region, project_id, gcs_bucket, 'job3.py', cluster_name)
job4 = Job(region, project_id, gcs_bucket, 'job4.py', cluster_name)
try:
    job1.cria_job()
    # job2.cria_job()
    # job3.cria_job()
    # job4.cria_job()
except Exception as e:
    print(str(e))

# Deletando o cluster para evitar cobranças
cluster.deleta_cluster()