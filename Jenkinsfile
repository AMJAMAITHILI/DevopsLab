pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'mkdir -p out'
                sh 'javac -d out main.java'
            }
        }
        stage('Run') {
            steps {
                sh 'java -cp out AddNumbers'
            }
        }
    }
}

