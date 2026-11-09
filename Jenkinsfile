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
                bat 'mkdir out'
                bat 'javac -d out AddNumbers.java'
            }
        }

        stage('Run') {
            steps {
                bat 'java -cp out AddNumbers'
            }
        }
    }
}