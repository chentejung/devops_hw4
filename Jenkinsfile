pipeline {
    // Run everything on the Target Server's Docker Agent
    agent { label 'docker-v1' } 

    parameters {
        file(name: 'Chicago_Restaurant_Data.csv', description: 'Upload the Chicago Restaurant CSV file')
    }

    environment {
        MYSQL_PW        = credentials('mysql-root-pw')
        DB_NAME         = 'restaurant_db'
        DB_CONTAINER_NAME  = 'my-mysql-db'
        WEB_CONTAINER_NAME = 'web-restaurant'
        NETWORK_NAME    = 'restaurant_net'
        BASE_IMAGE      = 'mysql:8.0'
        FOLDER1         = 'db_setup'
        FOLDER2         = 'import_data'
        FOLDER3         = 'web_setup'
        SONAR_AUTH_TOKEN   = credentials('7f94b206-0044-4e6f-a11c-f9c07471db31') // Create this in Jenkins Credentials
    }

    stages {
        stage('DB_setup') {
            steps {
                script {
                    def setup = load "${env.FOLDER1}/Jenkinsfile"
                }
            }
        }

        stage('Import_data') {
            steps {
                script {
                    def importer = load "${env.FOLDER2}/Jenkinsfile"
                }
            }
        }

        stage('Web_setup') {
            steps {
                script {
                    def verify = load "${env.FOLDER3}/Jenkinsfile"
                }
            }
        }
        stage('E2E Testing') {
            steps {
                echo 'Running Selenium Tests...'
                dir('tests/e2e') {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest test_user_workflow.py --html=report.html --self-contained-html'
                }
            }
            post {
                always {
                    // Archive the HTML report so it's viewable in Jenkins
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, 
                        reportDir: '.', reportFiles: 'report.html', reportName: 'E2E Report'])
                }
            }
        }
    }
}