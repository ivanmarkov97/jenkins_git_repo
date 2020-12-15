pipeline {
    agent any
    stages {
        stage('Building') {
            steps {
                sh 'python -m venv venv'
                sh 'chmod 777 venv/bin/activate'
                sh 'ls -lah'
                sh 'venv/bin/python -m pip install -r requirements.txt'
                sh 'venvbin/python setup.py install'
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
