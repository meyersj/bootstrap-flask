#!/bin/bash
set -e

SCRIPT=$(readlink -f $0)
DIR=`dirname $SCRIPT`

cd $DIR
rm -rf env 
virtualenv env 
env/bin/pip install -r requirements.txt
