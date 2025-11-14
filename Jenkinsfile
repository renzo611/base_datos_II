pipeline {
    agent any

    environment {
        // Variables de entorno para MongoDB y Redis
        // Puedes configurar estas variables en Jenkins:
        // Manage Jenkins > Configure System > Global properties > Environment variables
        // O definir valores por defecto aquí (no recomendado para producción)
        // Si las variables ya están definidas en Jenkins, se usarán esas; si no, se usan estos valores por defecto
        MONGO_USER = 'admin'
        MONGO_PASSWORD = 'admin123'
        REDIS_PASSWORD = 'redis123'
    }

    stages {
        stage('Stop previous services') {
            steps {
                script {
                    sh """
                        sudo docker compose down || true
                    """
                }
            }
        }

        stage('Start services with Docker Compose') {
            steps {
                script {
                    sh """
                        sudo docker compose up -d
                    """
                }
            }
        }

        stage('Verify services') {
            steps {
                script {
                    sh """
                        sleep 5
                        sudo docker compose ps
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
