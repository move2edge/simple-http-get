# Configuration

Put any string to data.txt it will be served under GET method at root address /.

Create `.env` file and configure http port e.g. `HTTP_PORT=8000`.

If HTTPS needed configre https port  e.g. `HTTPS_PORT=8443` and put cert.pem and key.pem files to the directory.


# SSL
Ssl `.pem` files should be put into the directory. 
For letsencrypt Android as certificate accepts fullchain.pem.