Weather tg sender
============

Telegram bot sending channel weather info

Running code
--------------

* Terminal command::

    $ mkdir pogoda
    $ cd pogoda
    $ source venv/bin/activate
    $ pip install -f req.txt
    
Installing
--------------


* Terminal command::

    $ nano /etc/environment
    
* Write token from one line::

    token_pogodas="12345678:TOKEN"
    
* Add this bot and change role for Admin

* Write channel link from main.py::

   some_id = "@pogodas"
* Then press CTRL + O -> Enter -> CTRL + X to save. Reboot system:: 

    $ sudo reboot 
  
* On VPS servers create service::

    $ nano /lib/systemd/system/pogodabot.service
    
* Type this command::

    [Unit]
    Description=Weather tg sender bot
    After=network.target

    [Service]
    EnvironmentFile=/etc/environment
    ExecStart=/project/dir/folder/venv/bin/python main.py
    ExecReload=/project/dir/folder/venv/bin/python main.py
    WorkingDirectory=/home/fonlinebot/
    KillMode=process
    Restart=always
    RestartSec=5

    [Install]
    WantedBy=multi-user.target
    
* Then press CTRL + O -> Enter -> CTRL + X to save.
    
* Type this command::

    $ systemctl enable fonlinebot
    $ systemctl start fonlinebot
    
* Edit time send from main.py code line::

    schedule.every().day.at("03:06").do(function_to_run)

For example
--------------
https://t.me/pogodas
