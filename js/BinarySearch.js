function binarySearch(arr, target) {
    const mid = Math.floor(arr.length / 2)  
    
    if (arr[mid] === target) {
        return arr[mid];
    }

    if (arr[mid] < target && arr.length > 1) {
        return binarySearch(arr.slice(mid), target);
    }

    if (arr[mid] > target && arr.length > 1) {
        return binarySearch(arr.slice(0, mid), target);
    }

    return -1;
}

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 10)); //10