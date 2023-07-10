# Judgy - Backend
#### YOUR TRUSTED ALLY FOR HACKATHON JUDGING
#
The frontend code for the project can be found here [https://github.com/yajatvishwak/judgy-frontend](https://github.com/yajatvishwak/judgy-frontend)

## What is Judgy?

Judgy streamlines the evaluation process for hackathon judges by leveraging AI to assist in code examination, market research, and providing interactive chat capabilities, along with an efficient semantic search functionality to navigate through numerous project submissions.

## How does it work?

Judgy uses Langchains and models in Google Vertex AI to build the following agents

1. Market Research Agent: This agent uses the project description to ask a set of predefined questions about the idea, such as the size of the target market, existing solutions, and the uniqueness of the project. These questions provide judges with quick insights into the project's potential.

2. Code Analysis Agent: The code agent thoroughly scans the entire project's codebase and asks predefined questions about the technologies used, whether the project adheres to the hackathon's rules, and the quality of the code. This analysis helps judges evaluate the technical aspects of the project.

3. Chat Agent: This agent offers an interactive chat session where judges can ask questions and have a conversation. It combines the knowledge obtained from both the code analysis and market research agents, providing judges with comprehensive information to make informed decisions.

4. Search Agent: With a large number of submissions in a hackathon, finding specific projects can be challenging. The search agent enables judges to perform searches using plain English queries, making it easier to find relevant projects based on specific criteria.


## Technologies Used

The backend is using the following technologies:

-   FlaskAPI
-   MongoDB
-   Google Vertex AI
-   LangChains


## Setup

To get started with the project, follow these steps:

1.  Clone the repository: `git clone https://github.com/SutureLogs/backend`
2.  Install dependencies: `pip install -r requirements.txt`
3.  Create a `.env` file and add the following variable `GOOGLE_APPLICATION_CREDENTIALS=<path of the service worker json file>`
4.  Start the server: `python server.py`
5.  The server runs on port `8000`


## Submission Video

