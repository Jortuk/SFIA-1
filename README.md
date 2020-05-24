# Footwear Inventory Management System 
Following the QAC Fundamental Project Specification (DevOps Core) due for 26th May 2020.

## Index
1. [Brief](#brief)
    + [Project Proposal](#projectproposal)
2. [Trello Board](#trelloboard)
    + [Initial Board](#initialboard)

## Brief <a name="brief"></a>
Design a Create Read Update and Delete (CRUD) application utilising tools, methodologies, and technologies that illustrate all core modules covered during training so far.

The requirements are, however not limited too:
- Trello Board (or Kanban equivalent).
- A relational MySQL database created on Google Cloud Platform (GCP) - displayed with an Entity Relationship Diagram (ERD).
- Clear documentation including architecture design, risk assessment, and so on.
- The CRUD application itself, coded in Python, that meets the User Stories on the Trello Board
- Testing the application for validation using Pytest - consistent reports and evidence must be provided to prove a Test Driven Development (TDD) approach.
- A fully functioning front-end website with integrated APIs, using Flask.
- Code incorporated into a Version Control Machine (VCS), implementing the Feature-Branch model which will then be built through a Continuous Integration (CI) server i.e. Jenkins, before finally being deployed to a cloud-based Virtual Machine (VM).

### Project Proposal <a name="projectproposal"></a>
My project aims to function as an Inventory Management System (IMS) for footwear products, for a hypothetical website - 'Shoose.com'. As an admin, shoes can be added and linked to pre-existing shops within the MySQL database. Both are joined together on a joining table, showcasing two many-to-many relationships. The IMS will be automatically built using Jenkins and GitHub Webhooks.

## Trello Board <a name="trelloboard"></a>
To track my project progression, I used a kanban Trello Board. This helped me to have an overview of different stages of the project. Although this wan an individual project, Agile methodology was carried out where possible, regarding the product and sprint (tasks) backlog. The product backlog contained User Stories that the CRUD application had to fulfill, then the tasks broke this down into smaller objectives that had to be completed to meet the end-goal.

### Initial Board <a name="initialboard"></a>
![image](https://drive.google.com/uc?export=view&id=1d6d1a2NCrQNdpFe7tiJo4Iyu_kyZTFBB)
