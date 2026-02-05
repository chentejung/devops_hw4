pipeline {
    // Run everything on the Target Server's Docker Agent
    agent { label 'docker-v1' } 

    parameters {
        file(name: 'Chicago_Restaurant_Data.csv', description: 'Upload the Chicago Restaurant CSV file')
    }

    environment {
        MYSQL_PW        = credentials('mysql-root-pw')
        DB_NAME         = 'restaurant_db'
        CONTAINER_NAME  = 'my-mysql-db'
        NETWORK_NAME    = 'restaurant_net'
        BASE_IMAGE      = 'mysql:8.0'
        FOLDER1         = 'db_setup'
        FOLDER2         = 'import_data'
        FOLDER3         = 'web_setup'
        SONAR_SERVER_URL = "http://localhost:9000"
        SONAR_TOKEN      = credentials('7f94b206-0044-4e6f-a11c-f9c07471db31') // Create this in Jenkins Credentials
    }

    stages {
        stage('DB_setup') {
            steps {
                script {
                    // Load the setup script
                    def setup = load "${env.FOLDER1}/Jenkinsfile"
                }
            }
        }

        stage('Import_data') {
            steps {
                script {
                    // Load the import script
                    def importer = load "${env.FOLDER2}/Jenkinsfile"
                }
            }
        }

        stage('Web_setup') {
            steps {
                script {
                    // Load the verification script
                    def verify = load "${env.FOLDER3}/Jenkinsfile"
                }
            }
        }
    }
}