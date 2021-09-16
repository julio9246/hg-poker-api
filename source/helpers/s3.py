import boto3
import source.commons.environment as environment
import datetime


class S3Helper:

    def __init__(self):
        self.client = boto3.client('s3')

    def upload_file(self, file, key, extra_args=None):
        with open(file, 'rb') as f:
            self.client.upload_fileobj(f, environment.AWS_S3_BUCKET, key, ExtraArgs=extra_args)


    def s3_write(self, file_object):
        try:
            resource = boto3.resource('s3')
            filename = f'export_{datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.xlsx'
            s3_object = resource.Object(bucket_name=environment.AWS_S3_BUCKET_EXPORT, key=filename)
            s3_response = s3_object.put(Body=file_object, ACL='public-read')
            s3_object.wait_until_exists()
            print(s3_response)
            return "https://{0}.s3.amazonaws.com/{1}".format(environment.AWS_S3_BUCKET_EXPORT, filename)
        except Exception as e:
            print("---------------------------------------------")
            print("---------------------------------------------")
            print(e)
            print("---------------------------------------------")
            print("---------------------------------------------")
            return 'ERROR: ' + str(e)
