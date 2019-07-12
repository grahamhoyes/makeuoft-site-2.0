pipeline {
  agent any
  environment {
    DB_CREDENTIALS = credentials('DB_USER')
  }
  stages {
    stage('Build') {
      steps {
        sh '''#!bin/bash
          #Delete existing docking image
          docker rmi --force makeuoft-site:latest
          #Build new image
          docker-compose -f deployment/docker-compose.yml build
        '''
      }
    }
    stage('Deploy') {
      when {
        branch "master"
      }
      steps {
        sh '''#!bin/bash
          #Bring down the old container
          docker-compose -f deployment/docker-compose.yml down
          #Bring up the new container
          docker-compose -f deployment/docker-compose.yml up
        '''
      }
    }
  }
}
