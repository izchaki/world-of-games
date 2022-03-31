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
    env:
    - name: docker_user_name
      valueFrom:
        secretKeyRef:
           name: j-jenkins-additional-secrets
           key: docker-user-name
    - name: docker_password
      valueFrom:
        secretKeyRef:
           name: j-jenkins-additional-secrets
           key: docker-password

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
                       docker build . -t izchaki/my-flask:build-by-jenkins
                                                """
        }
      }
    }
    stage('test') {
      steps {
        container('docker') {
          sh """
                       docker rm mf
                       docker run --name mf izchaki/my-flask:build-by-jenkins bash start.sh
                                                """
        }
      }
    }
     stage('push') {
      steps {
        container('docker') {
          sh """
                      docker login -u izchaki -p Doer24295548
                      docker push izchaki/my-flask:build-by-jenkins
                      echo $docker_user_name
                      echo $docker_password
                                                """
        }
      }
    }
  }
}
