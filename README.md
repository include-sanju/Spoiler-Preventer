# Spoiler-Preventer

###### Spoiler Preventer is a tool for easily extracting upcoming air dates of TV shows.

This imdb Webscraper scrapes the imdb site using python, providing the user with the air date of the next episode of their requested TV series, thus enabling the user to easily keep track of their favorite TV shows during their busy work schedules and save themselves from spoilers. 

  - Enter email id and  ","  separated TV series names
  - Recieve a mail from the program with the upcoming air dates of all requested TV series

This project has been made as an assignment for Innovaccer SDE-Intern (Platform) for their Summer Intern Hiring Challenge.

This assignment is currently hosted at <insert link here>

# Built with
- Python3
- BeautifulSoup
- mySQL db
- SMTP library

#  Features

  
  - Now faster with multithreading in python
  - Automatically outputs the closest correct name and specifies the release year of the show (avoids confusion)
  - Displays imdb rating of each show
  - Sorts according to imdb rating (high to low) 
  - Provides with storyline of the show
  
### Sample SQL database
![alt text](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)
# Getting Started
The following instructions will get you a copy of this project up and running on your local machine for development and testing purposes.

# Prerequisites
> [Virtual environment] - Setting up virtual environment
> [Pip] - Installing pip
> [mySQL] - mySQL db
> [Python3]


# Setup project

### Installation Instructions

Spoiler Preventer requires [mySQL]  v8.0+ to run.

Create a virtual environment using these commands

```sh
$ git clone https://github.com/include-sanju/Spoiler-Preventer.git
$ cd https://github.com/include-sanju/Spoiler-Preventer.git
$ virtualenv -p /usr/bin/python3 venv
```
Start the virtual environment by
```sh
$ source venv/bin/activate
```
Install the dependencies and start the server.
```sh
$ pip install -r requirements.txt
```
For running the script

```sh
$ python3 spoilerpreventer.py
```
Enter your own email id and password in the env.py file
```sh
$ EMAIL = <ENTER YOUR EMAIL ID IN STRING FORMAT HERE>
$ EMAIL_PASSWORD = <ENTER YOUR EMAIL PASSWORD IN STRING FORMAT HERE>
```


##

   [Virtual environment]: <https://docs.python-guide.org/dev/virtualenvs/>
   [Pip]: <https://docs.python-guide.org/dev/virtualenvs/>
   [Python3]: <http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/>
   [mySQL]:  <https://www.mysql.com>
   

