pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up environment...'
                // Instalar dependencias globales si es necesario
                sh '/opt/homebrew/bin/pip3 install -r requirements.txt'
            }
        }

        stage('Build') {
            parallel {
                stage('Build Trivia') {
                    steps {
                        echo 'Building Trivia module...'
                        // Instalar dependencias específicas de Trivia
                        sh '/opt/homebrew/bin/pip3 install -r Trivia/requirements.txt'
                    }
                }
                stage('Build USQL') {
                    steps {
                        echo 'Building USQL module...'
                        // Instalar dependencias específicas de USQL
                        sh '/opt/homebrew/bin/pip3 install -r USQL/requirements.txt'
                    }
                }
                stage('Build SistemaPedidos') {
                    steps {
                        echo 'Building SistemaPedidos module...'
                        // Instalar dependencias específicas de SistemaPedidos
                        sh '/opt/homebrew/bin/pip3 install -r SistemaPedidos/requirements.txt'
                    }
                }
            }
        }

        stage('Generate Documentation') {
            parallel {
                stage('Generate Trivia Documentation') {
                    steps {
                        echo 'Generating Trivia documentation...'
                        // Generar el archivo trivia.html
                        sh 'python generar_documentacion.py --module Trivia --output Documentacion/DocumentacionTrivia/trivia.html'
                    }
                }
                stage('Generate USQL Documentation') {
                    steps {
                        echo 'Generating USQL documentation...'
                        // Generar el archivo USQL.src.usql_parser.html
                        sh 'python generar_documentacion.py --module USQL --output Documentacion/DocumentacionUSQL/USQL.src.usql_parser.html'
                    }
                }
                stage('Generate SistemaPedidos Documentation') {
                    steps {
                        echo 'Generating SistemaPedidos documentation...'
                        // Generar el archivo Main.html
                        sh 'python generar_documentacion.py --module SistemaPedidos --output Documentacion/DocumentacionSistemaPedidos/Main.html'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Ejecutar la aplicación Flask en segundo plano
                sh 'nohup python app.py &'
                // Esperar un momento para asegurarse de que el servidor esté en ejecución
                sleep 5
                // Mostrar la URL local
                echo 'Application running at http://127.0.0.1:5000'
            }
        }
    }
}
