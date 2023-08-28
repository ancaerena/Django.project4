<h1>The Office Fan Page</h1>
<br>
<br>
The Office is a blog for fans of the TV series with the same name.<br>
Users can read articles with facts and other news about the actors from the series.<br> 
They can create an account to leave comments and to like and unlike an article.<br>
Comments are approved in the admin pannel of the webpage.<br>
<br>
<img src="static/assets/images/amiresponsive.jpg" alt="multiple screen sizes diplaying the website">
<br>
<br>
<h2>User stories</h2>
The project has started by establishing the user stories based on the template: As a "site user" I can "action" so that "reward"<br>
The steps followed to create the user stories in Github can be seen below:<br>
1. In the project repository, from the main menu, select Issues<br>
2. Select New Issue from the right-hand side and add a title, starting with USER Stories.<br>
3. Add a description in the Description box, based on the template above.<br>
4. Submit the new issue.
<br>
<img src="static/assets/images/userstoriesinitialboard.jpg" alt="using github issues to create a board">
<br>
There are a total of 10 User Stories for this project, as listed below:<br>
- Manage post<br>
- Display multiple posts on the home page<br>
- Drafted posts<br>
- Leave a comment<br>
- Like/Unlike a post<br>
- Manage comments<br>
- Article/post view<br>
- Create an account<br>
- Engagement<br>
- Comments visability<br>
<br>
<img src="static/assets/images/modelstoriespart1.jpg" alt="using github issues to create a board">
<br>
<br>
<img src="static/assets/images/modelsotriespart2.jpg" alt="using github issues to create a board">
<br>
<br>
<h2>Features</h2>
<hr>
<h3>Existing Features</h3>
<br>
Creating an admin in Django to write drafts and posts, delete articles, approve or delete comments<br>
<img src="static/assets/images/siteadmin.jpg" alt="admin page to manage a website">
<br>
The admin page was updated with search bar, filters and the Draft/Published option for posts. It also gives the option to create posts and approve comments.<br>
<br>
<img src="static/assets/images/djangoadminposts.jpg" alt="admin page to manage a website">
<br>
<img src="static/assets/images/approvingacomment.jpg" alt="admin page to manage a website">
<br>
Along with the Home screen with the display of the posts, there's also a Register/Sign in page, which moves to a Logout page when the user is logged into its account.
<br>
<br>
<img src="static/assets/images/register.jpg" alt="admin page to manage a website">
<br>
<img src="static/assets/images/signin.jpg" alt="admin page to manage a website">
<br>
<br>
<img src="static/assets/images/logout1.jpg" alt="admin page to manage a website">
<br>
<br>
<h2>Database</h2>
<br>
- I have used LucidChart as my ERD Diagram tool to create the database models, as seen below:
<br>
<img src="static/assets/images/databasediagrampost.jpg" alt="creating a table of content for posts">
<br>
<br>
<img src="static/assets/images/databasediagramcomments.jpg" alt="creating a table of content for comments">
<br>
<h3>Features left to implement</h3>
- User profile where the user can view account and add a profile photo<br>
- Search bar for the Home page<br>
- A forum page where users can interact and create topics to discuss<br>
<br>
<h2>Fixed Bugs</h2>
- Portal 800 not rendaring because of a typo in the for loop: for post in posts - error: from posts in posts<br>
- ModuleNotFound error: from .form import CommetForm, corrected: from .forms import CommentForm <br>
<br>
<img src="static/assets/images/error1.jpg" alt="creating a table of content for comments">
<br>
- Error rendering template: missing a ‘,’ in @admin.register(Post)<br>
<br>summernote_fields = ('content',)
<br>
- Error in rendering the template: added an exclamation mark by mistake in an if statement<br>
<br>
<img src="static/assets/images/error.jpg" alt="creating a table of content for comments">
<br>
<br>
<h2>Data Model</h2>
<br>
The code has models, templates and views, working on the Django framework.<br>
There is a base.html to include the navigation bar and the footer, which is then extended in each other html files.<br>
Including a superuser to control the admin panel, the front end has an interactive interface for users to join the fun.<br>
An automatic message was installed to give feedback to the user when interacting with the site.<br>
A JavaScript function is added at the end of the base.html file to make the automatic messaged dissapear after a few seconds.<br>
The workspace was deployed to Heroku at the beginning, leaving for a final deployment when finished<br>
<br>
<h2>Testing</h2>
<br>
- Unfortunatelly, the terminal gave me the error when trying to run my tests: Permission denied to create database.<br>
I have tried installing coverage, but that did not solve the issue. I looked for answers on stackoverflow, <br> but none of the results helped to fix it<br>
Which is why the tests weren't performed, the lack of time didn't allow me to try out things as they were giving other errors.
<br>
<br>
<h3>Validator testing</h3>
<br>
-No errors were returned when passing through the PEP8 Linter - https://pep8ci.herokuapp.com/
<br>
<img src="static/assets/images/piperrors.jpg" alt="creating a table of content for comments">
<br>
<br>
<h2>Deployment</h2>
<br>
- This project had an initial deployment at the beginning to Heroku
<br>
A. Create a new Heroku app:
- Log to Heroku<br>
- On Dashboard, click on New and Create New App<br>
- Add a name to your new app and click create app<br>
<br>
B. Create a database on ElephantSQL.com<br>
- Create an account and create a new instance.<br>
-Select the free Tiny Turtle Plan and select a region.<br>
- Once the instance is created, copy the URL for the database<br>
<br>
C. Create Heroku Vars
<br>
- From Settings, Show Config Vars and add the data base URL, the secret key<br>
-Add the port value 800, the Cloudinary URL after creating a free account.<br>
<br>
D. Link the Heroku app to the repository<br>
- Go to Deploy Tab<br>
- Select Github for Deployment method<br>
- Search for your blog repo <br>
- Select Main as deployed branch and press deploy.<br>
- A new app link will be created. <br>
<br>
The depolyed project can be found here: https://the-office.herokuapp.com/
<br>
<br>
<h2>Credits</h2>
<br>
- Stack Overflow<br>
- Hello Django and I think therefore I blog walkthrough projects from Code Institute<br>
- djangocentral.com<br>