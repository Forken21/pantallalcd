Linux
Tautulli will be installed to /opt/Tautulli.

Open a terminal.
Install prerequisites:
Ubuntu/Debian: sudo apt-get install git python3.7 python3-setuptools
Fedora: sudo yum install git python3 python3-setuptools
Change directory: cd /opt
Clone Tautulli: sudo git clone https://github.com/Tautulli/Tautulli.git
Add the Tautulli user:
Ubuntu/Debian: sudo addgroup tautulli && sudo adduser --system --no-create-home tautulli --ingroup tautulli
CentOS/Fedora: sudo adduser --system --no-create-home tautulli
Change ownership: sudo chown -R tautulli:tautulli /opt/Tautulli
Copy the service script: sudo cp /opt/Tautulli/init-scripts/init.systemd /lib/systemd/system/tautulli.service
Enable the service: sudo systemctl daemon-reload && sudo systemctl enable tautulli.service
Start Tautulli: sudo systemctl start tautulli.service
Tautulli will be loaded in your browser or listening on http://localhost:8181
Note:
Refer to the instructions in the service file to run Tautulli using a different user or move your Tautulli data to a different location:
https://github.com/Tautulli/Tautulli/blob/master/init-scripts/init.systemd