# Football Scout Rating Generator

### Author: Art Aliu

## Contents

* [Brief](#Brief)
* [Trello Board](#Trello-Board)
* [ED](#ED)
* [Risk Assessment](#Risk-Assessment)
* [Updated Risk Assessment](#Updated-Risk-Assessment)
* [CI/CD Pipeline](#CI/CD-Pipeline)
* [App Design](#App-Design)
* [Services](#Services)
* [Testing](#Testing)
* [Future Improvements](#Future-Improvements)
* [Acknowledgements](#Acknowledgements)

## Brief

The brief provided to us for this project sets the following out as its overall objective: "create an application that generates “Objects” upon a set of predefined rules. These “Objects” can be from whatever domain you wish."

I propose to create a football position app to meet these demands.

We must create an application that has at least 4 services working together.
Service 1 will be the 'core service' which will be responsible for communicating with the other 3 services. Services 2 and 3 will both create a random object, with service 4 also creating a random object based on the results of services 2 and 3.

The full tech stack that I will use in this project is:
- Trello Board for Project Tracking
- CI Server Jenkins
- GCP Cloud Platform
- GIT
- Docker as a containerisation tool
- NGINX as reverse proxy
- Docker Swarm


## Trello Board

I used Trello as a tool for my project management which helped me store and document all of my progress

![image](https://user-images.githubusercontent.com/101266740/168490568-c3f41699-82d5-4df8-8ef7-44d4e00b1ce7.png)


## ED

I started with this basic entity diagram as my initial thoughts as to what I wanted to deliver to the user

![image](https://user-images.githubusercontent.com/101266740/166654334-70edc87d-0a57-46f6-a428-9cab5a0b12bd.png)

Initially my idea was to have service 2 generating a random attribute for a player and for service 3 to have generate a number number between 1-99 using 'random.randint' to show the "skill" level of a player. However, I decided to change it  so that both services 2 and 3 provide a 'random.choice' of a player attribute and player skill respectively. Service 4 will then gather the information from services 2 and 3 and deliver a scout rating using requests and dictionaries. The rating will add the numbers based from the services generated in services 2 and 3.

## App Design

In response to the brief, I have chosen to develop a prize generator. This will look as follows:

- Front-end (Service 1): The service with which the user interacts. This service sends requests to the other services to generate random events and then displays the generated events to the user.
- Number API (Service 2): This service receives HTTP GET requests from service 1 and responds with a random attribute, using random.choice().
- Name API (Service 3): This service receives HTTP GET requests from service 1, and responds with a randomly selected football skill from a list, using random.choice().
- Generate API (Service 4): This service receives HTTP POST requests from service 1, which provide the randomly generated attributes and skills, service 4 has two dictionaries which use this data to provide a point based rating.

## Risk Assessment

![image](https://user-images.githubusercontent.com/101266740/166652051-3153ea9c-7667-4ed5-b7fc-bb4c8ce100fc.png)

My risk assessment for this project shows the possible risks that may arise during this project and the dates which I wrote down each risk.

## Updated Risk Assessment

Whilst going along the project I realised there was more to add to the risk assessment which is what I proceeded to do as shown below:

![image](https://user-images.githubusercontent.com/101266740/166706720-93649325-0df7-42f8-ad98-75114500f0c7.png)

## CI/CD pipeline 

![image](https://user-images.githubusercontent.com/101266740/165782428-cdfc021f-4c7f-4800-86b6-b59873daae2d.png)

Image taken from: https://collabnix.com/wp-content/uploads/2018/03/ci-cd.png

Jenkins was used as a CI Pipeline. I used Github to set up a webhook and then executed the pipeline script which was defined in my Jenkinsfile. I did run into many issues when it came to running ansible on my machine. Issues such as 'failed host key verification' and issues with Docker login. My pipeline consists of 4 main stages: "Testing, Build and push images, docker and deploy". The testing stage executes a bash script which tests all 4 of my services through pytest. The results showed 100% code coverage which was the goal and assured me that all functions for the app were working correctly and smoothly. 
Once the tests are seen to be successful, the build/push stage is executed which uses docker-compose to create the images for the different services which then pushes the images to the Dockerhub. The Jenkins pipeline shows the detailed breakdown of each stage providing an in depth look at each part of the project.
Following this, the deploy stage will then deploy the application, including the docker-compose.yaml and nginx.conf files. The ansible playbook will run all the relevant roles which includes: installing docker on the two swarm machines, initialise a swarm on the manager node and a worker. Stafes that are successful will appear green whilst those that fail will appear red.


## Services

The Front end of the app is seen below. The page refreshes and will generate a random attribute and a random skill. Service 4 then uses these two randomly generated data to give a rating.

![image](https://user-images.githubusercontent.com/101266740/167589433-695049cb-95fa-4e43-a05b-f88c7a648824.png)

![image](https://user-images.githubusercontent.com/101266740/167589499-15869ae1-c21c-4934-9748-8f5929529051.png)

The two images above show the front end which shows the idea of my app. It shows two pages, the second one is after refreshing. And the rating is giving a score which is combining what a scout(in this case the scout is me) is rating those skills in terms of importance on a player. I then used an f string to as a way to explain the scouts review.

## Testing

I utlised my testing for each of the 4 services as seen below, getting 100% coverage on all tests.

![image](https://user-images.githubusercontent.com/101266740/167639537-ff9046e2-b9c6-4913-b221-eac7423a540b.png)

![image](https://user-images.githubusercontent.com/101266740/167639561-feefe235-b819-4b31-af54-14bba3599139.png)

![image](https://user-images.githubusercontent.com/101266740/167639621-5fba8491-80f8-40f0-b8f0-5fe91f9ecb32.png)

![image](https://user-images.githubusercontent.com/101266740/167639644-1e61fc05-6dbc-4fcc-855b-373d7a322955.png)

## Future Improvements

Improve the aesthetics of the app aswell as fully utilise the CRUD to allow the user to choose more attributes and skills instead of the 6 in which they were restricted too. I would also like my application to display a variety of different ratings depending on the scout.

## Acknowledgements

-Victoria Sacre
-Bootstrap
-W3schools for basic navbar code
