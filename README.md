# Online Journal

Welcome to the Online Journal app! This is a functional website that allows you to keep track of the topics you are reading and learning about.

This app is built with Django, a powerful web framework for Python. It is part of a full stack portfolio project with Code Institute, designed to showcase your skills as a full stack developer.

With the Online Journal app, you can easily add and track the topics you are learning about, as well as make notes and comments on your progress. Whether you're a student, professional, or lifelong learner, this app is a great tool for staying organized and motivated.

We hope you enjoy using the Online Journal app!

![App Screenshot](learning_logs/static/images/am-i-responsive-img.jpg)

[View the live project here](https://online-journal2022.herokuapp.com/ "Link to deployed site - Online Journal")

## Table of contents
1. [UX](#UX)
    1. [User Stories](#User-Stories)
    2. [Design](#Design)
2. [Features](#Features)
    1. [Existing Features](#Existing-Features)
    2. [Features to Implement in the future](#Features-to-Implement-in-the-future)
3. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     2. [Additional Languages Used](#Additional-Languages-Used)
     3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
4. [Testing](#Testing)
     1. [Testing](TESTING)
5. [Deployment](#Deployment)
     1. [Deploying on Heroku](#Deploying-on-Heroku)
     2. [Forking the Repository](#Forking-the-Repository)
     3. [Creating a Clone](#Creating-a-Clone)
6. [Credits](#Credits)
     1. [Content](#Content)
     2. [Media](#Media)
     3. [Code](#Code)
7. [Acknowledgements](#Acknowledgements)
***
## UX 

### User Stories
#### Users
1. As a **user** I want to **log in the topic I have interest in** as a **way of tracking and revisiting information.**
2. As a **site user** I can **add a new topic** about a subject I'm interested in. 
3. **I can view a post's entirety** as a **site user** by **clicking on it.**
4. As a **site user** I can **delete** entries.
5. As a **site user** I can **edit the entries I've previously added.**
6. As a **site user** I can **login to the website with the username and password I used for registration.** 
7. I can **create** an account as a **user** of the site.
8. As a **site user** I can **sign up for the newsletter**


#### Site Admin:
1. As a **site Admin**, I can **restrict access to Topics page.**
2. As a **site Admin**, I can **modify the appearance and layout of the app** to make it more user-friendly and visually appealing.
3. As a **site Admin** , I can **create and manage categories or tags** to help users organize and classify their topics.
4. As a **site Admin** , I can **enable or disable features or functionality within the app** to customize the experience for users.

#### Users
1. As a user of the Online Journal app, you have the ability to log in the topics you have an interest in. This feature allows you to easily track and revisit the information you are learning about, helping you stay organized and focused on your goals.

     To log in a topic, simply navigate to the appropriate section of the app and enter the topic you are interested in. You can then add notes and comments about your progress as you learn more about the topic.

     The ability to log in and track your interests is a key feature of the Online Journal app, and it is designed to make it easy for you to stay organized and focused on your goals. Whether you are a student, professional, or lifelong learner, this feature can help you get the most out of your learning experience. So, it will be very helpful for you to use this feature and make the most out of it. 
2. As a user of the Online Journal app, you have the option to create new entries for subjects that interest you. This feature allows you to easily track your progress and revisit information as you learn.

     To create a new entry, simply navigate to the appropriate section of the app and enter the subject you are interested in.
3. As a site user of the Online Journal app, you have the ability to view the entirety of a post by clicking on it. This allows you to easily read and review the information you have logged about a particular topic.

     To view a post in its entirety, simply click on the post title or summary. This will open the full post, allowing you to read through all of the details and notes you have entered.
4. As a site user of the Online Journal app, you have the ability to delete entries that you no longer need or want to track. This feature allows you to keep your journal organized and focused on the topics that are most important to you.

     To delete an entry, simply navigate to the appropriate section of the app and locate the entry you wish to delete. You can then use the delete function to remove the entry from your journal.
5. As a site user of the Online Journal app, you have the ability to edit the entries you have previously added. This feature allows you to make updates or changes to your journal as your learning progresses.

     To edit an entry, simply navigate to the entry section of the app and locate the entry you wish to edit. You can then use the edit icon to make changes to the entry.
6. As a site user of the Online Journal app, you have the ability to log in to the website using the username and password you used during registration. This feature allows you to access your personal journal and track your learning progress.

     To log in, simply enter your username and password into the appropriate fields on the login page. Once you have logged in, you will be able to access your journal and use all of the features of the app.
7. As a user of the Online Journal app, you have the ability to create an account on the site. This allows you to access the features of the app and track your learning progress.

     To create an account, simply navigate to the registration page and enter your desired username, password and your email.

8. To sign up for the newsletter, users can visit the website and scroll to the bottom of the page to find the newsletter sign-up form in the footer. Users can enter their name and email address and click the "Sign up" button to submit their sign-up request. They will see a message confirming that they have successfully signed up for the newsletter. This feature allows users to stay informed about updates and new features on the Online Journal app, and helps the app team to connect with their users and gather feedback.

#### Site Admin:
1. As the site administrator of the Online Journal app, you have the ability to restrict access to the Topics page. This allows you to control which users are able to view and edit the topics in the app.

     To restrict access to the Topics page, you can use the app's built-in user management and permissions system. This system allows you to specify which users are able to access the page and which actions they are able to perform.

     The ability to restrict access to the Topics page is a useful feature for the site administrator, allowing you to control who can view and edit the topics in the app. This can be useful for maintaining the integrity and accuracy of the information in the app, as well as for managing access to sensitive or confidential information. So, it will be very helpful for you to use this feature and make the most out of it.
2. As the site administrator of the Online Journal app, you have the ability to modify the appearance and layout of the app to make it more user-friendly and visually appealing. This allows you to customize the look and feel of the app to better meet the needs and preferences of your users.

     To modify the appearance and layout of the app, you can use the app's built-in design and customization tools. These tools allow you to change things like the color scheme, font styles, and layout of the app to create a more cohesive and visually appealing experience for users.
3. As the site administrator of the Online Journal app, you have the ability to create and manage categories or tags to help users organize and classify their topics. This feature allows you to create structured categories or tags that users can use to classify and organize their posts and notes within the app.

     To create and manage categories or tags, you can use the app's built-in categorization and tagging tools. These tools allow you to create new categories or tags, assign them to specific posts or notes, and manage the organization of the app's content.
4. As the site administrator of the Online Journal app, you have the ability to enable or disable features or functionality within the app to customize the experience for users. This allows you to control which features and functionality are available to users, helping you tailor the app to the needs and preferences of your audience.

     To enable or disable features or functionality within the app, you can use the app's built-in feature management tools. These tools allow you to turn specific features on or off, as well as customize the behavior and functionality of the app.
### Design

 #### Colour Scheme

 Below is the colour scheme used in this project. 
 
- Lavender Web <span style="color: #dedef3;">&#x25A0;</span>
- Black <span style="color: #000000;">&#x25A0;</span>
- White <span style="color: #ffffff;">&#x25A0;</span>
- Light Gray <span style="color: #d3d3d3;">&#x25A0;</span>

How the colors have been used in this app:

Lavender Web (#dedef3) - This is a soft, muted shade of purple that was used as a background color for the journaling app. Its calming nature can help users focus and relax while writing.

Black (#000000) - Black is a classic color that was used for text and other design elements in the journaling app. It is a strong, bold color that can help create contrast and make text stand out.

White (#ffffff) - White is a clean, bright color that was used as the background color for the journaling app. It can help create a sense of openness and clarity, and make text and other elements easy to read.

Light Gray (#d3d3d3) - This is a soft, muted shade of gray that was used for text and other design elements in the journaling app. It is a neutral color that can help create a calming, focused atmosphere.

Overall, the colors in this palette are chosen to be non-distracting and calming, which can help users focus on journaling and writing. They also create a clean, uncluttered look that can help users feel organized and in control.

#### Typography

The **Sura** font is a geometric sans-serif font designed by Carolina Giovagnoli. It is a modern and clean font with a straightforward, no-nonsense design. The geometric shapes and clean lines of Sura give it a strong, futuristic look that is ideal for technology-focused projects. Sura was used for headings and other spotlight elements to create a clean, modern look.  For the body font I choose **Merriweather**. Merriweather is a serif font that is clean and modern, with a slightly more formal and traditional feel than Sura. I used it to provide a nice contrast to Sura's strong, geometric style.


#### Wireframes

Balsamiq has been used to create wireframes for this project. 

Index page 
![App Screenshot](learning_logs/static/images/index.jpg)

Base page 
![App Screenshot](learning_logs/static/images/base.jpg)

Login page 
![App Screenshot](learning_logs/static/images/login.jpg)

Register page 
![App Screenshot](learning_logs/static/images/register.jpg)

Topics page 
![App Screenshot](learning_logs/static/images/topics.jpg)

Topic page 
![App Screenshot](learning_logs/static/images/topic.jpg)

Add new topic page 
![App Screenshot](learning_logs/static/images/topic.jpg)

Add new entry page 
![App Screenshot](learning_logs/static/images/new-entry.jpg)


## Features

1. Topic tracking and revisiting - Our app allows users to log in topics they are interested in as a way of tracking and revisiting the information. This feature is useful for users who want to keep track of their interests and learn more about specific subjects.

2. Adding new topics - Our app allows users to add new topics about subjects they are interested in. This feature is useful for users who want to explore new areas of knowledge and share their interests with others.

3. Viewing full post - Our app allows users to view the entirety of a post by clicking on it. This feature is useful for users who want to read more about a specific topic or get a better understanding of the information being presented.

4. Deleting entries - Our app allows users to delete entries they no longer need or want. This feature is useful for users who want to keep their journal organized and free of clutter.

5. Editing entries - Our app allows users to edit entries they have previously added. This feature is useful for users who want to update or revise their journal entries as they learn more about a subject.

6. Logging in with a username and password - Our app allows users to login to the website using the username and password they used for registration. This feature is useful for users who want to access their journal from multiple devices or locations.

7. Creating an account - Our app allows users to create an account to access the journaling features. This feature is useful for users who want to create a private space to reflect on their thoughts and feelings.

### Design Features

1. Navbar with login/logout options - Our app has a navbar at the top of the screen that includes a login/logout option for logged-in users. This allows users to easily access their account and manage their session.

2. App name in navbar - The name of the app is displayed on the right side of the navbar, making it easy for users to identify the app and navigate to different areas of the site.

3. Jumbotron for registration - The landing page of our app includes a jumbotron that allows users to register for a new account. This feature is prominently displayed to make it easy for new users to get started with the app.

4. Search button and list of topics - After logging in or registering, users can access a search button that shows them a list of topics. This feature allows users to easily browse and find topics they are interested in.

5. Button for adding new topics - At the bottom of the list of topics, there is a button that allows users to add a new topic. This feature is useful for users who want to explore new areas of knowledge and share their interests with others.

6. Topic entries page - After clicking on a specific topic, users are taken to a page where they can view the topic's entries. This page also includes options to edit or delete entries, allowing users to manage their journal and keep it organized.

7. Alert messages - Every time a topic is edited, a message is displayed to inform the user of the update. This helps users stay informed about changes to their journal and allows them to easily track their progress.

### Features to Implement

- Liking system: Allow users to like and save articles or topics that they find particularly interesting or useful.

- Commenting system: Allow users to leave comments or feedback on articles or topics, either publicly or privately.

- Sharing functionality: Allow users to share articles or topics with their friends or colleagues via social media or email.

- Customizable font: Allow users to change size and style of the text on the website so that it is easier for individuals to read.

- View analytics data about website usage:  Allow admin to view analytics data about website usage so he can understand how users are interacting with the website. 

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks - Libraries - Programs Used
- [Django](https://www.djangoproject.com/)
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [ElephantSQL](https://www.elephantsql.com/)
- [Heroku](https://dashboard.heroku.com/login)
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")

# Testing

## Index ??? Table of Contents

* [Automated Testing](#automated-testing) 
* [Manual Testing](#manual-testing) 
* [User Stories Testing](#user-stories-testing)
* [Responsiveness Testing](#responsiveness-testing)
* [HTML Testing](#html-testing)
* [CSS Testing](#css-testing)
* [Python Testing](#python-testing)
* [Lighthouse Testing](#lighthouse-testing)


## Automated Testing
Automated unit testing was done within Django.

|  App              | Component     | Test                                                                                   | Test Outcome  |
|-------------------|---------------|----------------------------------------------------------------------------------------|---------------|
|  online_journal   | Urls          | Test that the admin URL works and redirects to the correct page                        | PASS          |
|  online_journal   | Urls          | Test that the users URL works and redirects to the correct page                        | PASS          |
|  online_journal   | Views         | Test that the home page view works and renders the correct template                    | PASS          |
|  learning_logs    | Urls          | Test that the home page URL works and redirects to the correct page                    | PASS          |
|  learning_logs    | Urls          | Test that the all topics URL works and redirects to the correct page                   | PASS          |
|  learning_logs    | Urls          | Test that the specific topic URL works and redirects to the correct page               | PASS          |
|  learning_logs    | Urls          | Test that the new entry URL works and redirects to the correct page                    | PASS          |
|  learning_logs    | Urls          | Test that the edit entry URL works and redirects to the correct page                   | PASS          |
|  learning_logs    | Urls          | Test that the delete entry URL works and redirects to the correct page                 | PASS          |
|  learning_logs    | Views         | Test that the home page view works and renders the correct template                    | PASS          |
|  learning_logs    | Views         | Test that the view for showing all topics works and renders the correct template       | PASS          |
|  learning_logs    | Views         |Test that the view for showing a specific topic works and renders the correct template  | PASS          |
|  learning_logs    | Views         |Test that the view for introducing a new topic works and renders the correct template   | PASS          |
|  learning_logs    | Views         |Test that the view for introducing a new topic works and renders the correct template   | PASS          |
|  learning_logs    | Views         |Test that the view for adding a new entry works and renders the correct template        | PASS          |
|  learning_logs    | Views         |Test that the view for editing an entry works and renders the correct template          | PASS          |
|  learning_logs    | Views         |Test that the view for deleting an entry works and renders the correct template         | PASS          |
|  learning_logs    | Forms         |Test that the topic form requires the name field                                        | PASS          |
|  learning_logs    | Forms         |Test that the entry form requires the text field                                        | PASS          |
|  users            | Urls          |Test that the logout URL works and redirects to the correct page                        | PASS          |
|  users            | Urls          |Test that the logout view works and redirects to the correct page                       | PASS          |
|  users            | Views         |Test that the logout view works and redirects to the correct page                       | PASS          |

## Manual Testing

|  Test Label                                   | Action         | Expected Outcome                                          | Test Outcome  |
|-----------------------------------------------|----------------|-----------------------------------------------------------|---------------|
|    Register Jumbotron                         | Page load      |  Visible on homepage                                      | PASS          |
|    Login button in navigation bar             | Page load      |  Visible on homepage                                      | PASS          |
|    Login functionality                        | User input     |  Successful login redirects to homepage                   | PASS          |
|    User greeting in navbar                    | User input     |  Correctly displays "Hello, [username]"	               | PASS          |
|    Search button                              | User input     |  Opens list of topics when clicked	                    | PASS          |
|    Topic list                                 | User input     |  Each topic is clickable                                  | PASS          |
|   "Add New Topic" button                      | User input     |  Redirects to new topic form when clicked                 | PASS          |
|   New topic form                              | User input     |  Accepts user input and adds new topic to list            | PASS          |
|   Entry list on specific topic page           | User input     |  Displays list of entries with dates                      | PASS          |
|   Edit entry button                           | User input     |  Redirects to form for editing entry                      | PASS          |
|   Delete entry button                         | User input     |  Redirects to "Are you sure?" page and removes entry      | PASS          |
|   Django messages+Bootstrap alert             | User input     |  Displays alert after making changes                      | PASS          |

## User Stories Testing

| #  | As a/an     | I want to be able to...                    | So that I can...                            | Achieved on...                             |
|----|-------------|--------------------------------------------|---------------------------------------------|--------------------------------------------|
| 1  | User        | log in to the website                      | access my account and topics                | Login page                                 |
| 2  | User        | add a new topic                            | track and revisit information               | New topic form                             |
| 3  | User        | view a post's entirety                     | learn more about a topic	               | Post details page                          |
| 4  | User        | delete entries                             | remove incorrect or outdated information    | Entry delete confirmation page             |
| 5  | User        | edit entries                               | update or correct information               | Entry edit form                            |
| 6  | User        | create an account                          | access the website and track topics         | Register page                              |
| 7  | Site Admin  | restrict access to Topics page             | control user access to certain content      | Topics page                                |
| 8  | Site Admin  | modify the appearance and layout           | improve the user experience                 | App pages                                  |
| 9  | Site Admin  | create and manage categories or tags       | help users organize and classify topics     | Categories/tags management page            |
| 10 | Site Admin  | enable or disable features or functionality| customize the experience of the user        | when the enable/disable feature is used    |


## Responsivness Testing
The app has been tested in Chrome with developer tools and showed to be fully responsive. In addition to Chrome developer tools the app has also been tested across other devices and browsers using [BrowserStack Live](https://live.browserstack.com/dashboard).
- Mozzila Firefox 108 on Mac Ventura 

![App Screenshot](learning_logs/static/images/firfefox-mac-img.jpg)

- Microsoft Edge 108 on Mac Ventura 

![App Screenshot](learning_logs/static/images/microsoft-edge-mac.jpg)

- Opera 94 on Mac Ventura 

![App Screenshot](learning_logs/static/images/opera-mac.jpg)

- Microsoft Edge 108 on Windows 

![App Screenshot](learning_logs/static/images/windows-edge.jpg)

- Samsung Galaxy S8 

![App Screenshot](learning_logs/static/images/galaxyS8.jpg)

- Samsung Galaxy S22 on Chrome 

![App Screenshot](learning_logs/static/images/galaxyS22-chrome.jpg)

- Iphone 13 mini 

![App Screenshot](learning_logs/static/images/iphone13-mini.jpg)

- Safari on iPad Pro 12.9 2022

![App Screenshot](learning_logs/static/images/ipad.jpg)


### Lighthouse Testing

- Lighthouse testing for mobile devices

![App Screenshot](learning_logs/static/images/lighthouse-mobile.jpg)

- Lighthouse testing for pc

![App Screenshot](learning_logs/static/images/lighthouse-pc.jpg)

## HTML Testing


| HTML document    | Result | Issues found                                                            | Fixes made                                                            |
|----------------  |--------|-------------------------------------------------------------------------|-----------------------------------------------------------------------|
| messages.html    | Fail   |1. Non-space characters found without seeing a doctype first.            |1. Added a DOCTYPE declaration at the beginning of the HTML code       |
|                  |        |2. Element head is missing a required instance of child element title.   |2. Added a title element inside the head                               |
|                  |        |3. Bad value True for attribute aria-hidden on element span.             |3. Change the value of the aria-hidden attribute to "true" (lowercase) |
| index.html       | Pass   |                                                                         |                             
| login.html       | "Info" |1. Trailing slash on void elements has no effect                         |1. Delete trailing slash
| base.html        | Pass   |                                                                         |
| topics.html      | Pass   |                                                                         |
| topic.html       | Fail   |1. Element div not allowed as child of element ul in this context.       |1. Wrap div element in li element
| edit_entry.html  | Pass   |                                                                         |
| delete_entry.html| Pass   |                                                                         |
| new_topic.html   | Fail   |1. Element div not allowed as child of element button in this context.   |1. Remove a element
| delete_topic.html| Pass   |                                                                         |
| disclaimer.html  | Pass   |                                                                         |
| footer.html      | Pass   |                                                                         |
| new_entry.html   | Pass   |                                                                         |
| newsletter.html  | Pass   |                                                                         |
| tandc.html       | Fail   |1. No p element in scope but a p end tag seen.                           |1. Remove p tag
| logout.html      | Pass   |                                                                         |
| register.html    | Fail   |1. End tag p implied, but there were open elements.                      |1. Could not fix, the p tag inside django template  |
|                  |        |2. Unclosed element span.                                                |2. Could not fix, span element inside django template                               |
|                  |        |3. Stray end tag span.                                                   |3. Related to first issue, p tag included in django template |
|                  |        |4. No p element in scope but a p end tag seen.                           |4. Could not fix, included in django template as well  |


## CSS Testing

The app's CSS file was tested using W3C CSS Validator. The CSS was free of errors and passed the validation process.

<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

In addition to using the W3C CSS Validator, the app's CSS was also manually tested by visually inspecting the app's pages in various web browsers to ensure that the styles were being applied correctly and consistently across different devices and platforms.

# Deployment

## Deploying-on-Heroku

To deploy this project on Heroku, the following steps were taken:

1. Create a new app on Heroku and choose a name and location for it.
2. In the Resources tab, add a Postgres database to the app by selecting the "Heroku Postgres" option under add-ons.
3. In the Settings tab, reveal the Config Vars and copy the url next to DATABASE_URL.
4. In the project's GitPod workspace, create an env.py file and add the DATABASE_URL and SECRET_KEY values to it.
5. Update the project's settings.py file to import the env file and add the SECRET_KEY and DATABASE_URL file paths.
6. Update the Config Vars with the Cloudinary URL, and also update the settings.py file with this URL.
7. In the settings.py file, add Cloudinary to the INSTALLED_APPS list, and add values for STATICFILE_STORAGE, STATICFILES_DIRS,   
   STATIC_ROOT, MEDIA_URL, DEFAULT_FILE_STORAGE, and TEMPLATES_DIR.
8. Update the DIRS in TEMPLATES with the TEMPLATES_DIR value, and update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost'].
9. Create media, storage, and templates directories in the main project directory, and add a Procfile with the following content: "web: gunicorn project-name.wsgi".
10. Log in to Heroku using the terminal and run the command "heroku git:remote -a your_app_name_here" to link the app to the GitPod workspace.
11. To deploy new versions of the app, run the command "git push heroku main" in the terminal

## Forking the Repository

1. Make sure you have a GitHub account. If you don't have one, you can create an account by going to https://github.com and following the prompts.
2. Go to the GitHub page for the repository you want to fork.
3. In the top right corner of the page, click the "Fork" button. This will create a copy of the repository in your account.
4. You can then clone the repository to your local machine by following the steps in the "Creating a clone" section above, replacing USERNAME with your own GitHub username and REPOSITORY with the name of the repository.
5. Once you have a copy of the repository on your local machine, you can make changes to it and commit those changes back to your fork on GitHub. You can also create a pull request to submit your changes to the original repository for review.

It's generally a good idea to keep your fork up to date with the original repository by regularly syncing your fork with the upstream repository. To do this, you can add the original repository as an upstream repository and then use the git pull command to sync your fork with the upstream repository.

## Creating a clone

1. Make sure you have Git installed on your local machine. You can check if you have it installed by running the command git --version in your terminal.
2. Navigate to the directory where you want to create a copy of the repository.
3. Run the command git clone https://github.com/USERNAME/REPOSITORY.git, replacing USERNAME with the username of the repository owner and REPOSITORY with the name of the repository. In this specific case (https://github.com/marosan28/online-journal.git) This will create a copy of the repository in a new directory with the same name as the repository.
4. Change into the new directory by running the command cd REPOSITORY, replacing REPOSITORY with the name of the repository.
5. Run the command git branch to see a list of available branches in the repository.
6. To switch to a specific branch, run the command git checkout BRANCHNAME, replacing BRANCHNAME with the name of the branch you want to switch to.

# Credits

## Content 

For finding website content I was using [Google](https://www.google.com)

## Media
For creating the website logo I used [Canva](https://www.canva.com/hr_hr/)

## Code
I used [this](https://pylessons.com/django-subscribe) tutorial for creating a newsletter form


# Acknowledgements

- Python crash course book by Eric Matthes
- Slack community
- Tutor support
- WebDevSimplified YouTube channel

