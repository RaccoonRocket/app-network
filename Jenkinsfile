pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/RaccoonRocket/app-network', branch: 'main')
      }
    }

    stage('Building') {
      steps {
        sh '''docker --version
sudo apt-get install docker-compose
docker-compose --version'''
      }
    }

  }
}