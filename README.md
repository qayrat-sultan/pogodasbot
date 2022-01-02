Weather tg sender
============

Telegram bot sending channel weather info

:License: MITa

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------


* Terminal command::

    $ nano /etc/environment
* Write token::

    $ token_pogodas="12345678:TOKEN"
    
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

    systemctl enable fonlinebot
    systemctl start fonlinebot

For example
--------------
https://t.me/pogodas
