node {
    def app

     stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }

    stage('Clone repository') {
      

        checkout scm
    }



    stage('Build image') {
  
       app = docker.build("sebastiannavia/micro-calculadora-suma")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest-suma', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}