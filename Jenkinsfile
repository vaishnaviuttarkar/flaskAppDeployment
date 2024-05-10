pipeline {

    agent any

    stages {

        stage('Git Checkout') {

            steps {

                git branch: 'main', url: 'https://github.com/vaishnaviuttarkar/flaskAppDeployment.git'

            }

        }

      stage("Pushing changes to the remote server"){

            steps {

              script {

                  sh """
                  sudo scp -i /root/secretkey app.py root@192.168.1.108:/root

                  sudo ssh -i /root/secretkey root@192.168.1.108 "nohup python3 /root/app.py > /dev/null 2>&1 &"
                  """

                }

            }

        }

    }

}
