# ReadSpeak
ReadSpeak is a web application that allows users to upload an image and have the text in the image transcribed and read out loud using Amazon Polly. The application is built with Django for the backend and React for the frontend, and uses Amazon S3 for storage and Amazon DynamoDB for database management.

## Prerequisites
- An AWS account
- An Amazon S3 bucket for storing the images and audio files
- An Amazon DynamoDB database for storing information about the recordings and texts
- An Amazon Polly account and voice profile for text-to-speech conversion

## Installation
1. Clone the repository:

```bash
codegit clone https://github.com/connorv001/ReadSpeak.git
```

2. Install the dependencies:

```bash
codepip install -r requirements.txt
```

3. Set up the environment variables for your AWS credentials and the names of the S3 bucket and DynamoDB table.
4. Run the migrations:

```bash
codepython manage.py migrate
```

5. Start the development server:

```bash
codepython manage.py runserver
```

## Usage
1. Go to the URL of the development server in your web browser.
2. Upload an image by clicking the "Upload Image" button.
3. The transcribed text and audio file will be displayed.


## Deployment :
1. Host the Django backend on Amazon API Gateway.
2. Deploy the React frontend to a web server or a hosting service such as GitHub Pages or Amazon S3.
