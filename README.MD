### Intstall postgres

    apt install -y postgresql postgresql-contri
    sudo -i -u postgre
    exi
    adduser webdaugia
    sudo -u webdaugia psq
    history

### All for data

    python manage.py flush
    python manage.py createsuperuser
    python manage.py runserver

### Add data to mode Fee

    INSERT INTO daugia_memberfee(ID, fee) VALUES (1, 'Paid');
    INSERT INTO daugia_memberfee(ID, fee) VALUES (2, 'Unpaid');
