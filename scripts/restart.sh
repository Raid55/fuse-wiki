#!/bin/bash

sudo stop fuse_api-prod
sudo service nginx restart
sudo start fuse_api-prod 
