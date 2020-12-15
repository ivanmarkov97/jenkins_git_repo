pipeline {
    agent any
    stages {
        stage( ' Example ' ) {
            steps {
                echo ' Hello World '   // Это отдельный вызов функции
                script {               // Это скрипт
                    def  browsers = [ ' chrome ' , ' firefox ' ]
                    for  ( int  i = 0 ; i < browsers.size(); ++i) {
                        echo " Testing the ${ browsers[i] }  browser "
                    }
                }
            }
        }
    }
}