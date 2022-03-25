pipeline {
    agent { label 'build image' }
    stages {
        stage('Build docker image'){
            steps{
                sh 'docker build -t izchaki/my-flask:from-jenkins-pipeline .'
                sh 'docker login -u izchaki -p Doer24295548'
                sh 'docker push izchaki/my-flask:from-jenkins-pipeline'
                sh 'docker rmi izchaki/my-flask:from-jenkins-pipeline'
            }
        }
    }
}
