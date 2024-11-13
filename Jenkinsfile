pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                // Crear la imagen de Docker usando el Dockerfile en el proyecto
                sh 'docker build -t proyecto_final_flask .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Deploying Docker container...'
                // Ejecutar el contenedor en segundo plano
                sh 'docker run -d -p 5000:5000 proyecto_final_flask'
                sleep 5
                echo 'Application running at http://localhost:5000'
            }
        }
    }
}
