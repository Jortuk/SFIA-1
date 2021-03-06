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
    + [Home Page](#home)
    + [Shoes Page](#shoes)
        + [Updating and Deleting Shoes](#updateanddelete)
    + [Shops Page](#shops)
        + [Example Shop](#exshop)
    + [Admin Login Page](#login)
7. [Testing](#testing)
    + [PyTest](#pytest)
    + [PyTest Coverage](#pytestcov)
8. [Project Hindsight](#hindsight)
    + [Noteable Accomplishments](#accomp)
    + [Project Drawbacks](#drawbacks)
    + [Future Improvements](#improvements)
9. [Author](#author)
10. [Acknowledgements](#ack)
11. [License](#license)
    
## Brief <a name="brief"></a>
Design a Create, Read, Update and Delete (CRUD) application utilising tools, methodologies, and technologies that illustrate all core modules covered during training so far.

The requirements are, however not limited too:
- Trello Board (or Kanban equivalent).
- A relational MySQL database created on Google Cloud Platform (GCP) - displayed with an Entity Relationship Diagram (ERD).
- Clear documentation including architecture design, risk assessment, and so on.
- The CRUD application itself, coded in Python, that meets the User Stories on the Trello Board.
- Testing the application for validation using Pytest - consistent reports and evidence must be provided to prove a Test Driven Development (TDD) approach.
- A fully functioning front-end website with integrated APIs, using Flask.
- Code incorporated into a Version Control Machine (VCS), implementing the Feature-Branch model which will then be built through a Continuous Integration (CI) server i.e. Jenkins, before finally being deployed to a cloud-based Virtual Machine (VM).

### Project Proposal <a name="projectproposal"></a>
My project aims to function as an Inventory Management System (IMS) for footwear products, for a hypothetical website - 'Shoose.com'. As an admin, shoes can be added and linked to pre-existing shops within the MySQL database. Both are joined together on a joining table, showcasing two many-to-many relationships. The IMS will be automatically built using Jenkins and GitHub Webhooks, then deployed on a WSGI production server using Gunicorn.

## Trello Board <a name="trelloboard"></a>
To track my project progression, I used a kanban Trello Board. This helped me to have an overview of the different stages of the project. Although this was an individual project, Agile methodology was carried out where possible, regarding the product and sprint (tasks) backlog. The product backlog contained User Stories that the CRUD application had to fulfill, then the tasks broke this down into smaller objectives that had to be completed to meet the end-goal.

### Initial Board <a name="initialboard"></a>
![](Documentation/images/initial_trello_board.PNG)

The above image displays my Trello Board prior to any project progression. As you can see, only the 'Product Backlog' and 'Tasks' columns are populated. The board also included an 'In Progress' column to show what was being worked on but not yet completed, a 'Tested?' column to illustrate what had been tested, for example the CRUD application itself, a 'Done' column to indicate what was finished, and finally a 'Bugs/Issues' column in case there were any problems while attempting to complete a task.

### On-going Changes <a name="changes"></a>
![](Documentation/images/updated_trello_board.PNG)

As project development went on, I made some modifications to the Trello Board. First, the MoSCoW (Must have, Should have, Could have, Would have) method was implemented to prioritise which tasks were the most important to complete, from most to least important. Note, names such as 'Could Haves' and 'Would Haves' did not mean they might not have made it into the project, they were for prioritisation purposes only. Second, tasks that had been completed were moved to the 'Done' column, as shown above. Lastly, a bug was encountered when creating a MySQL foreign key. However, this issue was resolved and labelled as 'FIXED'.

### Final Board <a name="finalboard"></a>
![](Documentation/images/final_trello_board.PNG)

By the project due date (26th May), all of the User Stories had been met, and issues were fixed. However, integration testing using Selenium had not been completed. Unfortunately, this was a result of the testing not being fully conducted because of time restrictions toward the end of the project.

## Risk Assessment <a name="risk"></a>
Due to the size of my risk assessment being too big to turn into a .PNG, the link for it can be found <a href="https://drive.google.com/open?id=1P-GaIPDCMVp0goVafJUdVP-oQIsWDpqf">here</a>. The 'Likelihood' and 'Impact' columns are rated on a scale of 1 (low) to 5 (high). The assessment encompasses the following types of risks: Time Management, Computer-related Injuries, Security and Other.

### Risk Assessment Revisited <a name="riskrevisit"></a>
The link for this assessment can be found <a href="https://drive.google.com/open?id=12DV4u67lq7aSlocLogD3vRRZl9lboC5qcYLrbm9IJpY">here</a>. During the project, I revisited my initial risk assessment and added an 'Update' column. This was filled with new considerations and discussed how effective the original solutions were.

Note: Both Risk Assessments are also located within the Documentation folder of this repository.

## Architecture <a name="archi"></a>
### Entity Relationship Diagrams <a name="erd"></a>
![](Documentation/images/ERD_1.PNG)

The core architecture of the application involves two main tables (shoes_tb and shops_tb), both having a relationship with a joining table (shoesshops_tb). All were made in a MySQL database through Flask. The shoesshops_tb links data from the main tables, in this case shoes and shops, to show which shoes can be purchased at which shop.

Underneath the previously discussed tables is an adminlogin_tb. This table has a one-to-one relationship with all other tables due to the fact that there are functions, specifically Create, Update and Delete, that require admin level access. This was a decision that required much consideration. In the end, I decided it was a good choice as IMSs are used for companies, not the customer. Yet, the customer/user can still Read about the name, size and price of a desired shoe, and what shop to but it from.

![](Documentation/images/ERD_2.PNG)

I later expanded on the previous diagram, adding an orders_tb with a many-to-many relationship with the shoesshops_tb, as a user could have many orders with many shoes from many shops. By proxy, this would demand a customerlogin_tb in order for a user to make orders and log in to see their orders.

After careful consideration, I decided against these additions as I wanted to focus on achieving the Minimum Viable Product (MVP) before attemping to try and add even more tables, which would have perhaps resulted in overwhelming myself. What's more, this section of the project already exceeds the MVP as it contains two relationships rather than one. Yet, this is not to say they will not be added in future.   

## Deployment <a name="deployment"></a>
![](Documentation/images/deployment.PNG)

### Tools, Technologies and Languages <a name="ttl"></a>
The following are all the tools, technologies and languages used to create and deploy the app:
- <b>Trello</b>: Used for project tracking 
- <b>GitHub</b>: Version Control System, also used in conjunction with Jenkins via Webhook
- <b>Google Cloud Platform (GCP)</b>: Allows a live, virtual environment for the application, also a host for MySQL database
- <b>MySQL</b>: Enables SQL databases and tables, as well as allowing query functions in Python
- <b>Jenkins</b>: Continuous Integration (CI) Server - automatically builds the application from pushed code on GitHub
- <b>Unit Testing (PyTest)</b>: Tests one function at a time with optional coverage
- <b>Gunicorn</b>: Deploys application on a Production WSGI server
- <b>Visual Studio Code</b>: IDE used for several languages to achieve front-end and back-end development:
    + <b>CSS</b>: Styling for front-end design
    + <b>HTML</b>: Front-end design
    + <b>Python3</b>: Logic and functionality
    + <b>Flask</b>: Integrates front-end and back-end
    + <b>Jinja2</b>: Allows for python variables and logic in HTML

## Front-end Design <a name="fdesign"></a>
To keep this section concise, rather then showing both the user and admin front-end, only the admin view of the front-end will be shown. Although, keep in mind that the only difference is the user view does not have any of the Create, Update or Delete APIs. Although CCS was not a priority according to the project specification, a small amount has been added to slightly better the user experience (UX). The user interface (UI) has been laid out in a way that is user-friendly. 

### Home Page <a name="home"></a>
![](Documentation/images/home_page.PNG)

Above is the home and landing page. It welcomes users to the site and offers links to the 'Shoes' and 'Shops' pages. 

### Shoes Page <a name="shoes"></a>
![](Documentation/images/shoes_page.PNG)

Next, the shoes page. Users can come to this page and see what Shoose.com has in its inventory. On the other hand, with admin access there is an 'Add Shoe' API that satisifies the Create functionality of the application. This API works with HTML, CSS, Jinja2, Python and Flask so that a new entry can be added to the MySQL database. This is the case for most APIs in this project. Furthermore, the 'Update Shoe' API, fulfilling the Update functionality, allows the admin to change an already existing entry in the database, in terms of the 'Shoe Name' and 'Shoe Price'.

#### Updating and Deleting Shoes <a name="updateanddelete"></a>
![](Documentation/images/update_delete_shoe.PNG)

As mentioned above, this is where a shoe can be updated. Moreover, a shoe can also be deleted when the 'Delete Shoe' button is pressed. When pressed, the button runs a function that removes the selected shoe entry from the database. Thus, supporting the Delete functionality of the application.

### Shops Page <a name="shops"></a>
![](Documentation/images/shops_page.PNG)

Here, the shops available are listed. These links redirect the user to a selected shop, where they will find the shoes that are sold at that shop. 

#### Example Shop <a name="exshop"></a>
![](Documentation/images/example_shop.PNG)

As an example, the first shop is shown above. The shoes at this shop are shown through the joining table, shoesshops_tb, discussed earlier. It uses the shoe IDs to determine which shoes are displayed, as long as the shop ID is equal to 1. This is also the case for the following shops, where the shop ID will be 2, and so on. In addition, the admin can update the quantity of a shoe to fulfill the application's role as an IMS, and further adhere to the Update functionality. 

### Admin Login Page <a name="login"></a>
![](Documentation/images/login_page.PNG)

On this page, an admin can login with an existing email and password that is within the 'Users' table of the MySQL database. The functionality for the login feature was given to the cohort by QA, therefore it will not count towards the overall mark for the project.

## Testing <a name="testing"></a> 
### PyTest <a name="pytest"></a>
Testing was achieved through Unit Testing, using the PyTest tool. This type of testing checks one function at a time through code written in a 'test_back_end.py', in this instance. Firstly, the flask url_for function was used to test whether or not a function did as it was programmed to, and direct to its specified page, returing a HTTP 200 value. All these tests were successful. Secondly, the CRUD functions were tested, taking advantage of the AssertIn() imported from unittest. Once again, these were all successful.

![](Documentation/images/pytest.PNG)

Note: The warning in the image above displays that 'flask.json_available' is deprecated. This in not an error in testing. 

### PyTest Coverage <a name="pytestcov"></a>
![](Documentation/images/pytest_coverage.PNG)

Overall, a coverage of 99% was attained. Using the 'pytest --cov ./application/ --cov-report term-missing' command, I was able to determine which lines of code were not covered during testing. After directing to the routes.py file, where the missed lines of code were, I found that the two lines of code were inside the login function. After several attempts of trying to create a function to test this, I was unfortunately unsuccessful. Therefore, this is something to learn for the future.

## Project Hindsight <a name="hindsight"></a>
### Noteable Accomplishments <a name="accomp"></a>
<b>Good Implementation of the Feature Branch Model</b>

I followed best practices by implementing the Feature Branch model, just as we learned during training. Before being merged onto the 'master' branch, all code was tested, version controlled and deployed using a 'developer' branch, before finalisation.

![](Documentation/images/branch_merge.PNG)

<b>Application Deployed onto a Production WSGI Server using Gunicorn</b>

When Jenkins automatically builds the application, the 'installation.sh' file within the repository runs a command to deploy the application on a production server using Gunicron, rather than a development server. This makes the deployment more stable, faster, and able to handle more requests at once.

### Project Drawbacks <a name="drawbacks"></a>
<b>Lack of Integration Testing</b>

Even though there was a high percentage of coverage in terms of Unit Testing, there was no Integration Testing. This is a disadvantage as it decreases validity. What's more, there is no way to verify whether the application works in unity. Ultimately, this goes against a TDD approach.

### Future Improvements <a name="improvements"></a>
<b>Full Testing Coverage</b>

Although test coverage was 99%, I feel it is important to be able to test your application fully. Full coverage would confirm the application's relevance, that it carries out what it aims to do, and it is as effective as it could be.

<b>Integration Testing</b>

As mentioned in Project Drawbacks, integration testing would drastically improve this project. To ensure this is carried out in future, I will work on my time management skills and set aside some time dedicated to this, as well as all round testing.

<b>Adding more Tables and Relationships</b>
During the ERD section of this document, I suggested a more complex core architecture could be put into practice. Incorporating an orders table and feature, along with a customer login, would add value to the application, making it richer with content.

## Author <a name="author"></a>
Jordan Taylor

## Acknowledgements <a name="ack"></a>
The QA Academy trainers for their enjoyable and detailed training sessions, as well as my fellow QA Academy Trainees.

## License <a name="license"></a>
MIT License

Copyright (c) 2020 Jordan Taylor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
