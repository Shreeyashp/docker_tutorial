#### FROM python:3.7
This will be downloaded FROM doker repo and in python=3.7 whatever will be tags in it  will be downloaded

#### COPY . /app
copy . means whatever will be there in local folder it will copy in app folder and this app folder will be present in docker image
. means basically all the files in folder, 
app means destination folder & this destination folder will go in docker image {app name can be anything, depend on us}

#### WORKDIR /app
Its required to run pip install -r ___, if workdir is not present this it will give us error

#### RUN pip install -r requirements.txt
we have to install all library dependencies because of that we need to run this command

#### CMD ["python","app.py"]
In case we need to run app.py, so we added python app.py in cmd [command line]

#### Docker cheatsheet:
https://dockerlabs.collabnix.com/docker/cheatsheet/


#### docker build -t <image_name> . 
image-name depend upon us what we have to keep let image-name here shreeyash_app

#### docker -d -p host port:container port <image-name>
docker -d -p 5000:8000 shreeyash_app

#### docker ps 
To check whichever image are running

#### docker stop <container-id>
To stop docker 

#### doctor build -t <username/image-name> 
To run/fetch locally in your system 
username suppose shreeyashpardeshi , image-name = shreeyassh_app

#### docker push <username/image-name>:latest
For example: docker push shreeyashpardeshi/shreeyassh_app:latest
:latest is version info
you can run this in your cmd
after completing above run, then try to run this docker -d -p 5000:8000 shreeyashpardeshi/shreeyassh_app
after this you can also try to run through port in chrome suppose i.e 127.0.0.1:8000


