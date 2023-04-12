pipeline
{
    agent any
    parameters{
        string(name:"VERSION1",defaultValue: "", description: "Version of the application")
        // choice(name:"VERSION",choices:['1','2','3'],description: "Environment to deploy")
        booleanParam(name:"VERSION",defaultValue: true,description: "Environment to deploy")
    }
    stages
    {
        stage('Build')
        {

            steps
            {
                echo 'Building...'
            }
        }
        stage('Test')
        {
            steps
            {
                echo 'Testing...'
            }
        }
        stage('Deploy')
        {
            steps
            {
                echo 'Deploying...'
                echo "Deploying Version: ${params.VERSION1}"
            }
        }
    }

}



