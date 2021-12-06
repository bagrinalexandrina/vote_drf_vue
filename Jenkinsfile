#!groovy

pipeline {
    agent any

     options {
          buildDiscarder(logRotator(numToKeepStr: '10'))
          timestamps()
     }
    parameters {
        booleanParam(name: 'CLEAN_WORKSPACE', defaultValue: true, description: 'Clean workspace at the end.')
    }

     environment {
         ON_SUCCESS_SEND_EMAIL = 'true'
         ON_FAILURE_SEND_EMAIL = 'true'
     }

    stages() {
        stage("Building project") {
            steps {
                echo "Build number ${BUILD_NUMBER} and ${BUILD_TAG}"

                bat 'python -m pip install -r requirements.txt && \
                    python manage.py makemigrations && python manage.py migrate'
            }
        }
        stage("Backend tests") {
            steps {
                bat 'python manage.py test'
                junit '**/test-reports/unittest/*.xml'
            }
        }
        stage("Testing frontend") {
            environment { 
                TESTING_FRONTEND=true
            }
            steps {
                bat 'IF "%TESTING_FRONTEND%"=="true" echo "running frontend %TESTING_FRONTEND%"'
            }
        }

    }

    post {
        always {
            echo "${BUILD_TAG}"
            script {
                if (params.CLEAN_WORKSPACE == true) {
                    echo 'Cleaning workspace'
                    cleanWs()
                } else {
                    echo 'Not needing to clean workspace'
                }
            }
        }
        success {
            echo "${currentBuild.currentResult}"
            echo "Sending emails"
        }
    }
}