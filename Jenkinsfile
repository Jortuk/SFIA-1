pipeline{
    agent any
    stages{
        stage("Set Up"){
            steps{
                sh 'chmod +x ./script/*'
                sh 'bash ./script/before_installation.sh'
                sh './script/installation.sh'
            }
        }
        stage("Docker-Compose"){
            steps{
                sh 'chmod +x ./script/*'
                sh './scripts/docker.sh'
            }
        }
        
    }
}