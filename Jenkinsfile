CODE_CHANGES=getGitChanges() //Get the changes in the git repository
pipeline
{
    agent any
    tools { 
        
    }
    parameters{
        string(name:"VERSION1",defaultvalue: "", description: "Version of the application")
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
            when{
                expression{ //Conditional expression
                    BRANCH_NAME == 'dev' || BRANCH_NAME == 'master'
                }
            }
            when {
                expression{
                        params.VERSION
                }
            }
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
    post //Executes after the pipeline is completed
    {
        always{ //Executes after the pipeline is completed and it's actually conditional 

        }
        success{ //Executes after the pipeline is completed and it's actually conditional 

        }
        failure{ //Executes after the pipeline is completed and it's actually conditional 

        }
    }
}



