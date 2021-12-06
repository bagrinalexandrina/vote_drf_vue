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
         DELETE_FOLDER_AFTER_STAGES = 'false'
         DB_ENGINE    = 'sqlite3'
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

               junit '**/test-reports/unittest/*.xml'
            }
        }
}