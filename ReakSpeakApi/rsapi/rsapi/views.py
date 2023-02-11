from django.http import HttpResponse
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
import boto3

class ReadSpeakView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']
        textract = boto3.client('textract')
        polly = boto3.client('polly')
        
        # Call AWS Textract to extract text from image
        response = textract.analyze_document(Document={'Bytes': file_obj.read()})
        text = ''
        for item in response['Blocks']:
            if item['BlockType'] == 'LINE':
                text += item['Text'] + '\n'
        
        # Call Amazon Polly to synthesize speech from text
        response = polly.synthesize_speech(
            OutputFormat='mp3',
            Text=text,
            VoiceId='Joanna'
        )
        audio = response['AudioStream'].read()
        
        # Store transcribed text and audio information in DynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ReadSpeak')
        table.put_item(
            Item={
                'text': text,
                'audio': audio
            }
        )
        
        return Response({'text': text, 'audio': audio})