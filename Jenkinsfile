pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vaishnaviuttarkar/flaskAppDeployment.git'
            }
        }
        stage('Deploy') {
            steps {
                // Copy the index.html file to the deployment directory
                sh 'cp app.py /var/www/html'
            }
        }
        stage('Verify Deployment') {
            steps {
                sh 'curl http://http://192.168.1.109//app.py | grep -i "Hello, World!"'
            }
        }
    }
}
