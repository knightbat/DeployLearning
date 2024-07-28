pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'DockerHub'
    }

    stages {
//         stage("build docker image") {
//             steps {
//                 echo "building docker image..."
//                 script {
//                     sh 'docker build -t knightbat/deploy-tutorial .'
//                 }
//             }
//         }
//         stage('Login to Docker Hub') {
//             steps {
//                 script {
//                     docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS) {
//                         echo 'Logged in to Docker Hub'
//                     }
//                 }
//             }
//         }
//         stage('Push to Docker Hub') {
//             steps {
//                 script {
//                     docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS) {
//                         docker.image("knightbat/deploy-tutorial").push()
//                     }
//                 }
//             }
//         }
//         stage('Install Docker Compose') {
//             steps {
//                 sh '''
//                 mkdir -p /var/lib/jenkins/bin/
//                 curl -L "https://github.com/docker/compose/releases/download/v2.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /var/lib/jenkins/bin/docker-compose
//                 chmod +x /var/lib/jenkins/bin/docker-compose
//                 '''
//             }
//         }
        stage('Build and Deploy') {
            steps {
//                 sh '/var/lib/jenkins/bin/docker-compose up -d --build'
                sh 'export MONGO_ADMIN_USER=admin'
                sh 'export MONGO_ADMIN_PASS=admin'
                sh 'docker-compose up -d --build'
            }
        }
    }
}