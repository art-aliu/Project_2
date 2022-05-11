// pipeline{
//     agent any
//     environment{
//         DOCKERHUB_LOGIN=credentials('DOCKERHUB_LOGIN')
//         DATABASE_URI=credentials('DATABASE_URI')
//     }
//     stages{
//         stage('Testing app'){
//             steps{
//                 sh "bash scripts/tests.sh"
//             }
//         }
//          }
//     stages{
//         stage('Install Dependencies'){
//             steps{
//                 sh "bash scripts/setup.sh"
//             }
//         }

//         stage('Build Images'){
//             steps{
//                 sh "bash scripts/build.sh"
//             }
//         }
//         stage('Configure VMs'){
//             steps{
//                 sh "bash scripts/config.sh"
//             }
//         }
//         stage('Deploy Stack'){
//             steps{
//                 sh "bash scripts/deploy.sh"
//             }
//         }
//     }
// } 

pipeline{

        agent any

        stages{

            stage('Testing'){

                steps{

                    sh "bash test.sh"

                }

            }

        }

}

         stage('Build and push images') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"
            }