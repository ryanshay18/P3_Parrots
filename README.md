# BeakersTorts's College survey

# links
- Website link: http://beakerscollegepicker.tk
- Easter egg: http://104.2.87.139:8080/easteregg/
- Scrum board link: https://github.com/valeriemiliteeva/BeakersTorts/projects/1
- First Big Ticket Video: https://youtu.be/LaLQzCo173c

# Creators & Github Links
NAME             | GITHUB Link |
-------------    | --------------- |
William Cherres | https://github.com/BillyCherres  |
Valerie Militeeva | https://github.com/valeriemiliteeva |
Lola Bulkin  | https://github.com/lolabulkin |
Michael Irribarren    | https://github.com/MichaelIribarren |

# Project Overview:
The user will be asked a series of multiple choice questions all college related. Then after the user answer's all of the questions, the user will be given a select number of colleges based on the answers given. To make this College Survey accurate, the creators implemented an API that contains thousands of colleges for the algorithim to choose from that best suits the user.

**IMPORTANT** : To easily navigate our site, please use the navbar at the top left of the home screen for guidence.

# Project Details
Section            | Details |
-------------    | --------------- |
Multiple Choice Page | **Some questions asked will be:** What do you prefer the environment to be? What is your ideal location? What majors/areas of study are you most interested in? What degree are you looking to get in college?|
College Database  | The database implemented into the College Survey Project holds over a thousand colleges and their attributes like school size, city, state, and if it offers undergrad and postgraduate degrees |
Easter egg  | **Contains:** Who am I in Computer Science for each team member, Links to pair share journals, How our project meets college board requiremnets  |
About Us Page    | This page contains all the fun information you need to know about your favorite creators! From fun pictures to interesting facts, this page will help you get closer to the Team! |

# Project Code Snippets
## Database (Val)
- This code shoes the complexity of the database and demonstrates the attributes being pulled from the api and being implemented into the database.
```# school.name,school.city,school.state,school.zip,school.carnegie_size_setting,school.school_url,school.carnegie_basic,school.locale,school.region_id,school.ownership,school.carnegie_undergrad
 crs.execute('''create table schools (
                  name text, 
                  region_id integer, 
                  state text)''')
                  name text,
                  city text,
                  state text,
                  url text,
                  region_id integer,
                  locale integer,
                  carnegie_size_setting integer,
                  carnegie_basic integer,
                  carnegie_undergrad integer,
                  ownership integer)''')

 crs.execute("insert into schools values('my school', 11, 'CA')")
 def insert_school(school):
   locale = str(school['school.locale']) if school['school.locale'] else 'null'
   carnegie_size_setting = str(school['school.carnegie_size_setting']) if school['school.carnegie_size_setting'] else 'null'
   carnegie_basic = str(school['school.carnegie_basic']) if school['school.carnegie_basic'] else 'null'
   carnegie_undergrad = str(school['school.carnegie_undergrad']) if school['school.carnegie_undergrad'] else 'null'
   ownership = str(school['school.ownership']) if school['school.ownership'] else 'null'
   url = '"' + school['school.school_url'] + '"' if school['school.school_url'] else 'null'
   query = 'insert into schools values(' + \
           '"' + school['school.name'] + '", ' + \
           '"' + school['school.city'] + '", ' + \
           '"' + school['school.state'] + '", ' + \
           url + ', ' + \
           str(school['school.region_id']) + ', ' + \
           locale + ', ' + \
           carnegie_size_setting + ', ' + \
           carnegie_basic + ', ' + \
           carnegie_undergrad + ', ' + \
           ownership + ")"
   print(query)
   crs.execute(query)

```
## API (Val)
- This code shows the api being used in the project and the process of implementing the attributes from this api into the database code which is up above in the  Database code section. 
```import requests

# url = "https://api.data.gov/ed/collegescorecard/v1/schools"
# url = "https://developer.nrel.gov/api/collegescorecard/v1/schools"

url = "https://api.data.gov/ed/collegescorecard/v1/schools?_per_page=100&_page={page}&" \
      "api_key=9o9cbIMIYKRe90jn29mhBTS1AZXbCvyLf0EygeES&" \
      "fields=school.name,school.city,school.state,school.zip,school.carnegie_size_setting,school.school_url,school.carnegie_basic,school.locale,school.region_id,school.ownership,school.carnegie_undergrad"

# print(url.replace("{page}", "11"))

for page in range(68):
  print('Reading page #' + str(page))
  response = requests.request("GET", url.replace("{page}", str(page)))
  with open('school-' + str(page) + '.json', 'w') as f:
    print(response.text, file=f)


# with open('page1.json', 'w') as f:
#     print('here goes page 111', file=f)

#
# response = requests.request("GET", url)
# print(response.text)
```
## Easter egg Code (Billy)
- This code gives an example of how embedding was used in this easter egg page.
```
<h2> How our project relates to College Board</h2>
<li>College board requirements: https://apcentral.collegeboard.org/pdf/ap-computer-science-principles-2021-create-performance-task-scoring-guidelines.pdf</li>
<iframe height="500px" width="300%" src="https://docs.google.com/document/d/1KuVEQKO4vod8RELblmBYNGX1hycmg6xARQu5i1R0tbs/edit" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
<h3> Who am I in Computer Science?</h3>
<h3> Billy</h3>
<iframe height="500px" width="300%" src="https://docs.google.com/document/d/1-4_LNqjEzu4XzEIR3LJe44UwOqnq9JtpCC5kK2A2CCI/edit" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<h3> Lola</h3>
<iframe height="500px" width="300%" src="https://docs.google.com/document/d/15b3xgcVgTHbtVvusDHCTwOTVEN_03TTAL60cbxbmlwM/edit" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<h3> Valerie</h3>
<iframe height="500px" width="300%" src="https://docs.google.com/document/d/18q2dMFWUwg-MGMfykfqJoBkHspU-ADS05f5b_OvS7M8/edit" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<h3> Michael</h3>
<!--<iframe height="500px" width="300%" src="(insert link here)" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>-->

```
## MC page (Lola)
- This code is an example of the usage of Post and how we were able to show the questions and submit button on to this page.
```{% if question_index == data|length - 1 %}
<form action="/submit" method="post">
{% else %}
<form action="/next" method="post">
{% endif %}

  <div class="question">
  <div class="question_text">{{ data[question_index].question }}</div>
    {% for answer in data[question_index].answers %}
      <div class="question_answer">
        <label>
          <input type="radio" name="answer" value="{{ answer.index }}" onclick="onSelectQuestion(event)">
          {{ answer.text }}
        </label>
      </div>
    {% endfor %}
    <input type="hidden" name="next_question" value="{{ question_index + 1 }}">
    <input type="hidden" name="answers" value="{{ answers }}">
    {% if question_index == data|length - 1 %}
    <input type="submit" value="Submit" class="button" disabled>
    {% else %}
    <input type="submit" value="Next" class="button" disabled>
    {% endif %}
  </div>
</form>

<script>
  function onSelectQuestion(event) {
    document.querySelectorAll('.button').forEach((button) => {
      button.removeAttribute('disabled');
    });
    const answersInput  = document.getElementsByName('answers')[0];
    const answersObj = JSON.parse(answersInput.value);
    answersObj['{{question_index}}'] = event.currentTarget.value;
    answersInput.value = JSON.stringify(answersObj);
```
## Rasberry pi (Michael)
- This project runs off of a rasberry pi
```
Rasberry Pi
```
# Tickets completed throughout the Project
### Crossover Tickets
| Name  |      Goal      |  Acomplished |
|----------|-------------|------|
| Billy | Work on the database| Was able to complete the database by finding more attributes in the API like websites and adress. Was able to succsesfully print these attributes in terminal in a table with lables. This code was replaced on by the valeries new database and api code. |
| Valerie |  Keep working on the database  |   Switched from SQL Alchemy to SQL Lite because it fits better with what we are trying to accomplish with our project. Was able to find a better API and create a new database for the group.   |
| Lola | Work on the MC page |  Created questions that related to Valerie's new Api code on the Multiple Choice oage. Updated the page and was able to make the next button work better. |
|  Michael  |  Work on rasberry pi code   | Ras pi code  |

### Ticket/Easter Egg (Info/Link)
| Name  |      Goal      |  Acomplished |
|----------|-------------|------|
| Billy | Create the Easter Egg page | Was able to create the easter egg page and a secret easter egg button that can be found on the home page. In the Easter egg page, there is an implementation of embedding from Trimester one of APCSP and a Who am I in APCSP?" assignment for each teammember. Easter egg link: http://104.2.87.139:8080/easteregg/ . ***Code is featured in Project code snippets***|
| Valerie | Work on the database | Creation of a new database is needed and a search for a New API is needed aswell because the API we have right now doen't have enough information about the schools. Started the process of a SQL lite database instead of the SQL Alchemy database that we used before. |
| Lola | Work on MC Page and Feed back Page | Was able to create the multiple choice questions on the MC Page and get the MC questions to work. Now what is needed is the questions to be connected to the database and then the MC page will be complete.|
| Michael   |  Rasberry Pi    |  Runs off a Rasberry Pi     |

### First Big Ticket
***Our Big ticket website video*** 
-since deployment didn't go as planned, a 2 minute video was created to show you the big ticket items for this week.
https://youtu.be/LaLQzCo173c
| Name   |   Goal   |  Accomplished |
|----------|-------------|--------|
| Billy | Database work | Was able to start the base code of the MySQL database. Still a long ways to go to get the database to work. |
| Valerie|  Find an API |  Found an API that has mediocre attributes about the college. College attributes in the api: Location, website, name, mascot, school colors, adress, etc. |
| Lola| Work on MC Page and Feedback Page | Was able to create the MC and Feedback page for the website. Also was able to come up with the questions for the feedback page and the MC page.  |
| Michael | Run website off Virtual Box   |  Wasn't able to accomplish this with Mr. Mortensen's help, instead Mr. Mortensen gave him another week to run the website off the Rasberry Pi    |


### Scrum master ticket grading
Evidence and links to code are in the project board 
- Valerie 19/20- searched for and found api databases/ upgraded the home page with carousol
- Michael 19/20- Worked on deploying the website. 
- Lola 19/20 - Created feedback page questions/ worked on Quiz questions page.
- Billy 17/20- Worked on database and create.py to define
### Justification for grading
Scrum Board has the official Tickets and is names of people assigned to each ticket.
Scrum board link: https://github.com/valeriemiliteeva/BeakersTorts/projects/1
- multiple choice questions created on the questions page.                          
- Feed back page created; user is able to input their thoughts on our page
- api databases collected and ready to connect to the database

# Final Project Delivery Plan
## Fridays
Every Friday the scrum group will meet up for atleast 5 minutes to discuss plans for the future and any possible assignments assigned to each scrum member over the weekend. 
## Midterm
Midterm is finished. So far what is done is:
- the creation of the SQL Database
- the api was found and connected to the database
- feedback page in progress (front end finished)
- quiz page in progress (nearly finished)
- Web page running off of a rasberry pi
## Night at the Museum
### goals:
- Finish the backend for MC page
- Finish the UI for MC page
- Finish the ReadMe
- Update the Rasberry Pi

## College Board
To meet and exceed College Board requirements, this project will include a SQL Database,Web scraper, will be a deployed Web Site on Raspberry Pi server, and will be way more advanced than the websites created from trimester 1.

College board requirements for project: https://apcentral.collegeboard.org/pdf/ap-computer-science-principles-2021-create-performance-task-scoring-guidelines.pdf

