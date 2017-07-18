# Recursive-CTE

Checkout this repo, install dependencies, then start the gulp process with the following:

    > git clone https://github.com/Ekluv/Recursive-CTE.git
    > cd Recursive-CTE
    For Backend
    > cd recursive_cte_demo
    > Make a virtual env using command `virtualenv -p python3 .`
    > Activate virtual env using `source bin/activate` in linux
    > pip install -r requirements.txt
    > Create a user for postgres : "createuser <YOUR_DBUSER> --pwprompt"
    > Create a db for the application : "createdb cte_demo"
    > Set password for the database : <DB_PASSWORD>
    > Now change postgres info in settings.py
       > change POSTGRES_APP_DB_USER to <YOUR_DBUSER>
       > change POSTGRES_APP_DB_PASSWORD TO <DB_PASSWORD>
    > python manage.py migrate
    > python manage.py runserver(Make sure port is 8000. default is 8000)
    
    For frontend
    > cd frontend
    > npm install
    > npm start
    
    Or 

Download the .zip file. Extract the contents of the zip file, then open your terminal, change to the project directory, 
and the same as above.
