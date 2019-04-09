# Script for creating and loading PatStat2018b dataset into Big Query tables
# coding: utf-8

###############################################
###### Importing Libraries and functions ######

from google.cloud import bigquery
from open_patstat.utils.gcp import create_table, load_gcs_file, delete_table
from open_patstat.utils.schema import Schema

####################################################
###### Initializing the Client anf Job Config ######

# Before running this line, make sure that you have defined the environment variable...
# ..."GOOGLE_APPLICATION_CREDENTIALS" which points to the JSON file containing authentication key
client = bigquery.Client()

# Initializing the Job_config
job_config = bigquery.LoadJobConfig()
job_config.skip_leading_rows = 1
job_config.max_bad_records = 10
job_config.source_format = bigquery.SourceFormat.CSV
dataset_ref = client.dataset('patstat')

###########################################
####### Creating and Adding Tables ########

# Tables list to be loaded
tables_list = ['tls201', 'tls209', 'tls204', 'tls207', 'tls206', 'tls211', 'tls212']

# Google Bucket directory address, which contains all data files
gs_add = 'gs://patstat_2018g/data_PATSTAT_Global_2018_Autumn/'

# Loading the tables in the list
for table in tables_list:
    # Creating the table
    create_table(client,
             dataset_id='patstat',
             table_id=table,
             schema=getattr(Schema(),table))
    # Adding files to the table from GCP bucket
    table_ref = dataset_ref.table(table)
    job_config.schema = getattr(Schema(),table)
        # Adding files to the table from GCP bucket
    table_ref = dataset_ref.table(table)
    job_config.schema = getattr(Schema(),table)
    load_job = client.load_table_from_uri(
        source_uris=gs_add+table+'_*.gz',
        destination=table_ref,
        # job_id=job_id,
        job_id_prefix='lgs-',
        job_config=job_config,
    )
    load_job.result()

