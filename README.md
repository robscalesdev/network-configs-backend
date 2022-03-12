Hosted URL:
https://netconf-backend.herokuapp.com/
https://git.heroku.com/netconf-backend.git
postgresql-silhouetted-97648 as DATABASE_URL
secret key generation: https://djecrety.ir/
CLIENT_ORIGIN: https://robscalesdev.github.io

push to heroku: git push heroku main
to get backend url: heroku open

# Network Configs Frontend
## Description
This app allows users to build a network of devices.

## Important Links
#### Link To Deployed Website
(https://robscalesdev.github.io/network-configs)

#### Link To Frontend Repo
(https://github.com/robscalesdev/network-configs)

#### Link To Backend API
(https://netconf-backend.herokuapp.com/)

## Goals / Unsolved
The end goal is to add the functionality of creating and downloading device configurations in script and YAML format to apply the configurations to a network of devices.
- Need to add devices
- Need to add additional configurations
- Need to add the ability to download files

## Tech
#### Technologies Used

- React
- HTML/CSS
- React Bootstrap
- Javascript

#### Catalog of Routes

Verb         |	URI Pattern
------------ | -------------
GET | /networks
GET | /networks/:id
POST | /networks
PATCH | /networks/:id
DELETE | /networks/:id

#### ERD
User | Model
---- | -----
email | string
password | string

Networks | Model
-------- | -----
address | string
subnet | integer
owner | OtM with User

#### User Stories
As an unregistered user, I would like to sign up with email and password.
As a registered user, I would like to sign in with email and password.
As a signed in user, I would like to change password.
As a signed in user, I would like to sign out.
As a signed in user, I would like to see all of my networks.
As a signed in user, I would like to create a new network.
As a signed in user, I would like to edit an existing network.
As a signed in user, I would like to delete an existing network.

## Directions
- fork and download
- python manage.py makemigrations
- python manage.py migrate

### important URLs
Hosted URL:
https://netconf-backend.herokuapp.com/
https://git.heroku.com/netconf-backend.git
postgresql-silhouetted-97648 as DATABASE_URL
secret key generation: https://djecrety.ir/
CLIENT_ORIGIN: https://robscalesdev.github.io