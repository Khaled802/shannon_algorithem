# Shannon-Fano

## definition
   - It is a mathimatical algorithm used for compression by Claude Shannon
   - It is lossless algorithm
     - that reduce the size of data without lossing information

## steps
   1. Determine the frequency of each symbol: The first step in the Shannon algorithm is to determine the frequency of each symbol in the message to be compressed. This can be done by counting the number of occurrences of each symbol.

   2. Calculate the probability of each symbol: Once the frequency of each symbol is known, the probability of each symbol is calculated by dividing its frequency by the total number of symbols in the message. This step generates a set of probabilities that sum to 1.

   3. Sort the symbols by probability: The symbols are then sorted in descending order of probability, with the most frequent symbol at the top of the list.

   4. Assign binary codes to each symbol: The next step is to assign binary codes to each symbol based on its probability. The most frequent symbol is assigned the shortest binary code (such as 0), and the least frequent symbol is assigned the longest binary code (such as 111...1). The binary codes are assigned in a way that ensures that no two codes are identical.

   5. Encode the message: Once the binary codes have been assigned to each symbol, the original message is encoded by replacing each symbol with its corresponding binary code.


## Efficiency

   The efficiency of a compression algorithm can be calculated using the following formula:

   Efficiency = (1 - Compressed Size / Original Size) x 100%

   Where:
      Compressed Size: the size of the data after compression
      Original Size: the size of the data before compression