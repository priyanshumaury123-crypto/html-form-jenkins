pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/priyanshumaury123-crypto/html-form-jenkins'
            }
        }

        stage('Test HTML Form') {
            steps {
                sh 'python3 -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }
        failure {
            echo 'FAILURE: Check the console output for errors.'
        }
    }
}
