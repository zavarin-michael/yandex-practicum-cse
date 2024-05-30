# yandex-practicum-cse

Web application for yandex cloud practicum "Cloud Services Engineer"

Simple application created with Django. Using this app anyone can post comment by defining name and comment. All data store in YDB.

There are two scripts: `create-replica.sh` and `update-replica.sh`. 
You need to run this scripts like that: `bash <script-name> 'container-name' 'image-version'`
```
bash create-replica.sh 'booking1' '0.0.3'
bash update-replica.sh 'booking1' '0.0.4'
```