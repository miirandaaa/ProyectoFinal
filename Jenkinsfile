pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up environment...'
                // Crear entorno virtual
                sh 'python3 -m venv venv'
                // Activar entorno virtual e instalar dependencias
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Build') {
            parallel {
                stage('Build Trivia') {
                    steps {
                        echo 'Building Trivia module...'
                        sh './venv/bin/pip install -r Trivia/requirements.txt'
                    }
                }
                stage('Build USQL') {
                    steps {
                        echo 'Building USQL module...'
                        sh './venv/bin/pip install -r USQL/requirements.txt'
                    }
                }
                stage('Build SistemaPedidos') {
                    steps {
                        echo 'Building SistemaPedidos module...'
                        sh './venv/bin/pip install -r SistemaPedidos/requirements.txt'
                    }
                }
            }
        }

        stage('Generate Documentation') {
            parallel {
                stage('Generate Trivia Documentation') {
                    steps {
                        echo 'Generating Trivia documentation...'
                        sh './venv/bin/python generar_documentacion.py --module Trivia --output Documentacion/DocumentacionTrivia/trivia.html'
                    }
                }
                stage('Generate USQL Documentation') {
                    steps {
                        echo 'Generating USQL documentation...'
                        sh './venv/bin/python generar_documentacion.py --module USQL --output Documentacion/DocumentacionUSQL/USQL.src.usql_parser.html'
                    }
                }
                stage('Generate SistemaPedidos Documentation') {
                    steps {
                        echo 'Generating SistemaPedidos documentation...'
                        sh './venv/bin/python generar_documentacion.py --module SistemaPedidos --output Documentacion/DocumentacionSistemaPedidos/Main.html'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Ejecutar la aplicación Flask en segundo plano
                sh './venv/bin/python app.py &'
                sleep 5
                echo 'Application running at http://127.0.0.1:5000'
            }
        }
    }
}
