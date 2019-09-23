pipeline {
  agent any
  stages {
    stage('Pull') {
      agent any
      steps {
        echo 'Pulled'
      }
    }
    stage('error') {
      steps {
        sh 'pwd'
        sh 'ls'
      }
    }
  }
}