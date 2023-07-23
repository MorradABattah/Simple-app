pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t myapp:latest .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Shell script to find an available port
                    def portScript = '''
                    for port in {5000..5100}; do
                        if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null ; then
                            continue
                        else
                            echo $port
                            break
                        fi
                    done
                    '''
                    // Run the shell script and get the output
                    def hostPort = sh(script: portScript, returnStdout: true).trim()
                    // Run the Docker container
                    sh "docker run -d -p ${hostPort}:5000 myapp:latest"
                }
            }
        }
    }
}
