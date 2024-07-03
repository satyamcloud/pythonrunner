this contains a flask application, which gives you the page to enter a python code and execute the python code. The docker image is created and you can use the docker image anywhere to run your application.

1. Install Docker on ubuntu machine
   $ sudo apt install docker.io
   $ sudo systemctl start docker
   $ sudo systemtl enable docker
   $ sudo useradd -aG docker ubuntu
2. Logout and login again to your machine
3. Clone the repository
4. Build the docker image
   $ docker build -t <imagename> .
5. run the image
   $ docker run -d -p 80:5000 <imagename>
6. Check your applicaton in web browser
