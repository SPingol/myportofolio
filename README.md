Name : Serafin Reysetyo Amantresno Grajo Pingol

NPM : 2506637136

Class : PBP KKI

## UPDATE LOGS

05/09/26

- Changed Accent and Accent Dark to blue colour values

06/09/26

- Changed the introduction description

06/09/26 & 07/09/26

- Total overhaul of the main webpage, with new colors and minor layout and component changes
- Changed the introduction description again
- NEW Audio Player added, with 4 different tracks with a audio visualizer for funsies
- NEW Hover Portrait mechanic, hover mouse cursor over portrait to reveal hidden image, for mobile simply click on the portrait to show and hide(also works on PC)
- Mobile optimization and functionality
- Checked and fixed the functionality of the Linkedin, Email and Github buttons

07/09/26

- Minor bug fixes
- Added commments to the index.HTML and style.css
- NEW added Education and Experiences sections, aswell as related sub-sections

13/09/26

- NEW Added new MVT sections to replace static sections
- Bug fixing for MVT sections
- NEW base.HTML template, to be inherted by MVT sections to increase clarity when working, reducing clutter and reucing repetition
- Compatibility changes to ensure certain features continue to work with the inheritance system

## REFLECTION QUESTIONS

### Assignment 1

1. In Tutorial 1 and Individual Assignment 1, you were given the freedom to decide your portfolio website’s design. When you designed the HTML structure you used, did you use semantic HTML5 elements such as section, article, or aside? If so, how did those elements help you build the static web? If not, why did your design’s needs stay met without them?

Yes, I used semantic HTML5 elements like section and article in my design. They were extremely helpful for breaking down the page layout into sections, making the HTML cleaner and much easier to manage. Additionally, it also made it easy to replicate identical pieces of code for certain sections of the wepage, such as the education and experiences section, by having the content be contained within those elements along with their clear indicators.

2. When you set up your CSS to stay responsive, what layout challenges did you encounter? How did you evaluate which elements needed to be repositioned or prioritized in size when moving from the desktop view to mobile?

The main challenge that I faced when setting up the CSS to stay responsive was, turning the 2 column grid format for PC, to a more mobile friendly 1 column layout. Other issues include elements overlapping, the website randomly crashing on mobile upon certain actions etc. The most notable cases being the unique features which I added such as the audio player and the hover mechanic, which needed some extra work to get functioning on mobile since the original design was PC-oriented and did not account for the mobile peculiarites. The way that I evaluated the necessary changes was simply trial and error, by pushing the updates and seeing what works and what broke. This is highly inefficient, as I am not preempting the issues that much, however I lack the experience in web development in general, let alone on mobile, to do such a thing consistently outside of following examples or guides online about such.

3. The website you’ve built right now is a purely static web. What limitations did you feel while trying to present your portfolio’s information optimally? Based on those limitations, what dynamic functionality would you most want to prepare and add in the next iteration of the project?

The greatest limitation is that whenever I want to change some content or description, I have to go into the HTML or css file and manually implement the change and then commit and push to see it, which is very time consuming. Especially since I am quite prone to making typos, and indecisive with wordings, so I like to make frequent changes, this makes the process very tedious and also kind of dangerous as if I'm editing the source files themselves theres a chance I break something somewhere by accident. The main dynamic functionaility I would like to have is viewer-admin priviliges where the viewer can only view the website howver the admin (me) can freely make select changes to the website from the weppage itself, i.e add new education and experience boxes/widgets, edit present descriptions and tags, and also change the colors of the website. Basically makes customising and updating information to the page must easier, requiring fewer direct changes to be made to the files themselves.

### Assignment 2

1. Explain what happens when a user opens the new portfolio page, starting from the request received by the project until the data appears in the browser. In your answer, explain the roles of the project’s urls.py, the application’s urls.py, the view, the model, and the template.

The user sends an HTTP request to the Django server, when they enter the url to open the portofolio page, Django inspects the root URL configuration in the project level urls.py. If there is match with the inputted url path, it delegates routing to the respective application using the include() function.Then, application level routing in main/urls.py receives the remaining path. Django inspects the pattern in the url to find a match and identify the corresponding view function mapped to the incoming url path, such as views.Control moves to the view function in view.py. Acting as the logical controller for the request. The view calls model.py to get the actual content to be displayed. The model uses Django's Object-Relational Mapper (ORM) to communicate with the database to execute the necessary queries to retrieve the data needed for the page and returns them to views as python model packages. The view packages the retrieved model objects with other required variables into a context dictionary. It then calls Django render() function, passing the target HTML template and and context dictionary as arguments. The render() function processes the HTML template using the built-in Django template engine, injecting data dynamically from the context dictionary into the corresponding place holder tags in the template. Producing a HTML string which is automatically wrapped inside a HttpResponse object. The view returns the HttpResponse object to Django's core request handler, transmitting the response to the user's browser via the webserver, which then parses the HTML data and displays the new Portofolio page.

2. Why should the data for the new portfolio section be stored in a model instead of being written directly in the template? Explain how this choice affects application maintenance and future development.

By having the data stored in a model, it makes it much simpler and easier to make changes to the inputted data on the page, without having to manually enter all the new data line by line, using a template instead. Additionally it is much safer since touching the source code always leaves a chance for something to break or an error to occur when executing a change directly. Furthermore by being in a model it makes reusing a template much easier. Overall a much more scalable, reusable and safer method.

3. What is the difference between makemigrations and migrate in Django? Give an example of a model change that requires you to run both commands.

makemigrations generates Python based migration files that are essentially version control blueprints, similar to commits on github, for changes to the database. It does this by inspecting the models.py file and compares it with the existing migration history and packagaes any changes into a new migration file.

migrate on the other hand takes those files and applies them to update the database schema. Executing the unapplied migration files to the configured database backend, running SQL queries to sync the database with the model definitions.

## AI DISCLOSURE

### Assignment 1

For this assignment, AI was utilized strictly as a supplementary tool for minor and mechanical tasks, including code formatting, indentation, adding comments (limited primarily to section headers, while content was written or rewritten by myself), and debugging.Given my unfamiliarity with web development, I also utilized AI to clarify code concepts, explain syntax, and guide the implementation of specific features like audio and hover mechanics, and certain positioning of elements such as boxes. This served to supplement external resources such as YouTube tutorials, Stack Overflow, and W3Schools whenever standard guides could not be directly applied to my project.

All core concepts, design choices, and structural logic remain my own work or originated from the tutorial template.

While helpful, AI presented notable limitations. It could not fully grasp my specific vision for the design, requiring manual tweaks to adapt its suggestions. Additionally, it occasionally generated unsolicited text, descriptions, or extraneous elements that had to be manually removed or rewritten to match my intended design.

### Assignment 2

For this assignment, similarly to the last one, AI was utilized strictly as a supplementary tool for minor and mechanical tasks, including code formatting, indentation, adding comments (limited primarily to section headers, while content was written or rewritten by myself), and debugging.

AI additionally was used to help further understand the syntax needed to implement the MVT structure and preserve some of the unique features I had previously implemented. Though it has to be double checked and cross referenced with other examples, aswell as cautionary testing every other suggested change as it proved unreliable at times and produced odd results.

Ultimately, AI is a useful supportive tool to help with the learning process especially for beginners facing new code that can feel overwhelming. However, it should not be used to completely do the work, as bypassing the process means learning nothing and developing no actual skills. It must remain a tool, not a replacement.
