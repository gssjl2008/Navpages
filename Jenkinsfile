def createVersion() {
	// 定义一个版本号作为当次构建的版本，输出结果 20191210175842_69
    return new Date().format('yyyyMMddHHmmss') + "_${env.BUILD_ID}"
}

pipeline {
    agent {
        label 'k8s-node'
    }

    environment {
        gitlab_id = "438e5486-9fac-4cb8-8351-2951c8d42790"
        gitlab_repo = "http://192.168.50.182:31001/wx/pages.git"
        docker_id = "a83a4d6c-3b91-4717-a1c3-23f519c1aced"
        docker_registory = "192.168.50.182:30082"
        docker_repo = "gssjl2008"
        image_name = "pages"
        image_version = createVersion()
        kube_yaml = "pages.yaml"
        kube_ns = "default"
    }

    stages {

        stage("代码检出"){
            steps{
                git credentialsId: gitlab_id, url: gitlab_repo
            }
        }

        stage("打包"){
            steps{
                withCredentials([usernamePassword(credentialsId:  gitlab_id, passwordVariable: 'password', usernameVariable: 'username')]) {
                    sh """
                echo y | docker system prune -a
                docker build -t ${docker_registory}/${docker_repo}/${image_name}:${image_version} .
                docker login  ${docker_registory} -u ${username} -p ${password}
                docker tag ${docker_registory}/${docker_repo}/${image_name}:${image_version} ${docker_registory}/${docker_repo}/${image_name}:latest
                docker push ${docker_registory}/${docker_repo}/${image_name}:latest
                kubectl get pod -n jenkins
                """
                }
            }
        }

        stage("部署"){
            steps{
                timeout(time: 60, unit: 'SECONDS') {
                    sh """
                        kubectl delete -f ${kube_yaml} -n ${kube_ns} || echo "First deploy in k8s"
                        kubectl apply -f ${kube_yaml} -n ${kube_ns}
                    """
                }
            }
        }
    }
}
