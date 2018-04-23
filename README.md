# dreamjob
This is a Django Project that incorporates Vue jS as its Template Engine.

Installing This Project to your local Machine is Easy can be done at a click..

Installation Instructions
1. You must make sure you have python installed on your system, as this appilication was built on top of the Language.
To do this head over to https://www.python.org/downloads/windows/ and download Python 3+ version compatible with your system, if your using a windows OS.  Python comes pre-installed with Ubuntu and Mac OS so ther wont be any need for futther installation.

2. Once Python has been Succesfully installed on your system, open your command prompt and type:  pip install virtualenvwrapper-win.
This installs a virtual enviroment on your System.

3. Download/ Clone the project and unzip.

4. Using your Favourite Editor(Sublime text/ Atom) or ide(Eclipse, Netbeans, PyCharm) that supports Python Modules open the dreamjobs project

5. On your command Prompt Terminal and  input in the following commands(NB: This must be from the project path)

	a. mkvirtualenv env //This create a Virtual Enviroment Seperate from your system to run the django process
	b. workon env // This activates the enviroment
	c. pip install -r requirements.txt //This install all the necessary requiremnets needed to run django on your system
	d. python manage.py migrate // This creates an sql database 
	e. python manage.py createsupersuer //This creates and admin user at the backend with can be accessed via http://127.0.0.1/admin
	f. python manage.py runserver //This runs and deploys the project and can be accessed via http://127.0.0.1 on your local machine

6. Enjoy the prowess on Django and VueJS


