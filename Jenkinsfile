pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'morradbattah'
        DOCKER_HUB_IMG_NAME = 'myapp'
        APP_VERSION = '1.0.0'
        EC2_HOST = '3.135.188.206'
        EC2_USER = 'ubuntu'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION} ."
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: '8ff899f7-a7c0-4bdc-8bee-7a43a6e06226', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        sh "echo ${DOCKER_HUB_PASSWORD} | docker login -u ${DOCKER_HUB_USERNAME} --password-stdin"
                        sh "docker push ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION}"
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'ec2-ssh', keyFileVariable: 'EC2_PEM_FILE')]) {
                        sshagent(['ec2-ssh']) {
                            sh """
                                ssh -o StrictHostKeyChecking=no -i ${EC2_PEM_FILE} ${EC2_USER}@${EC2_HOST} "docker stop \$(docker ps -q) || true && \
                                docker rm \$(docker ps -a -q) || true && \
                                docker rmi \$(docker images -q) || true && \
                                docker pull ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION} && \
                                docker run -d -p 5000:5000 ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION}"
                            """
                        }
                    }
                }
            }
        }
    }
}
