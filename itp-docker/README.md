Note that this folder is called "itp-docker", so that the letters ITP (IT-Project) are used to create the docker network.
Otherwise it would be called "docker", which wouldn't be so cool, as it might clash with other projects.

Open the firewall:

    firewall-cmd --zone=public --permanent --remove-port=40001/tcp
    firewall-cmd --zone=public --permanent --add-port=40001/tcp
    firewall-cmd --reload
    firewall-cmd --list-all

Startup the services:

    # go into docker folder in this project (ie here)
    docker-compose up -d

Create the database and change the password, and create a temporary table for testing:

    docker run -it --rm mysql mysql -h maxant.ch --port 40001 -u root -p -e "CREATE DATABASE timesheets CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
    docker run -it --rm mysql mysql -h maxant.ch --port 40001 -u root -p

    ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
    ALTER USER 'root'@'%' IDENTIFIED BY 'new_password';
    FLUSH PRIVILEGES;

    create table temp (id integer auto_increment, name varchar(100), primary key (id) );
    insert into temp values (null, 'Ant');
    select * from temp;

    exit;

Set the password into the environment permanently so that continuous deployment works.

    echo "MYSQL_PASSWORD=<the password>" >> /etc/environment

logout/login for that to take effect.

