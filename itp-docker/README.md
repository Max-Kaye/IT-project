Note that this folder is called "itp-docker", so that the letters ITP (IT-Project) are used to create the docker network.
Otherwise it would be called "docker", which wouldn't be so cool, as it might clash with other projects.

Open the firewall:

    firewall-cmd --zone=public --permanent --remove-port=40001/tcp
    firewall-cmd --zone=public --permanent --add-port=40001/tcp
    firewall-cmd --reload
    firewall-cmd --list-all

Startup the services:

    # go into docker folder in this project (ie here)
    docker-compose up &

Create the database:

    docker run -it --rm mysql mysql -h maxant.ch --port 40001 -u root -p -e "CREATE DATABASE timesheets CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
    docker run -it --rm mysql mysql -h maxant.ch --port 40001 -u root -p
