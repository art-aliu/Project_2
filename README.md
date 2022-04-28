# Prize Generator

### Author: Art Aliu

## Brief

The brief provided to us for this project sets the following out as its overall objective: "create an application that generates “Objects” upon a set of predefined rules. These “Objects” can be from whatever domain you wish."

I propose to create a prize generator app to meet these demands.

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

## Diagram

![image](https://user-images.githubusercontent.com/101266740/165785671-90d80c51-96d1-4b2f-9c1b-c4828dfecae6.png)

As the diagram reveals, service 1 will be my front end. Services 2 and 3 will provide a random number and random name then service 4 will use the result to give a 'prize'.

## Risk Assessment

![image](https://user-images.githubusercontent.com/101266740/165773451-8dba464d-e708-414d-92f8-8f125266b831.png)

My risk assessment for this project shows the possible risks that may arise during this project.

## CI/CD pipeline 

![image](https://user-images.githubusercontent.com/101266740/165782428-cdfc021f-4c7f-4800-86b6-b59873daae2d.png)

Image taken from: https://collabnix.com/wp-content/uploads/2018/03/ci-cd.png
