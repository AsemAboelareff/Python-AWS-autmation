import json
import boto3
import configparser

def main():
#get AK/SK from credentials
    crd = configparser.RawConfigParser()
    crd.read('credentials')
    AK = crd.get('default','aws_access_key_id')
    SK = crd.get('default','aws_secret_access_key') 
#get parameters
    parameters_json=open('Parameter.json').read()
    parameters_data = json.loads(parameters_json)
    region = parameters_data["RegionId"]
    session = boto3.client('cloudformation', region, aws_access_key_id=AK, aws_secret_access_key=SK)
    template_url = parameters_data["TemplateUrl"]
#create stack
    result = session.create_stack(StackName='Asem',TemplateURL=template_url)
    print(result)
    
    
if __name__ == "__main__":
    main()    