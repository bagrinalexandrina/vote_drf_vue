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

        stage("Frontend tests") {
            steps {

            }
        }
    }

      post {
          always {

               echo "${BUILD_TAG}"
               echo "${params.PERSON}"
               echo "${params.BIOGRAPHY}"
               echo "${params.CHECKBOX}"
               echo "${params.CHOICE}"
               echo "${params.PASSWORD}"
            
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
              echo "Sending emails"
            emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: "Jenkins Build ${BUILD_TAG}"
              
         }
        }
}