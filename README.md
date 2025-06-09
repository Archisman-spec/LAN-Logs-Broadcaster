
# Logs Broadcaster: Minimal LAN Log Monitor

A compact, internal-use Flask-based monitor that streams Linux system logs over LAN with SSL & Auth. 

## Overview
Minimalist internal use tool for streaming Linux journalctl logs over a secured LAN. Eliminates the need to SSH into multiple devices by offering a password-protected, browser-based interface to system logs—perfect for quick monitoring.

Lightweight, web-based wrapper for journalctl. While full containerization of systemd logs was not possible(I couldnt find a way due to systemd's restrictions), Docker is still used to run a secure NGINX reverse proxy with HTTPS.
## Features:
 * Basic Auth + SSL via NGINX for secured LAN access

 * Broadcast logs over LAN to browser clients 

 * Real-time categorized endpoints: kernel, system, user, error, services

 * Use over journalctl: no repeated SSH logins, share logs across LAN securely

 * No terminal tab juggling — just open a browser tab

 * Internal dashboard for dev/test/staging environments
## Setup:
  
  ###### 1. Clone and install requirements 

```bash
  pip install -r requirements.txt
```
  
  ###### 2. Run the Flask server

  ```bash
  gunicorn -w 4 -b 0.0.0.0:5000 --worker-class gevent run:app
```
  
  ###### 3. Generate Auth + SSL (One time setup)

  ```bash
  # Generate .htpasswd
sudo apt install apache2-utils
htpasswd -c nginx/.htpasswd user

 # Create SSL directory
 mkdir -p nginx/ssl

 # Generate self-signed certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout nginx/ssl/nginx-selfsigned.key \
    -out nginx/ssl/nginx-selfsigned.crt
  ```

 ###### 4. Access via Browser
  ```bash
  https://<host-ip>/
```

## Changes in nginx.conf:
 ###### 1. Point proxy_pass to your host IP and Flask port
  ```bash
   location / {
    auth_basic "Restricted Area";
    auth_basic_user_file /etc/nginx/.htpasswd;
    proxy_pass http://<host-ip>:5000;     // Add your host IP
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
  ```
## Limitations:
* Systemd incompatibility with Docker: Since journalctl ties deeply into systemd, containerizing this Flask app isn't viable. Docker containers typically don't have access to the system's /run/systemd or /var/log/journal, which breaks log querying.

* LAN-limited by design: This is intentional — broadcasting system logs publicly is a security risk. LAN deployment ensures tighter control, privacy, and safer monitoring within trusted networks.
