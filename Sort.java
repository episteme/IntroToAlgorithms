public class Sort {
    public static void main(String[] args) {
        int[] a = {31, 41, 59, 26, 41, 58};
        insertionSort(a);
        for(int i : a) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    private static void insertionSort(int[] a) {
        for(int i = 2; i < a.length; i++) {
            int j = i - 1;
            int key = a[i];
            while(j >= 0 && a[j] < key) {
                a[j+1] = a[j];
                j--;
            }
            a[j+1] = key;
        }
    }
}
