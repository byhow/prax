package com.acme;

import java.util.HashMap;
import java.util.Map;

public class FindDup {
    public static int notDup(int[] arr) {
        Map<Integer, Integer> occ = new HashMap<>();

        for (int i = 0; i < arr.length; i++) {
            if (occ.containsKey(arr[i])) {
                occ.put(arr[i], occ.get(arr[i]) + 1);
            } else {
                occ.put(arr[i], 1);
            }
        }

        for (int i : occ.keySet()){
            if (occ.get(i) == 1) {
                return i;
            }
        }
        return 0;
    }

}
