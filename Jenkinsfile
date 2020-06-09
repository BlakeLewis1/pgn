pipeline{
    agent any

    stages{
        stage('enable all scripts to be executable'){
            steps{
                sh 'chmod +x ./script/*'
            }
        }
        stage('docker swarm stack')
            steps{
                sh './script/docker.sh'
            }