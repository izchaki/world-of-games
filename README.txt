# World Of Games!
## this project is about creating three games:
    * Memory Game
    * Guess Game
    * CurrencyRoulette

deploy jenkins:

helm repo add jenkins https://charts.jenkins.io
helm repo update
git clone https://github.com/izchaki/world-of-games
cd world-of-games
deploy jenkins with my jenkins-statset.yaml:
helm install cj -f ./cd/values/jenkins-statset.yaml jenkins/jenkins

(wait for it...)

username:izchak
password:pass@

create pipeline:
    name: doesn't matter
    Definition: pipeline script from SCM
    SCM:Git
    Repository URL: https://github.com/izchaki/world-of-games
    Credentials:
        create new key:
              username: izchaki10@gmail.com
              password: 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
     Branch Specifier (blank for 'any'):*/master
     Repository browser:Auto
     Script Path: ci/Jenkinsfile.groovy
     
