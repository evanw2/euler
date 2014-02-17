
object Euler001 {
   def main(args: Array[String]) {
      var total = 0
      for( i <- 1 to 999 ){
         if( i % 3 == 0 || i % 5 == 0 ){
            total += i
         }
      }
      println(total)
   }
}


