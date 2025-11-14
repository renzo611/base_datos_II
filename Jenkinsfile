pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/renzo611/base_datos_II.git'
            }
        }

        stage('Stop previous services') {
            steps {
                script {
                    sh """
                        docker-compose down || true
                    """
                }
            }
        }

        stage('Start services with Docker Compose') {
            steps {
                script {
                    sh """
                        docker-compose up -d
                    """
                }
            }
        }

        stage('Verify services') {
            steps {
                script {
                    sh """
                        sleep 5
                        docker-compose ps
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
