int firstDuplicate(int[] a) {

    int duplicate;
    int lowestIndex = 0;

    for (int i = 0; i < a.length; i++){
        duplicate = a[i];
        if (a[i] == duplicate){
            lowestIndex = i;
           if (lowestIndex < i){
               lowestIndex = i;
           }
        }

    }

    return a[lowestIndex];

}
