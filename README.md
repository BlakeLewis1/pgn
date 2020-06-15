# PGN
SFIA Project 2

## Project Brief

you are creating an application that generates “Objects” upon a set of predefined rules.
These “Objects” can be from whatever domain you wish.

## Scope

The requirements set for the project are below.
Note that these are a minimum set of requirements and can be added onto during the duration of the project.

The requirements of the project are as follows:

* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
  This could also provide a record of any issues or risks that you faced creating your project.

* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through   a CI server and deployed to a cloud-based virtual machine.

* If a change is made to a code base, then Web hooks should be used so that Jenkins recreates and redeploys the changed application
  The project must follow the Service-oriented architecture that has been asked for.

* The project must be deployed using containerisation and an orchestration tool.
  As part of the project you need to create an Ansible Playbook that will provision the environment that your application needs to run.

## Project Tracking

One of the first things I created for this project was the trello board that I was required to create this helped me structure the project.

[Trello](https://trello.com/b/UzEPIn17/pgn)
![Before and after trello](https://github.com/BlakeLewis1/pgn/blob/master/Documentation/trello%20board%20.png)

## Risk Assessment
[risks](https://github.com/BlakeLewis1/pgn/blob/master/Documentation/risk%20assessment%202.1%20-%20Sheet1.pdf)
## Architecture 

* Kanban Board: Asana or an equivalent Kanban Board

* Version Control: Git

* CI Server: Jenkins

* Configuration Management: Ansible

* Cloud server: GCP virtual machines

* Containerisation: Docker

* Orchestration Tool: Docker Swarm

## CI Pipeline

![CI Pipeline](https://github.com/BlakeLewis1/pgn/blob/master/Documentation/CI%20Pipeline.png)

above is the general-flow of my ci-pipeline that i have created the source code was edited in vsc or visual studio code

## Jenkins
to make sure that my project had continious integration I needed to configure a Jenkins Pipeline for the project
![image](https://user-images.githubusercontent.com/64256460/84604823-abdafa80-ae90-11ea-8436-320367607843.png)
To create the pipe above i had to create a jenkinsfile this file would instruct jenkins on what to do in this case it would tell jenkins to pull the project and then enable all the executable scripts and the final part of the pipe is to deploy the swarm stack.

## Ansible
I used ansible to configure the virtual machines and run the application I created a playbook allowed me to run tasks on multiple VMs. These tasks included in installing Docker on each machine, initializing my Docker Swarm and connecting my worker nodes to the swarm. 

## Database
For my database i created a sql instance using gcp in the instance I created 3 tables that had no relationship with each other and would these would consist of an id number along with a word which would be either an animal for the animals table or a fruit for the fruit table and so on these tables would get these words from the user once they type them in. I added this feature to make sure that there was data that was able to be persisted.

## Database Structure

![ERD](https://github.com/BlakeLewis1/pgn/blob/master/Documentation/PGN%20ER-Diagram.png)

This is the structure of the tables these tables do not require a relationship between them and each will only hold the name of the items added by the 

## Testing 
Intially I wanted to apply a TDD approach to this project and consistently make tests for the different services in my application however this wasn't possible as I could not do this at a consistent enough level. I used PyTest when testing my code I had errors with getting tests to test outside of the service which was crucial for my project however by creating a seperate testing suite I was able to complete the testing for each of the services, linked below are the coverage reports.   

[service1 testing report](https://github.com/BlakeLewis1/pgn/blob/master/Documentation/service%201%20report.png)

[service2 testing report](https://github.com/BlakeLewis1/pgn/blob/master/Documentation/service%202%20report.png)

[service3 testing report](https://github.com/BlakeLewis1/pgn/blob/master/Documentation/service%203%20report.png)

[service4 testong report](https://github.com/BlakeLewis1/pgn/blob/master/Documentation/service%204%20report.png) 

## self reflection 

I was able to create a fully functioning application that is able to give a very secure password.
The project is able to produe a password that is secure and random due to the way that the password is generated in service 4 as it will randomise not just the words selected but the order and length of the password this meant that there was little chance that the user would get the same password twice this would also be a secutity feature as it is more secure to have different passwords for each account you make. In addition to this the user would also be allowed to add their own words so that the passsword generated would be more memorable for the user. 

However there are some improvements that could have been made for the application that would help in future use  

Improvements would include a way to add a test for how strong the password created would be this would enable the user to have a better idea of how strong their password is and enable them to decide whether they want a  new password instead of the one generated. 
In addition to this I would have liked to have a css for the webpage and make the site look more professional than what it currently is. 
To add to this i would have also liked to have a dark mode button implemented for the website this would be a good feature for the user in low light conditions reduce eye strain in low-light conditions as Dark Mode can reduce eye-strain in low light conditions. 100% contrast (white on a black background) can be harder to read and cause more eye strain. It can be harder to read long chunks of text with a light-on-dark theme.

