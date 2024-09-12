pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Create a virtual environment if it doesn't exist
                    if (!fileExists('venv')) {
                        bat '''
                        python -m venv venv
                        '''
                    }
                }
            }
        }

        stage('Install Dependencies and Run Tests') {
            steps {
                bat '''
                REM Activate the virtual environment
                call venv\\Scripts\\activate

                REM Install required dependencies
                pip install -r requirements.txt

                REM Run Django tests
                python manage.py test
                '''
            }
        }

        stage('Run Server') {
            steps {
                bat '''
                REM Activate the virtual environment
                call venv\\Scripts\\activate

                REM Run Django development server
                python manage.py runserver 0.0.0.0:8000
                '''
            }
        }
    }

    post {
        always {
            // Clean up virtual environment after job execution if needed
            cleanWs()
        }
    }
}
