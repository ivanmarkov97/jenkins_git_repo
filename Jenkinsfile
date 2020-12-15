pipeline {
    agent any
    stages {
        stage('Building') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'python -m pip install -r requirements.txt'
                sh 'python setup.py install'
            }
        }
        stage('Testing') {
            steps {
                sh 'python setup.py pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo deploying'
            }
        }
    }
}