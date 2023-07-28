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
                    try {
                        sh "docker build -t ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION} ."
                    } catch(Exception e) {
                        echo "Error in building Docker image: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping the pipeline")
                    }
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    try {
                        withCredentials([usernamePassword(credentialsId: '8ff899f7-a7c0-4bdc-8bee-7a43a6e06226', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                            sh '''
                                echo '{ "auths": { "https://index.docker.io/v1/": { "auth": "'$(echo -n ${DOCKER_HUB_USERNAME}:${DOCKER_HUB_PASSWORD} | base64)'" } } }' > ${WORKSPACE}/docker_auth.json
                                docker --config=${WORKSPACE} push ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION}
                                rm ${WORKSPACE}/docker_auth.json
                            '''
                        }
                    } catch(Exception e) {
                        echo "Error in pushing Docker image to Docker Hub: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping the pipeline")
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    try {
                        withCredentials([sshUserPrivateKey(credentialsId: 'dev-ssh', keyFileVariable: 'SSH_PRIVATE_KEY')]) {
                            sh """
                                ssh -o StrictHostKeyChecking=no -i ${SSH_PRIVATE_KEY} ${EC2_USER}@${EC2_HOST} "docker pull ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION} && \
                                docker stop myapp || true && \
                                docker rm myapp || true && \
                                docker rmi ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:current || true && \
                                docker tag ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:${APP_VERSION} ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:current && \
                                docker run -d -p 5000:5000 --name myapp ${DOCKER_HUB_USERNAME}/${DOCKER_HUB_IMG_NAME}:current"
                            """
                        }
                    } catch(Exception e) {
                        echo "Error in deploying to EC2: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping the pipeline")
                    }
                }
            }
        }
    }
}
