## Task

Write code to find a string of characters that contains only letters from

`acdegilmnoprstuw`

such that the hash(the_string) is

`930846109532517`

if hash is defined by the following pseudo-code:

```
Int64 hash (String s) {
    Int64 h = 7
    String letters = "acdegilmnoprstuw"
    for(Int32 i = 0; i < s.length; i++) {
        h = (h * 37 + letters.indexOf(s[i]))
    }
    return h
}
```

For example, if we were trying to find the 7 letter string where `hash(the_string)` was `680131659347`, the answer would be "leepadg".


## Instructions to run the program

Environment Setup (for windows):
•	Make sure JDK is installed and %JAVA_HOME% is set to it.
•	Create a folder named “Project” in any directory.
•	Copy paste the following file in this folder
o	Loktra.jar

•	Open command prompt to the path “/Project”.
•	Run below commands to run
o	“java -jar Loktra.jar 680131659347”
o	“java -jar Loktra.jar”
•	Run below commands to run the Unit Test Cases
o	“java -cp Loktra.jar LoktraTest.ReverseHashProblemTestsRun.java”





