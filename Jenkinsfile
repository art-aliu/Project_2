pipeline{
        agent any
        stages{
            stage('Testing Services'){
                steps{
                    sh "bash test.sh"
                }
            }
        stage('Build images') {
            steps {
                sh "docker-compose build --parallel"
            }
        }
        stage('Deploy') {
            steps {
                sh "scp -i ~/.ssh/ansible_id docker-compose.yaml manager:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/ansible_id nginx.conf manager:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i configuration/inventory.yaml configuration/playbook.yaml"
            }
        }
    } 
}

