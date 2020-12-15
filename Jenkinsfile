pipeline {
    agent any
    stages {
        stage('Building') {
            steps {
                sh 'python -m venv venv'
                sh 'venv/bin/python -m pip install -r requirements.txt'
                sh 'venv/bin/python setup.py install'
            }
        }
        stage('Testing') {
            steps {
                sh 'venv/bin/python setup.py pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo deploying'
            }
        }
    }
}
