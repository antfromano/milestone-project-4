<h1 align="center">Milestone Project 4 - ancraft - Ant Romano</h1>

[View the live project here](https://mp4ancraft.herokuapp.com/works/)

An art ecommerce designed using Python, HTML, Python, CSS, JavaScript, Django, Heroku and Amazon S3 to highlight skills learned during Full Stack Software Development coursework.

<h2 align="center"><img src="img/ancraftmultidevicewebsitemockup.jpg"></h2>

## User Experience (UX)

Designed to provide a simple experience for people to purchase unique art while highlighting software development skills.

-   ### User stories

    -   #### Customer

        1. As a customer, I want to browse the available artwork.
        ![Alt text](img/allworksscreenshot.jpg)

        2. As a customer, I want a simple user interface and functional interactivity.
        ![Alt text](img/singleworkscreenshot.jpg)
        
        3. As a customer, I want a recognizable and secure checkout experience.
        ![Alt text](img/checkoutscreenshot.jpg)

        4. As a customer, I want an order summary and confirmation.
        ![Alt text](img/ordersummaryscreenshot.jpg)

-   ### Design
    -   #### Color Scheme
        -   The main colors used are green, red, blue and white to match the art pieces's color pallette.
    -   #### Typography
        -   Balsamiq Sans font is the main font used throughout the whole website.
    -   #### Imagery
        -   Utilized Python, HTML, Python, CSS, JavaScript, Django, Heroku and Amazon S3.

## Features

-   Responsive on all device sizes.

-   Attractive, efficient and interactive elements.

## Features Left to Implement/Other Feature Ideas

-   Customer ability to leave ratings and reviews of art pieces was not implemented due to time constraints complicated by miscommunication between virtual collaborators.

## Technologies

### Languages

-   [Python](https://en.wikipedia.org/wiki/Python)
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs

1. [Django:](https://www.djangoproject.com/)
    - for database.
    
1. [Heroku:](https://www.heroku.com/)
    - for deployment.
1. [Amazon S3:](https://aws.amazon.com/s3/)
    - for Cloud Object Storage.
1. [GitHub:](https://github.com/antfromano/special-slice)
    - as a repository, distributed version-control system for tracking changes and to deploy and host final version of code.
1. [Gitpod:](https://gitpod.io/)
    - as a collaborative development environment.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/) - [Results](https://github.com/antfromano/special-slice/blob/main/docs/Showing%20results%20for%20https___special-slice.herokuapp.com_get_complete_slices%20-%20Nu%20Html%20Checker.pdf)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - [Results](https://github.com/antfromano/special-slice/blob/main/img/Capture.JPG)

Lighthouse was also used to validate the project for performance, accessability, best practices and SEO.

-   [Lighthouse](https://developers.google.com/web/tools/lighthouse) - [Desktop Results](https://github.com/antfromano/special-slice/blob/main/docs/lighthouse%20desktop.pdf)

-   [Lighthouse](https://developers.google.com/web/tools/lighthouse) - [Mobile Results](https://github.com/antfromano/special-slice/blob/main/docs/lighthouse%20mobile.pdf)

### Testing User Stories from User Experience (UX)

-   #### Pizza Diner Goals

    1. As a Pizza Diner, I want to share my favorite pizza.

        1. Upon entering the site, diners are greeted with a simple title, several pizza slices and an Add Slice button which allows them to add a slice.
        2. The Add Slice button is immediately noticeable which leads the diner to the appropriate pagae.
        3. The player can input the style, sauce, cheese, topping and name of the restaurant and hit submit to log their entry.
 
    2. As a Pizza Diner, I want a simple user interface and functional interactivity.

        1. The site has been designed to be simple to navigate. 
        2. Each page is layed out evenly and works cleanly when the items are entered and update, delete and submit are clicked.
        3. The Special Slice title allows the diner to home any time they wish.

    3. As a Pizza Diner, I want a visually appealing experience.
        1. The colors and contracts utilized make the text and buttons stand out.
        2. Flash messages confirm when slices are input, updated and deleted.
        3. The colorful combinations and highlights add to the user experience.

### Further Testing

-   Tested on Google Chrome, Internet Explorer and Microsoft Edge.
-   Viewed on variety of devices such as Desktop, Chromebook and Pixel XL.
-   Testing was done to ensure that all pages linked correctly.
-   Friends and family were asked to review site and documentation for any bugs and/or user issues.
-   Attempted to enter blank entries and was unable to.
-   Tested update, delete and submit buttons extensively.

### Known Bugs

-   Special Slice updates and inputs are sometimes not immediately displayed.
-   Extra data is sent to MongoDB sometimes but doesn't seem to affect program.
-   On some mobile devices the headings aren't fully centered.

## Deployment

### Heroku

Project was deployed to Heroku with the following steps...

1. Log in to Heroku and click the “new” dropdown button on the dashboard and select “create new app”
2. Name your app (the name must be unique) and ensure the correct region has been set for where you are. 
3. Click “create app”.
4. In the terminal in your app type “npm install -g heroku” and hit enter to install Heroku into your app. The “-g” installs Heroku globally across your project. 
5. Log in to Heroku in the terminal by using “Heroku login -I” then input your email address and password for Heroku.

### Forking the GitHub Repository

Forking the GitHub Repository makes an original repository copy on oGitHub account for viewing and/or making changes but not affecting original repository achieve with the following steps.

1. Log in GitHub and locate [GitHub Repository](https://github.com/)
2. At top of Repository, locate "Fork" Button where there is now a copy of original repository.

### Making a Local Clone

1. Log in GitHub and locate [GitHub Repository](https://github.com/)
2. Under repository name, select "Clone or download".
3. For cloning repository using HTTPS copy the link under "Clone with HTTPS".
4. Open Git Bash and modify current working directory to location of your preferred cloned directory.
5. Input `git clone`, and paste copied URL from Step 3.

```
$ git clone https://github.com/antfromano/special-slice
```

6. Press Enter. Local clone is created.

```
$ git clone https://github.com/antfromano/special-slice
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   [Materialize:](https://materializecss.com/) used to make site responsive.

-   [Mini Project](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/08-SearchingWithinTheDatabase/01-text_index_searching): Mini Project concepts used to develop match site.

### Content

-   All content was written by the developer.

-   The format for README.md was taken from [here](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md)


### Acknowledgements

-   Mentorship and guidance provided by Aaron Sinnott from Code Institute

-   Tutor support at Code Institute for their support.

-   I received inspiration for this project from [Amyh97](https://github.com/Amyh97)