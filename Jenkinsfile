CODE_CHANGES=getGitChanges() //Get the changes in the git repository
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
            when{
                expression{ //Conditional expression
                    BRANCH_NAME == 'dev' && CODE_CHANGES == true
                }
            }
            steps
            {
                echo 'Building...'
            }
        }
        stage('Test')
        {
            steps
            {
                when {
                    expression
                {
                        params.VERSION
                }
               }
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



