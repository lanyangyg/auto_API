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
            // 生成 Allure 报告
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])

            // 发送邮件
            emailext (
                subject: "[${currentBuild.result}] ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                to: 'fnnnfnnfn@126.com',
                mimeType: 'text/html',
                body: """
                <h3>Jenkins 自动发送，请勿回复</h3>
                <p>构建结果：<b>${currentBuild.result ?: 'SUCCESS'}</b></p>
                <p>Allure 测试报告：<a href="${BUILD_URL}allure">${BUILD_URL}allure</a></p>
                <p>构建日志：<a href="${BUILD_URL}console">${BUILD_URL}console</a></p>
                """,
                attachLog: true     // 控制台日志作为附件
            )
        }
    }
}