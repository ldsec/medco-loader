#!/usr/bin/env bash
./medcoLoader -debug 2 v1 -g /home/jagomes/medco-deployment/configuration-profiles/prod/3nodes-samehost/group.toml --entry 0 --sen ../data/i2b2/sensitive.txt -f ../data/i2b2/files.toml -e \
--dbHost localhost  --dbPort 5434 --dbName i2b2medco --dbUser postgres --dbPassword prigen2017

./medcoLoader -debug 2 v1 -g /home/jagomes/medco-deployment/configuration-profiles/prod/3nodes-samehost/group.toml --entry 1 --sen ../data/i2b2/sensitive.txt -f ../data/i2b2/files.toml -e \
--dbHost localhost  --dbPort 5436 --dbName i2b2medco --dbUser postgres --dbPassword prigen2017

./medcoLoader -debug 2 v1 -g /home/jagomes/medco-deployment/configuration-profiles/prod/3nodes-samehost/group.toml --entry 2 --sen ../data/i2b2/sensitive.txt -f ../data/i2b2/files.toml -e \
--dbHost localhost  --dbPort 5438 --dbName i2b2medco --dbUser postgres --dbPassword prigen2017