pipeline {
  agent {
    node {
      label 'docker-agent-python'
      }
  }
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/RaccoonRocket/app-network', branch: 'main')
      }
    }

    stage('Building') {
      steps {
        sh '''docker --version
ls -la
docker build -t image-app .
docker run -p 5000:5000 image-app
docker ps'''
      }
    }

  }
}
