# Questions API Documentation

### Introduction

The Questions API is a tool designed to streamline the process of generating questions and answers from news articles. Its primary purpose is to assist users in extracting key information and insights from text-based content, enabling them to create engaging quizzes, study materials, or informative summaries with ease.

### Getting Started

First Clone this folder in the project:

- Create a new Folder for the project.
- run the following commands:
  - `git init`
  - `git remote add -f origin https://github.com/AbhinavSinghSokhi/SpeakWise-Hub.git`
  - `git config core.sparseCheckout true`
  - `echo "questions-api/" >> .git/info/sparse-checkout`
  - `git pull origin dev` (Or use main branch if you need to)
    Next:

\[Fully read this before acting upon it\]

First you will need an OpenAI API KEY. To get this, create and OpenAI Account or login from an existing Login Provider and Open the dashboard. Navigate to API Keys, and click on Create New Secret Key. This generates a secret key which is available to copy ONLY ONCE so make sure to copy it.  

Next create an environment variable file(`.env`) and put your OpenAI Secret Key in there like so:  
 - OPEN_API_KEY=yourexampleapikey
 - additionally ou must define the DB Url and API Port in the .env file like so:
   - DB_URL=your_db_url
   - API_SERVER_PORT=3001
Now You can start using the APIs provided by Speakwise Hub!

\*\*Please note that all of these functions are limited to the number of requests allowed per minute as set by OpenAI and has an upper limit of $5 per month which is roughly equal to 1 Million Token(IN and OUT both).  

Note that all responses are given as JSON Objects, with status code being the HTTP Status Code of the response. If any error occurs while processing it will give an 500 Internal Server Error.

### Calling API Using cURL

Curl Request:

``curl --location 'http://localhost:3001/graphql' \``

``--header 'Content-Type: application/json' \``

``--data '{"query":"query ($article: ArticleInputs) {\n getQuestions(\n article: $article\n ) {\n question\n answer\n }\n}","variables":{"article":{"heading":"This is an example Heading for the news Article", "content": "Hello, this is an example article, we hope you are in the best of your health and are enjoying this beautiful day/night."}}}'``

Do replace the variable article: {heading, content} to your actual article object.

This API returns a GraphQL JSON Object as data in the form: {getQuestions: {"question": "Returned Question", "answer": "Returned Answer" }}
Have fun coding!