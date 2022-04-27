# Prize Generator

### Author: Art Aliu

## Brief

The brief provided to us for this project sets the following out as its overall objective: "create an application that generates “Objects” upon a set of predefined rules. These “Objects” can be from whatever domain you wish."

I propose to create...


We must create an application that has at least 4 services working together.
Service 1 will be the 'core service' which will be responsible for communicating with the other 3 services. Services 2 and 3 will both create a random object, with service 4 also creating a random object based on the results of services 2 and 3.


ERD

![image](https://user-images.githubusercontent.com/101266740/165546302-ded7040e-8be2-4f65-b5e9-e03e6c236dbd.png)

As the ERD reveals, service 1 will be my front end. Services 2 and 3 will be the random number and random name generator which will look at whether the number generated is even or odd and if the name begins with a letter in the first half of the alphabet to determine the prize which will be generated through service 4.
