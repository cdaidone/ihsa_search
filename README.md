PythonAnywhere link: http://cdaidone.pythonanywhere.com/

#Introduction
In the spirit of the business mind set, efficiency is what drove the inspiration for this project. As an IHSA team captain, I frequently direct prospective students and riders to the IHSA website to get more information about teams.

However, the "Current Teams" tool currently available on the site doesn't help users besides list the schools alphabetically or by IHSA sanctioned Zone and Region. Unfortunately for new students, they aren't familiar with the Zones and Regions teams are split into.

My solution is to allow users to search by standard geographic region in the United States: Northeast, South, West, and Midwest. Once a region is selected, users can then select the states listed within each region and reveal the teams and their respective coaches within the state selected.

This app was built using HTML, CSS, JavaScript, Python, Flask, Bootstrap, and BeautifulSoup. The database of teams and their relevant information was collected via web scraping.

For reference, IHSA website: http://www.ihsainc.com

***Step 1: Scrape the Data***
I scraped the IHSA website to collect all the Universities with teams, their coaches, and the state they are locate in. (ihsa_site_scrape.py)

This information is written into a CSV file via CSV Dict Writer (schools2.csv).

I used Mr. Data Converter to convert the csv data into a python dict (school_list.py). The regions were created by organizing the states into lists and assigning variables named with the respective regions.

***Step 2: Build App***
The main file of the app is ihsa_app.py. This file holds the functions that allow the app to cycle through the regions, matching the states to the regions, and listing the teams and coaches.

There are four routes: /home, /home/search, /home/search/<region>, and /home/search/<region>/<state_name>.

***Step 3: Templates***
1. Home (home.html):
  - This is a simple landing page with a button that allows the user to advance to the next page.

2. Pick State (pickstate.html):
  - This page features a drop down menu that allows users to choose a region to explore.

  - Using bootstrap, flask, and python, the drop down menu is populated using a for loop that searches through the regions dictionary created in regions.py.        The regions are then placed in a list in the menu.

  - Using flask, the link for each region is customized based on the region the user selects:

      <li><a href="/home/search/{{ region }}">{{ region }}</a></li>

  - A footer is at the bottom of this page with info regarding this project and a link to my GitHub page.

3. Details (details.html):
  - There are 2 parts to this template and 2 different routes feed into it.

  - The first part of this template shows the region chosen and the states associated with the region below it (third route). Also, depending on what region is selected, the container background image changes to reflect the landscape of the region.

    - The changing background image was created through 4 if statements:

        {% if region == "South" %}
        <div class="container" id="c_1">
        {% elif region == "Northeast" %}
        <div class="container" id="c_2">
        {% elif region == "Midwest" %}
        <div class="container" id="c_3">
        {% elif region == "West" %}
        <div class="container" id="c_4">
        {% endif %}

    - The ids are referenced in the CSS where the images are customized to the region.

    - The displayed region is simple, it's written in using Flask: {{ region }}

    - The listed states below the region is created using a for loop that references the variable "states" created in ihsa_app.py and uses flask to write the state: {{ state }}.

  - The second part of this template comes from the fourth route and populates the table with teams and coaches.

      - Above the table, the state selected is printed using Flask, {{ state_name }}.

      - A for loop is used to populate the table. This part was tricky to figure out; I kept using the variable name to reference "team" and "coach." However, row[0] and row[1] ended up working to reference their location.

      - Other problems I encountered:
        - I originally planned on having a footer at the bottom of the details.html page. However, due to the nature of the page structure and varying size container 5 (bottom half of the page, #c_5), having a footer only caused problems. The solution was to move the footer to the pickstates.html page.

        - I was a bit frustrated with the table structure in that I wanted their to be even margins on either side of the table and present the information for Team and Coach evenly. However, this was not realistic since the university names are all different lengths, as well as the coach names, so the rows had to adjust to accommodate for the different lengths. This is noticed most when you change states in a region and you can see "Team" and "Coach" shift horizontally. Perfectionism gave a strong fight on this.

        - An "extra" aspect I was going to add to this tool was to scrape the team websites and link them so that users could click on the university name and be directed to their website. However, several schools didn't have a website, some links were broken, and some have (very evidently) not been updated in years. I chose to bypass this aspect because of the inconsistency. Because of this, the primary purpose of this app remains to allow users to discover teams across the United States based on their geographical location. Users are savvy enough to quickly Google a team today, so I don't think it's too big of a problem.

***Overall Experience***
There were two things I often asked myself when working on this project: "Is this a thing?" and "What do you mean?"

Towards the end of this project, I found myself thinking more logically and asking "what if.." when trying to figure a function out. My intention was to keep this project simple since I knew I wasn't going to have a tremendous amount of time to work on it with the three other exams I had to study for. It was exactly the opposite. While the functionality of the app is quite simple, the code behind it took days. There were some sections of the files that took over five hours to figure out. With python, I discovered that while some of the errors you might come across might be the same that others have faced and solved, no error is exactly alike so it can be difficult to find an exact solution.

As a visual learner, it can be overwhelming when there isn't a step-by-step tutorial on how to do something since that is the most sure-fire way I can immediately understand it. This project had its own challenge for me just because of this, but I found a way to think through functions by writing it out, talking through it and working through the problem that way.
