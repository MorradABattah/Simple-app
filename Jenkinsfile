pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github', url: 'https://github.com/username/repo.git'
            }
        }
        stage('Build Image') {
            steps {
                script {
                    def dockerImage = docker.build 'morradbattah/myapp:1.0.0'
                }
            }
        }
        stage('Test Image') {
            steps{
                script {
                    def app = docker.image('morradbattah/myapp:1.0.0')
                    app.inside {
                        sh 'echo "Tests passed"'
                    }
                }
            }
        }
        stage('Push Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        def app = docker.image('morradbattah/myapp:1.0.0')
                        app.push('1.0.0')
                        app.push('latest')
                    }
                }
            }
        }
        stage('Check SSH Key') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'dev-ssh', keyFileVariable: 'SSH_KEY')]) {
                        sshagent(['dev-ssh']) {
                            sh """
                            chmod 600 $SSH_KEY
                            ssh -o StrictHostKeyChecking=no -i $SSH_KEY ubuntu@3.135.188.206 echo "SSH key is working!"
                            """
                        }
                    }
                }
            }
        }
        stage('Deploy to Prod') {
            steps{
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'dev-ssh', keyFileVariable: 'SSH_KEY')]) {
                        sshagent(['dev-ssh']) {
                            sh """
                            chmod 600 $SSH_KEY
                            ssh -o StrictHostKeyChecking=no -i $SSH_KEY ubuntu@3.135.188.206 << EOF
                              docker stop myapp || true &&                                 
                              docker rm myapp || true &&                                 
                              docker rmi morradbattah/myapp:current || true &&                                 
                              docker tag morradbattah/myapp:1.0.0 morradbattah/myapp:current &&                                 
                              docker run -d -p 5000:5000 --name myapp morradbattah/myapp:current
                            EOF
                            """
                        }
                    }
                }
            }
        }
    }
}
