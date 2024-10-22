from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):    
 
    service = build('dataflow', 'v1b3')
    project = "lithe-catbird-434312-p9"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "cricket_dataflow_qa",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://cricket_metadata11112/udf.js",
        "JSONPath": "gs://cricket_metadata11112/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "lithe-catbird-434312-p9:crickt_dataset.batsman_ranking",
        "inputFilePattern": "gs://cricket_data_korir/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://cricket_metadata11112",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
