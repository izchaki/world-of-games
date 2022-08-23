pipeline {
  agent {
    kubernetes {
      label 'spring-petclinic-demo'
      defaultContainer 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
metadata:
labels:
  component: ci
spec:
  # Use service account that can deploy to all namespaces
  containers:
  - name: docker
    image: docker:latest
    command:
    - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-sock
  volumes:
    - name: docker-sock
      hostPath:
        path: /var/run/docker.sock
    - name: flask-sock
      hostPath:
        path: /var/run/flask.sock
"""
}
   }
  stages {
    stage('build') {
      steps {
        container('docker') {
          sh """
                       docker build ./ci -t izchaki/my-flask:build-by-jenkins
                                                """
        }
      }
    }
    stage('test') {
      steps {
        container('docker') {
          sh """#!/bin/bash
                       if [ $( docker ps -a | grep mf | wc -l ) -gt 0 ]; then
                            docker rm mf
                       fi
                       docker run --name mf izchaki/my-flask:build-by-jenkins bash start.sh
                                                """
        }
      }
    }
     stage('push') {
      steps {
        container('docker') {
          sh """
                      docker login -u name -p //password
                      docker push izchaki/my-flask:build-by-jenkins
                                                """
        }
      }
    }
  }
}
