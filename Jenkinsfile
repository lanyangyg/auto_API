pipeline {
    agent any

    environment {
        CI = 'true'
    }

    stages {
        stage('Prepare') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('API Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
            // Email-ext 邮件插件配置
            emailext (
                subject: "[${currentBuild.result}] ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: '详见附件 Allure 报告',
                to: 'fnnnfnnfn@126.com',
                attachLog: true
            )
        }
    }
}