pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Obteniendo el código del repositorio...'
                checkout scm
            }
        }

        stage('Verificar Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Verificar Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/python -m pip install --upgrade pip
                    ./venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar Pruebas Python') {
            steps {
                sh './venv/bin/python test_atm.py'
            }
        }

        stage('Construir Imagen Docker') {
            steps {
                sh 'docker build -t atm-python:latest .'
            }
        }

        stage('Ejecutar Pruebas en Docker') {
            steps {
                sh 'docker run --rm atm-python:latest python test_atm.py'
            }
        }

        stage('Finalizado') {
            steps {
                echo 'Pipeline ejecutado correctamente con Python, pruebas y Docker.'
            }
        }

    }
}
