#!/bin/bash

set -e

DOCKER_IMAGE_TAG=$1


cd bybit-profit-loss

echo "Shutting Down Previous Containers."

sudo docker-compose -f docker-compose-bybit-profit-loss.yaml down

cd ..

echo "Deleting previous directory"

rm -rf bybit-profit-loss

echo "Cloning Repo"

git clone https://github.com/HaynesX/bybit-profit-loss.git

cd bybit-profit-loss

echo "Checkout new version"

git checkout tags/$DOCKER_IMAGE_TAG

echo "Starting Docker Container for Image $DOCKER_IMAGE_TAG"

sudo TAG=$DOCKER_IMAGE_TAG docker-compose -f docker-compose-bybit-profit-loss.yaml up -d


