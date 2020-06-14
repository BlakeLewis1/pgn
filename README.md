# pgn
sofia project 2

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
