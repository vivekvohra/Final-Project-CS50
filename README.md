# Final-Project-CS50

#### Video Demo:  <https://youtu.be/IXOy0vf_DNk>

### Description:
iPlus Code, a personal blogging platform designed specifically for tech enthusiasts. It's a space where you can share your passions, connect with like-minded individuals, and foster a vibrant community.

The technology stack used :

* HTML, CSS, and JavaScript: The foundation of our platform, ensuring a responsive and interactive user experience.

* Bootstrap: A popular framework for creating visually appealing and mobile-friendly designs.

* Flask: A lightweight Python web framework that powers iPlus Code, providing a scalable and efficient backend.

* CS50x sqlite3 : Cs50's own sqlite3 for interacting with the database,making data management efficient and reliable.

#### Key Features

* User-Friendly Interface: Intuitive design and easy navigation for a seamless blogging experience.Using bootstrap framework,the site is mobile-friendly and is web responsive. Bootstrap is a popular library (that comes with lots of CSS classes and more) via which you can beautify your site. For this webpage layout I used bootstrap template on which the website is futher build.<div>
My pre-written website has a three-part series blogpost. It uses bootstraps power to its fullest .The next/previous button, the page button, column for author introduction, insertion of the pictures responsively, insertion of table etc. all uses bootstrap or html with css styling.  
* Learning Opportunities: Discover new technologies and trends through the diverse content shared on the platform.
* User Authentication: Login/Logout and Registration: Users can easily create accounts, log in, and log out securely. This ensures that only authenticated users can access certain features of the platform.I used this feature from cs50 finance.The user data is stored in users table in finance.db.To ensure that the password safe we used encryption in the hash column.So only when correct username and password is inputted we can access the site.In case of new user we must register them.<div>
  Login is implemented in several parts:
  * Form Submission: Users submit their username and password via a form in the login.html page.
  * Database Query: The server queries the users table in finance.db database to find the user with the provided username.
  * Password Verification: The server verifies the provided password against the hashed password stored in the database.The password is checked against the stored hash using a function that compares the plaintext password provided by the user with the hashed password stored in the database.Here we did it by using check_password_hash function from the werkzeug.security module.
  * Session Management: If the credentials are correct, the server sets a session variable to keep the user logged in.To implement this we first need to import  request, session from flask.To keep track of the logged in user we use user_id session variable which is unique and autoincremented. This variable is set to the user's unique ID from the database when they successfully log in.In this way the server can identify the user in the following requests.
  Logout simply uses Session Clearing :
  * When a user logs out, the server clears the session data by using the session.clear() method. This removes all data stored in the session, effectively logging the user out.
* Dynamic Content Management:Users can add new blog posts, which will dynamically update on the website. This feature allows for real-time content sharing and engagement.We achived it by using form in add.html and sending it to route in app.py through action button.In app.py in /add route we add the contents of the form into our database with sqlite3 using post method.<div> 
                            Our Home page is then updated automatically,as we use jinja's for function to loop through the posts; so that the cards can increase according to the number of posts available in the database.We also used inheritance as our basic style was similar. I used 2 template i.e- tamplate.html and template2.html both of them provides basic structure for the newly added blog page and the login/logout and register page respectively.<div>
                            Our new posts our created using combination of template inheritance and jinja templating. We use /post/<string:post_slug> route with get method and rendering into post.html. Where we use jinja templating of {{post.content}} and template inheritance to create that instance of static webpage.

* Contact Us Page: The platform includes a contact page where users can submit their information. This data is stored in the database, facilitating easy communication and feedback collection.We achived it by using form in contact.html and sending it to route in app.py through action button.In app.py in /contact route we add the contents of the form into our database with sqlite3 using post method.We can see the contents in the database using phpLiteAdmin.
* SEO Optimization in iPlus Code:Keyword Optimization: iPlus Code allows users to incorporate relevant keywords into their blog posts this is done by slug. By researching and using popular search terms related to your content, you can improve your blog’s ranking on search engines. The platform provides tools to help identify and integrate these keywords effectively.<div>
Meta Tags and Descriptions: Each blog post has pre written meta tags and descriptions, which are essential for SEO. Meta tags provide search engines with information about the content of your page, while meta descriptions offer a brief summary that appears in search results. Properly optimized meta tags and descriptions can significantly boost your blog’s visibility.<div>
Responsive Design: iPlus Code’s use of HTML, CSS, and Bootstrap ensures that your blog is mobile-friendly and responsive. Search engines prioritize websites that offer a seamless experience across all devices, so a responsive design can improve your search rankings.

My final project folder is futher has 2 folder i.e Static and Templates with python and Database Files:
 * Static Assets: contain images used in the website, such as blog post thumbnails;styles.css: This file contains the CSS styles that define the appearance and layout of your website.
 *  HTML Templates:<div>
index.html: This is the main template for the homepage, which might display a list of posts and other content.<div>
contact.html: This template would contain the form for users to submit contact information.<div>
post.html: This template display newly added blog posts with details like title, content, author.<div>
login.html: This template would contain the login form.<div>
register.html: This template would contain the registration form.<div>
layout.html/layout2.html: This template might define the overall layout and structure of your web pages, including headers, footers, and navigation menus.<div>
add.html: This file likely contains the HTML form for users to add new posts to the application.<div>
apology.html: The template should include a message indicating that an error occurred, along with any additional information or instructions.<div>
about.html: This file typically contains information about your application, its features, and its creators.<div>
blog1.html/filter_c.html/helper_c.html : these are the static web blogs.<div>
* Python Files:
app.py: This file contains the main Flask application, including routes, database interactions. It's the core of the web application.<div>
helpers.py: This file contain helper functions used throughout the application, such as authentication logic,apology/error logic.<div>
* Database File:
  reads.db/finance.db: This file stores the database data for your application, such as user information, blog posts, and contacts.

Join iPlus Code Today

Embark on your blogging journey with iPlus Code and become part of a thriving community of tech enthusiasts. Share your knowledge, learn from others, and make your mark in the tech world. Sign up now and start creating content that inspires and connects.

