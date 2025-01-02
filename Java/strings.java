class strings{
    public static void main(String[] args) {
        String words = "Taco Cat Test Muffin";
        String word = "Test";
        int indexstart = words.indexOf(word);
        int indexend = indexstart + word.length();

        System.out.print(indexstart);
        System.out.print(":");
        System.out.print(indexend);

    }
}