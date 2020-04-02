


    firewall-cmd --zone=public --permanent --add-port=40000/tcp
    firewall-cmd --reload
    firewall-cmd --list-all

    # go into docker folder in this project (ie here)
    docker-compose up
    