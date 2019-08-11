# UDACITY - Log Analysis Report

A **python** script that analyses the logs of fictional news website and generates a report. The logs are stored in a **PostgreSQL** database. This is a part Udacity's Full Stack Web Developer Nanodegree. The report was designed to answer the following questions:

1. What are the most popular three articles of all time?

2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?


## Setup

### Prerequisites

On **Windows** you will need a Unix-style terminal. Download and the **Git Bash** terminal [here](https://git-scm.com/download/win)

Download and install the latest version of **Python 2**  [here](https://www.python.org/downloads/release/python-2716/)

Download and install the latest version of **Virtual Box**  [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

Download and install **Vagrant**  [here](https://www.vagrantup.com/downloads.html)

Download the database data (**newsdata.zip**) [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
 

### Virtual Machine Configuration

Launch the terminal (Git Bash on Windows) and download the Vagrant machine configuration by cloning the Full Stack Nanodegree repo from **Git Hub**  [here](https://github.com/udacity/fullstack-nanodegree-vm). You can use the command below:

```git clone https://github.com/udacity/fullstack-nanodegree-vm.git```

Unzip the **newsdata.zip** file that was downloaded previously and place the contents in the **vagrant** directory of the cloned repo

Place the **log-analysis.py** script in this directory as well

From the terminal use ``cd`` to navigate to the **vagrant** directory

Execute the command below to setup a new vagrant machine with the downloaded configuration. This may take a few minutes.

``vagrant up``

Log into the newly setup vagrant machine

``vagrant ssh``
 

### PostgreSQL Database Setup

The vagrant machine configuration comes with **PostgreSQL** pre-installed. Load the data for the report into this database using the following terminal command

``psql -d news -f newsdata.sql``


## Usage

From the running Vagrant machine in the terminal, use ``cd`` to navigate the the **vagrant** direcory containing **log-analysis.py**

Execute the script using the following command

``python log-analysis.py``