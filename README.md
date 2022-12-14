# Api_vcf
The aim of this API is to **load a dataset contained in vcf in the DB and manipulate data**
Api Rest implemented with basics Http methods: Post, Get, Put, Delete.
Retrive, update and delete data from database.
The Database Records are read and stored from vcf file.
The Arquitecture used is Hexagonal, DDD based.

## Usage

The Api use docker to run the server.
In the [Makefile](/Makefile)

- First Step:

In the [Makefile](/Makefile) under loaddatavcf change the vcf file name with the new one, and make sure that is contained in the Api_vcf or puth the relative path with the name.

In the terminal cd in Api_vcf repository and run the command `make first`.
This command will build the docker and make all the migrations and run the server.
It will load the vcf record in the DB too. Maximum record of 5000.
the server run in localhost:5050.
For next times you will up the application use `make up`.

- Second Step:

Create a super user running `make user`.
after this you will be able to enter in the admin page **localhost:5050/admin**
In the admin page you can manage the data loaded and the users and the Tokens for Authorization.

## Api endpoints

- GET: localhost:5050/data/<id>
- POST: localhost:5050/update/
- PUT: localhost:5050/update/<id>
- DELETE: localhost:5050/delete/<id>
  
- TOKEN: loclahost:5050/api-token-auth/  add { username: your_user, password: user_password }
