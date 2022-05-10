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

![image](https://user-images.githubusercontent.com/101266740/166707724-3043464a-fc17-48cd-8605-0ca453fec013.png)


## ED

I started with this basic entity diagram as my initial thoughts as to what I wanted to deliver to the user

![image](https://user-images.githubusercontent.com/101266740/166654334-70edc87d-0a57-46f6-a428-9cab5a0b12bd.png)

Initially my idea was to have service 2 generating a random attribute for a player and for service 3 to have generate a number number between 1-99 using 'random.randint' to show the "skill" level of a player. However, I decided to change it  so that both services 2 and 3 provide a 'random.choice' of a player attribute and player skill respectively. Service 4 will then gather the information from services 2 and 3 and deliver a scout rating using requests and dictionaries. The rating will add the numbers based from the services generated in services 2 and 3.

## Risk Assessment

![image](https://user-images.githubusercontent.com/101266740/166652051-3153ea9c-7667-4ed5-b7fc-bb4c8ce100fc.png)

My risk assessment for this project shows the possible risks that may arise during this project and the dates which I wrote down each risk.

## Updated Risk Assessment

Whilst going along the project I realised there was more to add to the risk assessment which is what I proceeded to do as shown below:

![image](https://user-images.githubusercontent.com/101266740/166706720-93649325-0df7-42f8-ad98-75114500f0c7.png)

## CI/CD pipeline 

![image](https://user-images.githubusercontent.com/101266740/165782428-cdfc021f-4c7f-4800-86b6-b59873daae2d.png)

Image taken from: https://collabnix.com/wp-content/uploads/2018/03/ci-cd.png

## App Design

In response to the brief, I have chosen to develop a prize generator. This will look as follows:

- Front-end (Service 1): The service with which the user interacts. This service sends requests to the other services to generate random events and then displays the generated events to the user.
- Number API (Service 2): This service receives HTTP GET requests from service 1 and responds with a random attribute, using random.choice().
- Name API (Service 3): This service receives HTTP GET requests from service 1, and responds with a randomly selected football skill from a list, using random.choice().
- Generate API (Service 4): This service receives HTTP POST requests from service 1, which provide the randomly generated attributes and skills, service 4 has two dictionaries which use this data to provide a point based rating.

## Services

## Testing

## Future Improvements

## Acknowledgements

-Victoria Sacre
-Bootstrap
-W3schools for basic navbar code
