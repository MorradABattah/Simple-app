pipeline {
    agent any

    environment {
        // Change these to your Docker Hub username and image name
        DOCKER_HUB_USERNAME = 'morradbattah'
        DOCKER_HUB_IMG_NAME = 'myapp'
        APP_VERSION = '1.0.0'
        EC2_HOST = '3.135.188.206'
        EC2_USER = 'ubuntu'
        EC2_PEM_FILE = '~/.ssh/Instance-1.pem'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION}")
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        docker.image("${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION}").push()
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    def remote = [:]
                    remote.name = 'ec2'
                    remote.host = EC2_HOST
                    remote.user = EC2_USER
                    remote.identityFile = EC2_PEM_FILE
                    remote.allowAnyHosts = true

                    sshCommand remote: remote, command: """
                        docker stop \$(docker ps -q) || true && \
                        docker rm \$(docker ps -a -q) || true && \
                        docker rmi \$(docker images -q) || true && \
                        docker pull ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION} && \
                        docker run -d -p 5000:5000 ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION}
                    """
                }
            }
        }
    }
}
