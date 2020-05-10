pipeline {
    agent any
    
    stages {
        stage("Git clone") {
            steps {
                //git clone  
                deleteDir()
                echo 'Clone the latest code from the code-base'
                sh 'git clone https://github.com/mrajesh712/icavtech-challenge.git'       
            }
            
        }
        stage("Testcases") {
            steps {
                //Execute testcases 
                echo 'Execute test cases'
                dir("loan-repayment-plan-generator"){
                    sh 'mvn clean test' 
                }               
            }
            
        }
        stage("Maven Build") {
            steps {
                echo 'Execute Maven Build'
                dir("loan-repayment-plan-generator"){
                    sh 'mvn clean package'
                }
            }
            
        }
        stage("Docker Build") {            
            steps {
                echo 'Execute Docker Build'
                dir("icavtech-challenge"){
                    sh "docker build -t icavtechicontainer.azurecr.io/icavtech-challenge:\"${env.BUILD_NUMBER}\" . "
                    //sh 'docker push'
                    echo "Check the Docker image"
                    sh 'docker images'
                }
            }
            
        }
        stage("Deployment") {
            steps {
                dir("icavtech-challenge"){
                    sh "docker run -d -p 5000:5000 icavtechicontainer.azurecr.io/icavtech-challenge:\"${env.BUILD_NUMBER}\""
                }
            }            
        }
      
    }//end stages
}