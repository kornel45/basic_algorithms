pipeline {
  agent any
  stages {
    stage('Pull') {
      agent any
      steps {
        sh 'git pull'
        echo 'Pulled'
      }
    }
  }
}