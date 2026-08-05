import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

/**
 * Demonstrates three interview approaches to the same Two Sum problem.
 *
 * <p>The methods return the original array indices or an empty array when no
 * solution exists. The input array is never modified.</p>
 */
public final class TwoSumThreeApproaches {

    private TwoSumThreeApproaches() {
        // Utility class.
    }

    public static int[] bruteForce(int[] values, int target) {
        requireInput(values);

        for (int left = 0; left < values.length; left++) {
            for (int right = left + 1; right < values.length; right++) {
                if ((long) values[left] + values[right] == target) {
                    return new int[]{left, right};
                }
            }
        }
        return new int[0];
    }

    public static int[] sortAndTwoPointers(int[] values, int target) {
        requireInput(values);

        IndexedValue[] indexed = new IndexedValue[values.length];
        for (int index = 0; index < values.length; index++) {
            indexed[index] = new IndexedValue(values[index], index);
        }
        Arrays.sort(indexed, Comparator.comparingInt(IndexedValue::value));

        int left = 0;
        int right = indexed.length - 1;
        while (left < right) {
            long sum = (long) indexed[left].value() + indexed[right].value();
            if (sum == target) {
                int first = indexed[left].originalIndex();
                int second = indexed[right].originalIndex();
                return first < second
                        ? new int[]{first, second}
                        : new int[]{second, first};
            }
            if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[0];
    }

    public static int[] hashMapOnePass(int[] values, int target) {
        requireInput(values);

        Map<Integer, Integer> indexByValue = new HashMap<>();
        for (int index = 0; index < values.length; index++) {
            long required = (long) target - values[index];
            if (required >= Integer.MIN_VALUE && required <= Integer.MAX_VALUE) {
                Integer matchIndex = indexByValue.get((int) required);
                if (matchIndex != null) {
                    return new int[]{matchIndex, index};
                }
            }
            indexByValue.putIfAbsent(values[index], index);
        }
        return new int[0];
    }

    private static void requireInput(int[] values) {
        if (values == null) {
            throw new IllegalArgumentException("values must not be null");
        }
    }

    private record IndexedValue(int value, int originalIndex) {
    }

    public static void main(String[] args) {
        int[] values = {2, 7, 11, 15};
        int target = 9;
        int[] expected = {0, 1};

        assertResult("bruteForce", expected, bruteForce(values, target));
        assertResult("sortAndTwoPointers", expected, sortAndTwoPointers(values, target));
        assertResult("hashMapOnePass", expected, hashMapOnePass(values, target));

        assertResult("duplicate values", new int[]{0, 1}, hashMapOnePass(new int[]{3, 3}, 6));
        assertResult("no solution", new int[0], hashMapOnePass(new int[]{1, 2, 3}, 100));

        System.out.println("All Two Sum sample checks passed.");
    }

    private static void assertResult(String name, int[] expected, int[] actual) {
        if (!Arrays.equals(expected, actual)) {
            throw new AssertionError(
                    name + " expected " + Arrays.toString(expected)
                            + " but received " + Arrays.toString(actual));
        }
    }
}
