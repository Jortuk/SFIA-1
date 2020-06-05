pipeline{
    agent any
    stages{
        stage("Make Scripts Executable"){
            steps{
                sh 'chmod +x ./script/*'
            }
        }
        stage("Run Docker-Compose"){
            steps{
                sh './scripts/docker.sh'
            }
        }
        
    }
}