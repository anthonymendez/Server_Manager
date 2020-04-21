# From https://www.jamescoyle.net/how-to/1073-bash-script-to-create-an-ssl-certificate-key-and-request-csr

#!/bin/bash

# Required
domain=$1
commonname=$domain

if [ -z "$domain" ]
then
    echo "Argument not present."
    echo "Useage $0 [common name]"

    exit 99
fi

#Change for your details
country="US"
state="Florida"
locality="Fort Lauderdale"
organization="anthonymendez.duckdns.org"
organizationalunit="Development"
email="anthonymendez9@gmail.com"

echo "Generating key request for $domain"

openssl req -x509 -newkey rsa:4096 -keyout key_4096.key -out cert_4096.pem -days 365 -nodes -subj "/C=$country/ST=$state/L=$locality/O=$organization/OU=$organizationalunit/CN=$commonname/emailAddress=$email"


echo "---------------------------"
echo "-----Below is your CSR-----"
echo "---------------------------"
echo
cat cert_4096.pem

echo
echo "---------------------------"
echo "-----Below is your Key-----"
echo "---------------------------"
echo
cat key_4096.key