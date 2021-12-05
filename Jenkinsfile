#!groovy

pipeline {
    agent any

     options {
          buildDiscarder(logRotator(numToKeepStr: '10'))
          timestamps()
     }


     environment {
         DELETE_FOLDER_AFTER_STAGES = 'false'
         DB_ENGINE    = 'sqlite3'
     }

    stages() {
        stage("Building project") {
        
            steps {
                echo "Build number ${BUILD_NUMBER} and ${BUILD_TAG}"

                bat 'python -m venv "${BUILD_TAG}" && \
                    .\ ${BUILD_TAG}/bin/activate && \
                    ${BUILD_TAG}/bin/pip install --upgrade pip && \
                    ${BUILD_TAG}/bin/pip install -r requirements.txt && \
                    python manage.py makemigrations && python manage.py migrate'
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
      }
      }
}