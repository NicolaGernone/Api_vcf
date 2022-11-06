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

The api spec are illustrated in the postman collection and the api.spec.yaml
