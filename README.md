# Footwear Inventory Management System 
Following the QAC Fundamental Project Specification (DevOps Core) due for 26th May 2020.

## Index
1. [Brief](#brief)
    + [Project Proposal](#projectproposal)
2. [Trello Board](#trelloboard)
    + [Initial Board](#initialboard)
    + [On-going Changes](#changes)
    + [Final Board](#finalboard)
3. [Risk Assessment](#risk)

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

The above image displays my Trello Board prior to any project progression. As you can see, only the 'Product Backlog' and 'Tasks' columns are populated. The board also included an 'In Progress' column to show what was being worked on but not yet completed, a 'Tested?' column to illustrate what had been tested, for example the CRUD application itself, a 'Done' column to indicate what was finished, and finally a 'Bugs/Issues' column in case there were any problems while attempting to complete a task.

### On-going Changes <a name="changes"></a>
![image](https://drive.google.com/uc?export=view&id=1__VUMEC28VAjuXz1Q5r4F49viOVwbWrq)

As project development went on, I made some modifications to the Trello Board. First, the MoSCoW (Must have, Should have, Could have, Would have) method was implemented to prioritise which tasks were the most important to complete, from most to least important. Note, names such as 'Could Haves' and 'Would Haves' did not mean they might have not made it into the project, they were only for prioritisation purposes. Second, tasks that had been completed were moved to the 'Done' column, as shown above. Lastly, a bug was encountered when creating a MySQL foreign key. However, this issue was resolved and labelled as 'FIXED'.

### Final Board <a name="finalboard"></a>
![image](https://drive.google.com/uc?export=view&id=1js5eU76mnwDvg3Z7SRNWD73M6Ly9UruS)

By the project due date (26th May), all of the User Stories had been met, and issues were fixed and near to none. However, integration testing using Selenium had not been completed. Unfortunately, this was a result of the testing not being fully conducted because of time restrictions toward the end of the project.

## Risk Assessment <a name="risk"></a>
Due to the size of my risk assessment being too big to turn into a .PNG, the link for it can be found <a href="https://drive.google.com/open?id=1P-GaIPDCMVp0goVafJUdVP-oQIsWDpqf" target="_blank">here.</a> The 'Likelihood' and 'Impact' columns are rated on a scale of 1 (low) to 5 (high).
