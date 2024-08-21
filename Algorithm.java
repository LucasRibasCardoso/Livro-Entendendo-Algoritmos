import java.util.ArrayList;
import java.util.List;

public class Algorithm {
    
    public static void main(String[] args) {
        List<Integer> numbersList = ListCreate(1000);
        
        boolean ifExist = BinarySearch(numbersList, 9);
        System.out.println("Exist this number: " + ifExist);
    }

    public static boolean BinarySearch(List<Integer> numbersList, int target) {

        int low = 0;
        int cont = 0;
        int high = numbersList.size() - 1;

        while (low <= high) {
            int half = (low + high) / 2;
            int pivot = numbersList.get(half);
            
            cont += 1;

            if (pivot == target) {
                System.out.println("Iterations: " + cont);
                return true;
            }
            if (pivot > target) {
                high = half - 1;
            }
            if (pivot < target) {
                low = half + 1;
            }
        }
        return false;
    }

    public static List<Integer> ListCreate(int size) {
        List<Integer> numbers = new ArrayList<>();
        
        for(int i = 0; i < size; i++) {
            numbers.add(i);
        }
        return numbers;
    }
}
