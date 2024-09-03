pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/RaccoonRocket/app-network', branch: 'main')
      }
    }

    stage('') {
      steps {
        sh 'docker --version && docker-compose --version'
      }
    }

  }
}