import boto3
import source.commons.environment as environment
from typing import Any, Dict
import json
import uuid


class SQSHelper:

    def __init__(self):
        self.sqs = boto3.resource('sqs')

    def send_message_queue(self, message_attrs: Dict) -> Any:
        queue = self.sqs.get_queue_by_name(QueueName=environment.AWS_SQS_QUEUE)
        if not message_attrs:
            raise KeyError
        response = queue.send_message(
            MessageBody=str(json.dumps(message_attrs)),
            MessageDeduplicationId=str(uuid.uuid4()),
            MessageGroupId='cropland-importation-development'
        )
        return response.get('Failed')

    def send_message_queue_onboarding(self, message_attrs: Dict) -> Any:
        queue = self.sqs.get_queue_by_name(QueueName=environment.AWS_SQS_QUEUE_ONBOARDING)
        if not message_attrs:
            raise KeyError
        response = queue.send_message(
            MessageBody=str(json.dumps(message_attrs)),
            MessageDeduplicationId=str(uuid.uuid4()),
            MessageGroupId='cropland-onboarding-development'
        )
        return response.get('Failed')
