/**
 * Each character on a computer is assigned a unique code and the preferred
 * standard is ASCII (American Standard Code for Information Interchange).
 * For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
 *
 * A modern encryption method is to take a text file, convert the bytes to
 * ASCII, then XOR each byte with a given value, taken from a secret key.
 * The advantage with the XOR function is that using the same encryption
 * key on the cipher text, restores the plain text; for example,
 * 65 XOR 42 = 107, then 107 XOR 42 = 65.
 *
 * For unbreakable encryption, the key is the same length as the plain text
 * message, and the key is made up of random bytes. The user would keep the
 * encrypted message and the encryption key in different locations, and
 * without both "halves", it is impossible to decrypt the message.

 * Unfortunately, this method is impractical for most users, so the modified
 * method is to use a password as a key. If the password is shorter than the
 * message, which is likely, the key is repeated cyclically throughout the
 * message. The balance for this method is using a sufficiently long password
 * key for security, but short enough to be memorable.

 * Your task has been made easy, as the encryption key consists of three
 * lower case characters. Using cipher.txt (right click and 'Save
 * Link/Target As...'), a file containing the encrypted ASCII codes, and
 * the knowledge that the plain text must contain common English words,
 * decrypt the message and find the sum of the ASCII values in the original text.
 **/

import java.io.FileNotFoundException;
import java.util.Iterator;
import java.util.Scanner;
import java.io.File;

public class p059 {
  
  public static void main(String[] args){
    
    String contents  = null;
    Scanner sc = null;
    try {
      sc = new Scanner(new File("cipher.txt"));
      contents = sc.nextLine();
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    } finally {
      sc.close();
    }
    
    // Extract the message into a int array
    String[] arr = contents.split(",");
    int[] intContents = new int[arr.length];
    for (int i = 0; i < arr.length; i++) {
      intContents[i] = Integer.parseInt(arr[i]);
    }

    // Iterate over all passwords. Making the iterator is probably
    // overkill here. Could use some nested for loops instead.
    PasswordIterator iterator = new PasswordIterator();
    int[] password = null;
    int[] decrypted = null;
    while (iterator.hasNext()) {
      password = iterator.next();

      decrypted = decr(intContents, password);
      if (isEnglish(decrypted)) {
        // Uncomment to view the decrypted message
        //  System.out.println(intArrayToString(decrypted));
        break;
      }
    }
    
    int sum = 0;
    for (int i = 0; i < decrypted.length; i++) {
      sum += decrypted[i];
    }
        
    System.out.println(sum);
  }
  
  /**
   * Applies the encryption algorithm to the message.
   */
  private static int[] decr(int[] message, int[] password) {
    int[] result = message.clone();
    
    for (int i = 0; i < result.length; i++) {
      result[i] = result[i]^password[i%(password.length)];
    }
    return result;
  }
  
  
  // Determines if a message is english.
  private static boolean isEnglish(int[] msg) {
    // A simplistic test: just check that the combined frequency of (a,e,o,t)
    // is at least 30 times the combined frequency of (j,q,x,z).
    // The actual expected ratio of these frequencies is around 80 in English text.
    int[] freq = new int[26];
    for (int i = 0; i < msg.length; i++) {
      char c = Character.toLowerCase((char) msg[i]);
      int v = c - 'a';
      if (v >= 0 && v < freq.length) {
        freq[v]++;
      }
    }
    int a = freq[0];
    int e = freq[4];
    int o = freq[14];
    int t = freq[19];
    int j = freq[9];
    int q = freq[16];
    int x = freq[23];
    int z = freq[25];
    
    return (j+q+x+z) == 0 || (a+e+o+t)/(j+q+x+z) > 30;
  }
  
  private static int[] strToIntArray(String s) {
    int[] arr = new int[s.length()];
    for (int i = 0; i < s.length(); i++) {
      arr[i] = s.charAt(i);
    }
    return arr;
  }

  private static String intArrayToString(int[] arr) {
    StringBuffer s = new StringBuffer();
    for (int i = 0; i < arr.length; i++) {
      s.append((char)arr[i]);
    }
    return s.toString();
  }
}




/**
 * Iterates over possible passwords.
 */
class PasswordIterator implements Iterator<int[]>{
  
  private int char1;
  private int char2;
  private int char3;
  
  // The internal representation is an array of integers, 
  // each one ranging from 0-25.
  private int[] chars;
  
  public  PasswordIterator() {
    chars = new int[3];
  }

  @Override
  public boolean hasNext() {
    return !(char1 == 25 && char2 == 25 & char3 == 25);
  }

  @Override
  public int[] next() {
    // Store current value to be returned.
    int[] result = new int[3];
    for (int i = 0; i < 3; i++) {
      result[i] = 'a' + chars[i];
    }
    
    // Increment current value.
    boolean carryIn = true;
    boolean carryOut = false;
    for (int i = 0; i < 3; i++) {
      carryOut = carryIn && chars[i] == 25;
      if (carryIn) {
        chars[i] = (chars[i] + 1) % 26;
      }
      // Update for next digit.
      carryIn = carryOut;
    }
    
    return result;
  }

  @Override
  public void remove() {
    // No need to support this.
    throw new UnsupportedOperationException();
  }
}