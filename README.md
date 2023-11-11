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
- Error Page Not Found 404 when adding the LoginRequiredMixin to classes PostCreate, PostUpdateView and PostDeleteView, as login_url was not found initially, as I have added the html page for login. After checking the error page, I found the login_url is looking into URL patterns, so I've added '/accounts/login/' as the login_url and the page worked, redirecting unlogged users to the login page.
<br>
<img src="static/assets/images/accountserror.jpg" alt="creating a table of content for comments">
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
- Home Page
<br>
Home page performs as expected, displaying a list of posts, with a short excerpt of the article, highlight it when hovered over
<br>
<img src="static/assets/images/homePage.jpg" alt="home page of the blog">
<br>
-The users can Register or login to their accounts. Once registered or logged in, the LogOut tab is showing. When users register, or login/logout, a successfull message is displayed:
<br>
<img src="static/assets/images/SignUp.jpg" alt="register page">
<img src="static/assets/images/registerMessage.jpg" alt="register comfirmation message">
<br>
<img src="static/assets/images/SignInMessage.jpg" alt="sign in message">
<img src="static/assets/images/signedOutMessage.jpg" alt="signed out message">
<img src="static/assets/images/signOutConfirm.jpg" alt="signed out comfirmation">
<br>
- Create. Edit. Delete
<br>
<img src="static/assets/images/CreateEditDelete.jpg" alt="edit create and delete buttons">
<br>
- The users have the option to create a post, once logged in. They can also delete or edit a post, but only if they are the authors of the post. All three features work as expected, reverting to the sign in page in case user is not logged in, trowing a Forbbiden page in case a user who is not the author is trying to edit or delete a post.
<br>
<img src="static/assets/images/LoginToCreatePost.jpg" alt="reverted to login page">
<img src="static/assets/images/EditPostError.jpg" alt="edit post error">
<img src="static/assets/images/EditPostAdmin.jpg" alt="allowing to edit a post for a user">
<img src="static/assets/images/deletePostAdmin.jpg" alt="allowing to edit a post for a user">
<br>
- All users, once logged in, are allowed to create a new post. Once the post is created, the user is reverted to the home page, where the latest post will be displayed first.
<br>
<img src="static/assets/images/AddPost.jpg" alt="adding a post">
<img src="static/assets/images/AddPostResult.jpg" alt="results of a new post">
<br>
- Comments
<br>
<img src="static/assets/images/Comments.jpg" alt="comments section">
<br>
- Once logged in, users can leave a comment on a certain post. To do so, they need to open the detailed page of a post and scroll at the bottom and use the Comment section. The username will be pulled into the form. All comments will be submitted for approval on the admin side. Once approved, they will be displayed at the bottom of that post.
<br>
<img src="static/assets/images/CommentsApproval.jpg" alt="comments approval request">
<br>
- Contact Us page
<br>
<img src="static/assets/images/ContactUs.jpg" alt="contact us page">
<br>
- Any user can contact the admin page through a Contact us form. Once the user leaves their details, the message is sent to the admin pannel.
And the user is directed to a success message page confirming his message was submitted.
<br>
<img src="static/assets/images/ContactUsAdmin.jpg" alt="contacts admin panel page">
<br>
<img src="static/assets/images/ContactUsSuccess.jpg" alt="contact us success message">
<br>
- Like feature
<br>
<img src="static/assets/images/LikeButton.jpg" alt="the heart icon to like a blog post">
<br>
- Each post has a heart icon to like it. Once users are logged in, they can press the heart to like the post. 
This also works to revers it, pressing it again will unlike the post, giving the user control over this, in case they change their mind.
<br>
<img src="static/assets/images/LikeButtonOn.jpg" alt="actioned like button">
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
- Sarah in Tutor assistance from Code Institute. <br>
- geeksforgeeks.org forum for creating UpdateView and DeleteView classes https://www.geeksforgeeks.org/class-based-generic-views-django-create-retrieve-update-delete/
- learndjango.com forum for restricting permision to edit or delete post to authors only
