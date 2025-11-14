pipeline {
    agent any

    stages {
        stage('Stop previous services') {
            steps {
                script {
                    sh """
                        docker compose down || true
                    """
                }
            }
        }

        stage('Start services with Docker Compose') {
            steps {
                script {
                    sh """
                        docker compose up -d
                    """
                }
            }
        }

        stage('Verify services') {
            steps {
                script {
                    sh """
                        sleep 5
                        docker compose ps
                    """
                }
            }
        }
    }

    post {
        always {
            script {
                echo 'Pipeline ejecutado. Servicios MongoDB y Redis están corriendo.'
            }
        }
    }
}
