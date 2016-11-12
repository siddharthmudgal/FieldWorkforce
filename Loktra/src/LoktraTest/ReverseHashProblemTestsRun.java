package LoktraTest;

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class ReverseHashProblemTestsRun {
    public static void main(String[] args){
        Result result = JUnitCore.runClasses(ReverseHashProblemTest.class);
        for (Failure failure:result.getFailures()){
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()){
            System.out.println("Tests ran successfully");
        }
    }
}
