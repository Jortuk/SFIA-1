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
    + [Risk Assessment Revisited](#riskrevisit)
4. [Architecture](#archi)
    + [Entity Relationship Diagrams](#erd)
5. [Deployment](#deployment)
    + [Tools, Technologies and Languages](#ttl)
6. [Front-end Design](#fdesign)

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
Due to the size of my risk assessment being too big to turn into a .PNG, the link for it can be found <a href="https://drive.google.com/open?id=1P-GaIPDCMVp0goVafJUdVP-oQIsWDpqf">here</a>. The 'Likelihood' and 'Impact' columns are rated on a scale of 1 (low) to 5 (high). The assessment encompasses the following types of risks: Time Management, Computer-related Injuries, Security and Other.

### Risk Assessment Revisited <a name="riskrevisit"></a>
The link for this assessment can be found <a href="https://drive.google.com/open?id=12DV4u67lq7aSlocLogD3vRRZl9lboC5qcYLrbm9IJpY">here</a>. During the project, I revisited my initial risk assessment and added an 'Update' column. This was filled with new considerations and discussed how effective the original solutions were.

Note: Both Risk Assessments are also located within the Documentation folder of this repository.

## Architecture <a name="archi"></a>
### Entity Relationship Diagrams <a name="erd"></a>
![image](https://drive.google.com/uc?export=view&id=14VIJZAb27fpLH9GmlslE44lvbHYXaOY7)

The core architecture of the application involves two main tables (shoes_tb and shops_tb), both having a relationship with a joining table (shoesshops_tb). All were made in a MySQL database through Flask. The shoesshops_tb links data from the main tables, in this case shoes and shops, to show which shoes can be purchased at which shop.

Underneath the previously discussed tables is an adminlogin_tb. This table has a one-to-one relationship with all other tables due to the fact that there are functions, specifically Create Update and Delete, that require admin level access. This was a decision that required much consideration. In the end, I decided it was a good choice as IMSs are used for companies, not the customer. Yet, the customer/user can still Read about the name, size and price of a desired shoe, and what shop to but it from.

![image](https://drive.google.com/uc?export=view&id=1LSMPA05MJNA_wDj7jzrjeh74ASYHkpay)

I later expanded on the previous diagram, adding an orders_tb with a many-to-many relationship with the shoesshops_tb, as a user could have many orders with many shoes from many shops. By proxy, this would demand a customerlogin_tb in order for a user to make orders and log in to see their orders.

After careful consideration, I decided against these additions as I wanted to focus on achieving the Minimum Viable Product (MVP) before attemping to try and add even more tables, which would have perhaps resulted in overwhelming myself. What's more, this section of the project already exceeds the MVP as it contains two relationships rather than one. Yet, this is not to say they will not be added in future.   

## Deployment <a name="deployment"></a>
![image](https://drive.google.com/uc?export=view&id=1jRfyKoUjp3DHN_Ic3bmVSJp2OvYGBxI9p6r5iF8-xU8)

### Tools, Technologies and Languages <a name="ttl"></a>
The following are all the tools, technologies and languages used to create and deploy the app:
- <b>Trello</b>: Used for project tracking 
- <b>GitHub</b>: Version Control System, also used in conjunction with Jenkins via Webhook
- <b>Google Cloud Platform (GCP)</b>: Allows live, virtual environment for the application, also a host for MySQL database
- <b>MySQL</b>: Enables SQL databases and tables, as well as allowing query functions in Python
- <b>Jenkins</b>: Continuous Integration (CI) Server - automatically builds application from pushed code on GitHub
- <b>Unit Testing (PyTest)</b>: Tests one function at a time with optional coverage
- <b>Gunicorn</b>: <b>NEEDS EDITING</b>
- <b>Visual Studio Code</b>: IDE used for several languages to achieve front-end and back-end development:
    + <b>CSS</b>: Styling for front-end design
    + <b>HTML</b>: Front-end design
    + <b>Python3</b>: Logic and functionality
    + <b>Flask</b>: Integrates front-end and back-end
    + <b>Jinja2</b>: Allows for python variables and logic in HTML

## Front-end Design <a name="fdesign"></a>
