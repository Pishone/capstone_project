## Automation of [OrangeHRM demo site](https://opensource-demo.orangehrmlive.com/) as part of Guvi's capstone project.
![]([https://d36w3vgtkvgnsp.cloudfront.net/53964754958927242995fd73b8194b764123aca6.jpg](http://ww1.prweb.com/prfiles/2013/03/20/10554993/OrangeHRM-logo.png)

The above mentioned site has been automated using Python with Selenium and pytest frameworks. 

This is just for learning purposes.Having said that, if you can improve the functionality of the code, please free feel to fork the repo and make a PR (pull request).

Suggestions are always welcome!


#### How to run the test script to generate your own report? / Check the intergrity of the given report?

### Steps to generate report:

### Pre-requisites
- Clone / Download the entire repo
- Install [Python](https://www.python.org/downloads/)
- Selenium is required but that'll be installed using the requiremnets.txt file, so we'll skip that.
- Download webdriver for your preferred browser.
  - [Firefox](https://github.com/mozilla/geckodriver/releases)
  - [Chrome](https://chromedriver.storage.googleapis.com/index.html?path=109.0.5414.25/)
  - For other browsers, use [duck.com](duckduckgo.com/).

### Next steps
- Run the following command in your preferred shell.
> pip install -r -U requirements.txt

- The above command will install dependensies and upgrade them if any update is available.

- Now, cd into the test_script folder and run the following command.
> pytest -v -s -x test_login.py --capture=sys --html=/home/user/yourworkingdirectory/reports/report_something.html

#### Explanation of the pytest command:

- *pytest* > The framework we use for testing and generating report.
- *-v*  > -v, or --verbose, increases the verbosity level. Use '-vv' to increase level.
- *-s*  > Captures standard output since by default only failed cases show captured output.
- *-x*  > Stop after the first failed test. Use *--maxfail=N* for stopping after N failed cases.
- *--capture=sys* > captures the std Out which is used in report.

### Other usefull flags to improve report

- *-k*  > This option allows you to filter which tests to run, by matching their names against a “keyword expression”
- *--pdb* > makes pytest start PDB, Python’s built-in debugger, when a test fails. Rather than seeing static failure output, you can directly interact with the objects, in the test environment, right at the point of failure.

----------------------------------------------------------------------------------------------------------------------------------------------------------
