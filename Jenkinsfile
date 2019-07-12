pipeline {
  agent any
  environment {
    DB_CREDENTIALS = credentials('DB_USER')
  }
  stages {
    stage('Build') {
      steps {
//          #Delete existing docking image
          sh 'docker rmi --force makeuoft-site:latest'
//          #Build new image
          sh 'docker-compose -f deployment/docker-compose.yml build'
      }
    }
    stage('Deploy') {
      when {
        branch "master"
      }
      steps {
//          #Bring down the old container
          sh 'docker-compose -f deployment/docker-compose.yml down'
//          #Bring up the new container
          sh 'docker-compose -f deployment/docker-compose.yml up -d'
      }
    }
  }
}
