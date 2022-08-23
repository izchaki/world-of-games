# World Of Games!

CONTENTS OF THIS FILE
---------------------

* [Introduction](#Introduction)
* [Requirements](#Requirements)
* [Installation](#Installation)
* [Configuration](#Configuration)
 
 INTRODUCTION
------------

This project is about creating three games that we can play with them via the command line:
  - Memory Game
  - Guess Game
  - CurrencyRoulette
  
  After pushing to your repo, jenkins will start a pipeline to check if everything works, and pushing the new image to
  your dockerHub registry.
  
  ( I deleted my username and changed my password so the push stage will fail.)

REQUIREMENTS
------------

This Project requires the following dependencies:

 * [docker](https://docs.docker.com/engine/install/ubuntu/)
 * [kubectl](https://kubernetes.io/docs/tasks/tools/)
 * [helm](https://helm.sh/docs/helm/helm_install)
 
INSTALLATION
------------
 deploy jenkins:
```sh
helm repo add jenkins https://charts.jenkins.io
helm repo update
git clone https://github.com/izchaki/world-of-games
cd world-of-games
deploy jenkins with my jenkins-statset.yaml:
helm install cj -f ./cd/values/jenkins-statset.yaml jenkins/jenkins
```
(wait for it...)

CONFIGURATION
-------------

#### log in as:
  * username:izchak
  * password:pass@

#### create pipeline:
```
    name: doesn't matter
    Definition: pipeline script from SCM
    SCM:Git
    Repository URL: https://github.com/izchaki/world-of-games
    Credentials: none
     Branch Specifier (blank for 'any'):*/master
     Repository browser:Auto
     Script Path: ci/Jenkinsfile.groovy
```
     
