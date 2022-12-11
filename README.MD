### Intstall postgres

    apt install -y postgresql postgresql-contri
    sudo -i -u postgre
    exi
    adduser webdaugia
    sudo -u webdaugia psq
    history

### All for data

    python manage.py flush
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

### Add data to mode Fee

    INSERT INTO daugia_memberfee(ID, fee) VALUES (1, 'Paid');
    INSERT INTO daugia_memberfee(ID, fee) VALUES (2, 'Unpaid');

### Add billder for user admin

### Add data starus

    INSERT INTO daugia_status(ID, status) VALUES (1, 'Accept');
    INSERT INTO daugia_status(ID, status) VALUES (2, 'Pending');
    INSERT INTO daugia_status(ID, status) VALUES (3, 'Reject');
    INSERT INTO daugia_status(ID, status) VALUES (4, 'Done');
